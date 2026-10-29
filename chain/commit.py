from typing import Any, Dict, List
from web3 import Web3
from chain.client import ChainClient
from solvers.base import SolverRun
from evidence.storage import pin_json

def commit_allocation_from_run(
    solver_run: SolverRun,
    contract_id: int,
    client: ChainClient = None,
    role_name: str = "PROCESSOR"
) -> Dict[str, Any]:
    if client is None:
        client = ChainClient()

    if not client.contract:
        raise RuntimeError("Smart contract not connected. Start node and deploy first.")

    run_dict = solver_run.to_dict()
    cid, sha256_hex, storage_mode = pin_json(run_dict)

    allocations_for_contract = solver_run.decoded_solution.get(contract_id, {})
    lot_ids: List[int] = []
    weights_g: List[int] = []

    for l_id, w in allocations_for_contract.items():
        if w > 0:
            lot_ids.append(int(l_id))
            weights_g.append(int(w))

    if not lot_ids:
        raise ValueError(f"No positive allocations found for contract {contract_id} in solver run.")

    sha256_bytes = bytes.fromhex(sha256_hex)

    receipt = client.send_tx(
        role_name,
        "commitAllocation",
        contract_id,
        lot_ids,
        weights_g,
        cid,
        sha256_bytes
    )

    tx_hash = Web3.to_hex(receipt.transactionHash)

    return {
        "status": "COMMITTED",
        "tx_hash": tx_hash,
        "block_number": receipt.blockNumber,
        "contract_id": contract_id,
        "lot_ids": lot_ids,
        "weights_g": weights_g,
        "solver_run_cid": cid,
        "solver_run_sha256": f"0x{sha256_hex}",
        "storage": storage_mode
    }

def commit_dispute_resolution_from_run(
    solver_run: SolverRun,
    lot_id: int,
    client: ChainClient = None,
    role_name: str = "AUDITOR"
) -> Dict[str, Any]:
    if client is None:
        client = ChainClient()

    if not client.contract:
        raise RuntimeError("Smart contract not connected.")

    run_dict = solver_run.to_dict()
    cid, _, storage_mode = pin_json(run_dict)

    rejected_claims = solver_run.decoded_solution.get("rejected_claim_ids", [])

    receipt = client.send_tx(
        role_name,
        "resolveDispute",
        lot_id,
        rejected_claims,
        cid
    )

    tx_hash = Web3.to_hex(receipt.transactionHash)

    return {
        "status": "DISPUTE_RESOLVED",
        "tx_hash": tx_hash,
        "block_number": receipt.blockNumber,
        "lot_id": lot_id,
        "rejected_claim_ids": rejected_claims,
        "solver_run_cid": cid,
        "storage": storage_mode
    }
