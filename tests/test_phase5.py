import time
import pytest
from evidence.storage import pin_json, fetch_json
from evidence.packer import build_evidence_pack
from chain.client import ChainClient
from solvers.p1_allocation import P1AllocationSolvers
from solvers.p2_dispute import P2DisputeSolvers
from chain.commit import commit_allocation_from_run, commit_dispute_resolution_from_run

def test_storage_pinning_and_retrieval():
    payload = {"test_key": "agrotrace_val_2026", "nonce": 9999}
    cid, sha256_hex, mode = pin_json(payload)
    assert cid.startswith("bafy")
    assert len(sha256_hex) == 64
    assert mode in ("ipfs", "local-cas")

    fetched = fetch_json(cid)
    assert fetched["test_key"] == "agrotrace_val_2026"
    assert fetched["nonce"] == 9999

def test_evidence_packer():
    client = ChainClient()
    if not client.is_connected() or not client.contract:
        pytest.skip("Local Hardhat node is not running or contract is unconfigured.")

    pack = build_evidence_pack(lot_id=2, client=client)
    assert pack["lot"]["id"] == 2
    assert "quality_grade" in pack
    assert "audit_trail_verification" in pack
    assert pack["storage"] in ("ipfs", "local-cas")
    assert pack["evidence_cid"].startswith("bafy")

def test_commit_allocation_on_chain():
    client = ChainClient()
    if not client.is_connected() or not client.contract:
        pytest.skip("Local Hardhat node is not running.")

    # 1. Register a fresh lot for testing
    client.send_tx("FARMER", "registerLot", "WHEAT_SHARBATI", 500000, "Test-Field-Commit")
    lot_id = client.contract.functions.lotCounter().call()

    # 2. Attest Grade 3
    dummy_hash = bytes.fromhex("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    client.send_tx("GRADER", "attestGrade", lot_id, 3, 1100, 50, "bafy_test_cid", dummy_hash)

    # 3. Create a fresh procurement contract
    now = int(time.time())
    client.send_tx("PROCESSOR", "createContract", "WHEAT_SHARBATI", 1000000, 2, 3200, [9000, 10000, 11500], now + 86400, 50000)
    c_id = client.contract.functions.contractCounter().call()

    lots = [{"id": lot_id, "weight_g": 500000, "grade": 3}]
    contracts = [{"id": c_id, "qty_g": 1000000, "min_grade": 2, "base_price_paise": 3200}]

    solver_run = P1AllocationSolvers.solve_exact(lots, contracts)
    res = commit_allocation_from_run(solver_run, contract_id=c_id, client=client, role_name="PROCESSOR")

    assert res["status"] == "COMMITTED"
    assert res["tx_hash"].startswith("0x")
    assert res["contract_id"] == c_id
    assert res["storage"] in ("ipfs", "local-cas")

def test_commit_dispute_resolution_on_chain():
    client = ChainClient()
    if not client.is_connected() or not client.contract:
        pytest.skip("Local Hardhat node is not running.")

    claims = [
        {"id": 101, "amount_paise": 1920000, "lot_id": 2},
        {"id": 102, "amount_paise": 1920000, "lot_id": 2}
    ]
    conflicts = [(101, 102)]

    solver_run = P2DisputeSolvers.solve_exact(claims, conflicts)
    res = commit_dispute_resolution_from_run(solver_run, lot_id=2, client=client, role_name="AUDITOR")

    assert res["status"] == "DISPUTE_RESOLVED"
    assert res["tx_hash"].startswith("0x")
    assert res["lot_id"] == 2
    assert res["storage"] in ("ipfs", "local-cas")
