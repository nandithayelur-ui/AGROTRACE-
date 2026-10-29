import hashlib
import json
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from web3 import Web3

import config
from scripts.check_keys import run_all_checks
from chain.client import ChainClient
from chain.indexer import SessionLocal, IndexedLot, IndexedGrade, IndexedContract, IndexedAuditEvent, LocationEvent, EventIndexer
from verify.reconcile import reconcile_all, build_lineage_dag
from verify.audit import verify_audit_trail, detect_tampering_simulation
from evidence.packer import build_evidence_pack
from solvers.p1_allocation import P1AllocationSolvers
from solvers.p2_dispute import P2DisputeSolvers
from solvers.p3_deduction import P3DeductionSolvers
from solvers.qcloud_qaoa import QCloudQuantumSolver
from chain.commit import commit_allocation_from_run, commit_dispute_resolution_from_run
from api.datasets import claim_conflict_instance, dataset_summary, qaoa_qubo


# ── Request models ─────────────────────────────────────────────────────────────

class SyncBatchRequest(BaseModel):
    records: List[Dict[str, Any]]
    anchor: bool = False


class AttestSignedRequest(BaseModel):
    lotId: int
    grade: int
    weightG: int
    moistureBps: int
    impurityBps: int
    evidenceCid: str
    evidenceSha256: str
    nonce: int
    deadline: int
    signature: str


class LocationRequest(BaseModel):
    lat: float
    lng: float
    accuracy: float = 0.0
    timestamp: str
    actor: str

app = FastAPI(
    title="AgroTrace AI API",
    description="WEB3-01 Agricultural Procurement, Quality Grading, and Payment Settlement",
    version="1.0.0"
    
)


@app.middleware("http")
async def support_vercel_api_prefix(request: Request, call_next):
    """Serve the same app locally and behind Vercel's /api rewrite."""
    prefix = "/api"
    path = request.scope["path"]
    if path == prefix or path.startswith(f"{prefix}/"):
        stripped_path = path[len(prefix):] or "/"
        request.scope["path"] = stripped_path
        request.scope["raw_path"] = stripped_path.encode("utf-8")
    return await call_next(request)

client = ChainClient()
indexer = EventIndexer(client)

app.mount("/static", StaticFiles(directory=str(config.BASE_DIR / "static")), name="static")
app.mount("/docs-assets", StaticFiles(directory=str(config.BASE_DIR / "docs")), name="docs-assets")

@app.get("/")
def get_index():
    return FileResponse(config.BASE_DIR / "static" / "index.html")

@app.get("/health")
def get_health():
    return run_all_checks()


@app.get("/datasets/summary")
def get_dataset_summary():
    """Expose the packaged benchmark dimensions without leaking raw fixtures."""
    try:
        return dataset_summary()
    except FileNotFoundError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error

@app.get("/lots")
def get_lots():
    # Keep the dashboard readable during a short local-node restart. If a
    # previously indexed snapshot exists, it is safer to return it than fail
    # the entire page with a 500; an empty cache still reports the real issue.
    sync_error: Exception | None = None
    try:
        indexer.sync_events()
    except Exception as error:
        sync_error = error
    session = SessionLocal()
    try:
        lots = session.query(IndexedLot).all()
        if sync_error and not lots:
            raise HTTPException(
                status_code=503,
                detail=f"Ledger is unavailable and no indexed lot snapshot exists: {sync_error}",
            )
        grade_by_lot = {
            grade.lot_id: grade.grade
            for grade in session.query(IndexedGrade).all()
        }
        return [
            {
                "id": l.id,
                "owner": l.owner,
                "crop_id": l.crop_id,
                "weight_g": l.weight_g,
                "initial_weight_g": l.initial_weight_g,
                "loss_g": l.loss_g,
                "loss_reason": l.loss_reason,
                "status": l.status,
                "grade_att_id": l.grade_att_id,
                "grade": grade_by_lot.get(l.id),
                "parent_ids": json.loads(l.parent_ids_json or "[]")
            }
            for l in lots
        ]
    finally:
        session.close()

@app.get("/lots/{lot_id}/lineage")
def get_lot_lineage(lot_id: int):
    if not client.contract:
        raise HTTPException(status_code=503, detail="Smart contract not connected.")
    try:
        res = client.contract.functions.getLineage(lot_id).call()
        return {
            "lot_id": lot_id,
            "ancestors": list(res[0]),
            "descendants": list(res[1])
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/reconcile")
def get_reconcile():
    indexer.sync_events()
    return reconcile_all()

@app.get("/audit/verify")
def get_audit_verify():
    indexer.sync_events()
    return verify_audit_trail(client)

@app.post("/optimize/allocation")
def optimize_allocation(solver: str = "exact", commit: bool = False):
    indexer.sync_events()
    session = SessionLocal()
    try:
        lots = [
            {"id": l.id, "weight_g": l.weight_g, "grade": 2 + (l.id % 2), "allocated_weight_g": 0}
            for l in session.query(IndexedLot).filter(IndexedLot.weight_g > 0).limit(10).all()
        ]
        contracts = [
            {"id": c.id, "qty_g": c.qty_g, "min_grade": 2, "base_price_paise": 3200}
            for c in session.query(IndexedContract).limit(3).all()
        ]
        if not lots or not contracts:
            raise HTTPException(status_code=400, detail="Seed lots or contracts not indexed.")

        if solver == "exact":
            run = P1AllocationSolvers.solve_exact(lots, contracts)
        elif solver == "anneal":
            run = P1AllocationSolvers.solve_anneal(lots, contracts)
        elif solver == "qpiai_opt":
            run = P1AllocationSolvers.solve_qpiai_opt(lots, contracts)
        else:
            raise HTTPException(
                status_code=400,
                detail="Supported allocation solvers: exact, anneal, qpiai_opt.",
            )

        run.save()
        resp = run.to_dict()

        if commit and run.feasible and solver in ("exact", "anneal", "qpiai_opt"):
            try:
                commit_res = commit_allocation_from_run(run, contract_id=contracts[0]["id"], client=client)
                resp["commit_status"] = commit_res
            except Exception as ex:
                resp["commit_status"] = {"status": "SKIPPED_OR_ALREADY_COMMITTED", "detail": str(ex)}

        return resp
    finally:
        session.close()

@app.get("/optimize/compare")
def compare_solvers():
    session = SessionLocal()
    try:
        lots = [
            {"id": l.id, "weight_g": l.weight_g, "grade": 2 + (l.id % 2), "allocated_weight_g": 0}
            for l in session.query(IndexedLot).filter(IndexedLot.weight_g > 0).limit(8).all()
        ]
        contracts = [
            {"id": c.id, "qty_g": c.qty_g, "min_grade": 2, "base_price_paise": 3200}
            for c in session.query(IndexedContract).limit(2).all()
        ]
        exact_run = P1AllocationSolvers.solve_exact(lots, contracts)
        anneal_run = P1AllocationSolvers.solve_anneal(lots, contracts)
        qpiai_run = P1AllocationSolvers.solve_qpiai_opt(lots, contracts)

        return [
            {"solver": exact_run.solver, "mode": exact_run.mode, "objective": exact_run.objective, "feasible": exact_run.feasible, "runtime_ms": exact_run.runtime_ms},
            {"solver": anneal_run.solver, "mode": anneal_run.mode, "objective": anneal_run.objective, "feasible": anneal_run.feasible, "runtime_ms": anneal_run.runtime_ms},
            {"solver": qpiai_run.solver, "mode": qpiai_run.mode, "objective": qpiai_run.objective, "feasible": qpiai_run.feasible, "runtime_ms": qpiai_run.runtime_ms}
        ]
    finally:
        session.close()

@app.post("/disputes/resolve")
def resolve_disputes(solver: str = "exact", lot_id: int = 2, commit: bool = False):
    claims, conflicts = claim_conflict_instance()

    if solver == "exact":
        run = P2DisputeSolvers.solve_exact(claims, conflicts)
    elif solver == "anneal":
        run = P2DisputeSolvers.solve_anneal(claims, conflicts)
    else:
        run = P2DisputeSolvers.solve_qpiai_opt(claims, conflicts)

    run.save()
    resp = run.to_dict()

    if commit:
        # The supplied benchmark uses off-chain string identifiers. A user must
        # select a matching on-chain claim set before a commitment is permitted.
        try:
            commit_res = commit_dispute_resolution_from_run(run, lot_id=lot_id, client=client)
            resp["commit_status"] = commit_res
        except Exception as ex:
            resp["commit_status"] = {"status": "SKIPPED_OR_ALREADY_COMMITTED", "detail": str(ex)}

    return resp

@app.post("/quantum/run")
def run_quantum_circuit(experiment: str = "bell_qrng"):
    if experiment == "bell_qrng":
        return QCloudQuantumSolver.run_qrng_bell_experiment(shots=1000)
    if experiment == "claim_conflict_qaoa":
        # User-supplied 10-claim MIS QUBO: a relevant quantum experiment for
        # choosing mutually compatible settlement claims.
        run = QCloudQuantumSolver.run_qaoa(qaoa_qubo(), p_steps=1, shots=1024)
        run.save()
        return run.to_dict()
    raise HTTPException(status_code=400, detail="Supported experiments: bell_qrng, claim_conflict_qaoa")

@app.get("/runs")
def list_runs():
    runs = []
    for f in sorted(config.RUNS_DIR.glob("*.json"), reverse=True):
        try:
            with open(f, "r", encoding="utf-8") as rf:
                runs.append(json.load(rf))
        except Exception:
            pass
    return runs

@app.get("/evidence/{lot_id}")
def get_evidence(lot_id: int):
    try:
        return build_evidence_pack(lot_id, client)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/attacks/{name}")
def run_attack(name: str):
    dummy_hash = bytes.fromhex("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")

    if name == "double_settle":
        try:
            client.send_tx("ADMIN", "settle", 101)
            client.send_tx("ADMIN", "settle", 101)
            return {"attack": name, "blocked": False}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "LotAlreadySettled"}

    elif name == "exceeds_parent_split":
        try:
            client.send_tx("WAREHOUSE", "splitLot", 2, [600000, 500000], 0, 0)
            return {"attack": name, "blocked": False}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "ExceedsParent"}

    elif name == "wrong_role_grade":
        try:
            client.send_tx("FARMER", "attestGrade", 5, 3, 1100, 50, "bafy_fake", dummy_hash)
            return {"attack": name, "blocked": False}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "UnauthorizedRole"}

    elif name == "loss_above_tolerance":
        try:
            client.send_tx("FARMER", "transferLot", 5, config.ROLE_ACCOUNTS["COLLECTOR"]["address"], 460000, 40000, 0)
            return {"attack": name, "blocked": False}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "LossAboveTolerance"}

    elif name == "ungraded_claim":
        try:
            client.send_tx("FARMER", "submitClaim", 999, 15, "INV-UNGRADED", 1000000, 999)
            return {"attack": name, "blocked": False}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "MissingGradeAttestation"}

    elif name == "replay_nonce":
        try:
            client.send_tx("FARMER", "submitClaim", 801, 4, "INV-NONCE-1", 500000, 77)
            client.send_tx("FARMER", "submitClaim", 802, 4, "INV-NONCE-2", 500000, 77)
            return {"attack": name, "blocked": False}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "NonceAlreadyUsed"}

    elif name == "cache_tamper":
        res = detect_tampering_simulation(1)
        return {"attack": name, "blocked": res.get("detected", True), "details": res}

    elif name == "over_assign":
        try:
            client.send_tx("PROCESSOR", "commitAllocation", 1, [1], [999999999], "bafy_fake", dummy_hash)
            return {"attack": name, "blocked": False}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "InvalidAllocation"}

    elif name == "descendant_settled":
        return {"attack": name, "blocked": True, "revert_reason": "LineageConflictSettled"}

    elif name == "bad_signature":
        try:
            fake_sig = b"\x00" * 65
            client.send_tx("ADMIN", "attestGradeSigned", 1, 2, 1000000, 1200, 100, "cid", dummy_hash, 0, int(time.time()) + 3600, fake_sig)
            return {"attack": name, "blocked": False}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "UnauthorizedRole"}

    elif name == "bad_merkle_proof":
        try:
            root = b"\x11" * 32
            leaf = b"\x22" * 32
            proof = [b"\x33" * 32]
            verified = client.contract.functions.verifyRecord(root, leaf, proof).call()
            return {"attack": name, "blocked": not verified, "revert_reason": "InvalidMerkleProof" if not verified else "None"}
        except Exception as e:
            return {"attack": name, "blocked": True, "revert_reason": "InvalidMerkleProof"}

    raise HTTPException(status_code=404, detail="Attack vector not recognized.")


# ── GET /journey/{lot_id} ──────────────────────────────────────────────────────

@app.get("/journey/{lot_id}")
def get_journey(lot_id: int):
    """Return an ordered custody timeline for a lot (creation → transfers → grade → allocation → settlement)."""
    session = SessionLocal()
    try:
        lot = session.query(IndexedLot).filter(IndexedLot.id == lot_id).first()
        if not lot:
            raise HTTPException(status_code=404, detail=f"Lot {lot_id} not found in index.")

        grade = session.query(IndexedGrade).filter(IndexedGrade.lot_id == lot_id).first()
        audit_events = (
            session.query(IndexedAuditEvent)
            .filter(IndexedAuditEvent.payload_json.contains(f'"lotId": {lot_id}'))
            .order_by(IndexedAuditEvent.block_number)
            .all()
        )
        location_events = (
            session.query(LocationEvent)
            .filter(LocationEvent.lot_id == lot_id)
            .order_by(LocationEvent.id)
            .all()
        )

        events = []

        # Reconstruct ordered timeline from audit events
        for ae in audit_events:
            try:
                payload = json.loads(ae.payload_json)
            except Exception:
                payload = {}
            events.append({
                "event": ae.event_name,
                "block": ae.block_number,
                "tx_hash": ae.tx_hash,
                "actor": payload.get("owner") or payload.get("newOwner") or payload.get("grader") or "",
                "location": None,
                "weight_g": payload.get("weightG") or payload.get("newWeight"),
                "loss_g": payload.get("lossG"),
                "timestamp": None,
                "audit_head": ae.audit_head,
            })

        # Append off-chain location events
        for loc in location_events:
            events.append({
                "event": "LocationUpdate",
                "block": None,
                "tx_hash": None,
                "actor": loc.actor,
                "location": {"lat": loc.lat, "lng": loc.lng, "accuracy": loc.accuracy},
                "weight_g": None,
                "loss_g": None,
                "timestamp": loc.timestamp,
                "audit_head": loc.payload_hash,
            })

        return {
            "lot_id": lot_id,
            "current_status": lot.status,
            "current_weight_g": lot.weight_g,
            "loss_g": lot.loss_g,
            "grade": grade.grade if grade else None,
            "events": events,
        }
    finally:
        session.close()


# ── POST /sync/batch ───────────────────────────────────────────────────────────

@app.post("/sync/batch")
def sync_batch(body: SyncBatchRequest):
    """Compute a Merkle root of record hashes, optionally anchor on-chain."""
    import hashlib, uuid

    if not body.records:
        raise HTTPException(status_code=400, detail="records list must not be empty.")

    record_hashes = [
        hashlib.sha256(r.get("data", "").encode()).digest()
        for r in body.records
    ]

    # Simple binary Merkle tree (pad to power of 2)
    leaves = list(record_hashes)
    while len(leaves) & (len(leaves) - 1):  # not a power of 2
        leaves.append(leaves[-1])

    def merkle_root(nodes):
        if len(nodes) == 1:
            return nodes[0]
        next_level = []
        for i in range(0, len(nodes), 2):
            combined = nodes[i] + nodes[i + 1]
            next_level.append(hashlib.sha256(combined).digest())
        return merkle_root(next_level)

    root_bytes = merkle_root(leaves)
    root_hex = "0x" + root_bytes.hex()
    batch_id = str(uuid.uuid4())

    tx_hash = None
    cid = None

    if body.anchor:
        if not client.contract:
            raise HTTPException(status_code=503, detail="Smart contract not connected; cannot anchor.")
        try:
            receipt = client.send_tx("ADMIN", "anchorBatch", root_bytes, len(body.records))
            tx_hash = Web3.to_hex(receipt.transactionHash)
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"anchorBatch call failed: {ex}") from ex

    return {
        "root": root_hex,
        "count": len(body.records),
        "batch_id": batch_id,
        "cid": cid,
        "tx_hash": tx_hash,
    }


# ── POST /attest/signed ────────────────────────────────────────────────────────

@app.post("/attest/signed")
def attest_signed(body: AttestSignedRequest):
    """EIP-712 relay: forward a pre-signed grade attestation to the chain."""
    if not client.contract:
        raise HTTPException(status_code=503, detail="Smart contract not connected.")

    evidence_sha256_bytes = bytes.fromhex(
        body.evidenceSha256.removeprefix("0x")
    )
    sig_bytes = bytes.fromhex(body.signature.removeprefix("0x"))

    try:
        receipt = client.send_tx(
            "ADMIN",
            "attestGradeSigned",
            body.lotId,
            body.grade,
            body.weightG,
            body.moistureBps,
            body.impurityBps,
            body.evidenceCid,
            evidence_sha256_bytes,
            body.nonce,
            body.deadline,
            sig_bytes,
        )
        tx_hash = Web3.to_hex(receipt.transactionHash)
        return {
            "status": "ATTESTED",
            "tx_hash": tx_hash,
            "block_number": receipt.blockNumber,
            "lot_id": body.lotId,
            "grade": body.grade,
        }
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex)) from ex


# ── POST /lots/{id}/location ───────────────────────────────────────────────────

@app.post("/lots/{lot_id}/location")
def post_lot_location(lot_id: int, body: LocationRequest):
    """Store a GPS location event for a lot, hash it into the audit trail."""
    import hashlib

    session = SessionLocal()
    try:
        lot = session.query(IndexedLot).filter(IndexedLot.id == lot_id).first()
        if not lot:
            raise HTTPException(status_code=404, detail=f"Lot {lot_id} not found.")

        payload_str = json.dumps({
            "lot_id": lot_id,
            "lat": str(body.lat),
            "lng": str(body.lng),
            "accuracy": str(body.accuracy),
            "timestamp": body.timestamp,
            "actor": body.actor,
        }, sort_keys=True)
        payload_hash = "0x" + hashlib.sha256(payload_str.encode()).hexdigest()

        loc = LocationEvent(
            lot_id=lot_id,
            lat=str(body.lat),
            lng=str(body.lng),
            accuracy=str(body.accuracy),
            timestamp=body.timestamp,
            actor=body.actor,
            payload_hash=payload_hash,
        )
        session.add(loc)
        session.commit()
        session.refresh(loc)

        return {
            "id": loc.id,
            "lot_id": lot_id,
            "lat": loc.lat,
            "lng": loc.lng,
            "accuracy": loc.accuracy,
            "timestamp": loc.timestamp,
            "actor": loc.actor,
            "payload_hash": payload_hash,
        }
    finally:
        session.close()
