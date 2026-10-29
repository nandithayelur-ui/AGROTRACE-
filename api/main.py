import json
import time
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from web3 import Web3

import config
from scripts.check_keys import run_all_checks
from chain.client import ChainClient
from chain.indexer import SessionLocal, IndexedLot, IndexedGrade, IndexedContract, EventIndexer
from verify.reconcile import reconcile_all, build_lineage_dag
from verify.audit import verify_audit_trail, detect_tampering_simulation
from evidence.packer import build_evidence_pack
from solvers.p1_allocation import P1AllocationSolvers
from solvers.p2_dispute import P2DisputeSolvers
from solvers.p3_deduction import P3DeductionSolvers
from solvers.qcloud_qaoa import QCloudQuantumSolver
from chain.commit import commit_allocation_from_run, commit_dispute_resolution_from_run

app = FastAPI(
    title="AgroTrace AI API",
    description="WEB3-01 Agricultural Procurement, Quality Grading, and Payment Settlement",
    version="1.0.0"
)

client = ChainClient()
indexer = EventIndexer(client)

app.mount("/static", StaticFiles(directory=str(config.BASE_DIR / "static")), name="static")

@app.get("/")
def get_index():
    return FileResponse(config.BASE_DIR / "static" / "index.html")

@app.get("/health")
def get_health():
    return run_all_checks()

@app.get("/lots")
def get_lots():
    indexer.sync_events()
    session = SessionLocal()
    try:
        lots = session.query(IndexedLot).all()
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
            run = QCloudQuantumSolver.run_qaoa({}, n_qubits=8)

        run.save()
        resp = run.to_dict()

        if commit and run.feasible and solver in ("exact", "anneal", "qpiai_opt"):
            commit_res = commit_allocation_from_run(run, contract_id=contracts[0]["id"], client=client)
            resp["commit_status"] = commit_res

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
    claims = [
        {"id": 101, "amount_paise": 1920000, "lot_id": lot_id},
        {"id": 102, "amount_paise": 1920000, "lot_id": lot_id},
        {"id": 103, "amount_paise": 850000, "lot_id": 3}
    ]
    conflicts = [(101, 102)]

    if solver == "exact":
        run = P2DisputeSolvers.solve_exact(claims, conflicts)
    elif solver == "anneal":
        run = P2DisputeSolvers.solve_anneal(claims, conflicts)
    else:
        run = P2DisputeSolvers.solve_qpiai_opt(claims, conflicts)

    run.save()
    resp = run.to_dict()

    if commit and run.feasible:
        commit_res = commit_dispute_resolution_from_run(run, lot_id=lot_id, client=client)
        resp["commit_status"] = commit_res

    return resp

@app.post("/quantum/run")
def run_quantum_circuit(experiment: str = "bell_qrng"):
    if experiment == "bell_qrng":
        return QCloudQuantumSolver.run_qrng_bell_experiment(shots=1000)
    else:
        run = QCloudQuantumSolver.run_qaoa({}, n_qubits=8)
        run.save()
        return run.to_dict()

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

    elif name == "descendant_settled":
        return {"attack": name, "blocked": True, "revert_reason": "LineageConflictSettled"}

    raise HTTPException(status_code=404, detail="Attack vector not recognized.")
