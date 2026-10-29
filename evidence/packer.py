import json
from datetime import datetime, timezone
from typing import Any, Dict
from chain.client import ChainClient
from chain.indexer import SessionLocal, IndexedLot, IndexedGrade
from verify.audit import verify_audit_trail
from evidence.storage import pin_json

def build_evidence_pack(lot_id: int, client: ChainClient = None) -> Dict[str, Any]:
    """
    Constructs a comprehensive tamper-evident bundle for dispute resolution or verification:
    1. Lot identity, current weight, and status
    2. Full DAG ancestry & descendants
    3. Attested quality grading and evidence certificates
    4. On-chain audit trail verification
    5. Content-addressed storage receipt
    """
    if client is None:
        client = ChainClient()

    session = SessionLocal()
    try:
        lot = session.query(IndexedLot).filter_by(id=lot_id).first()
        if not lot:
            raise ValueError(f"Lot {lot_id} does not exist in registry.")

        parents = json.loads(lot.parent_ids_json or "[]")

        # Fetch quality attestation
        grade_record = None
        if lot.grade_att_id > 0:
            grade = session.query(IndexedGrade).filter_by(id=lot.grade_att_id).first()
            if grade:
                grade_record = {
                    "attestation_id": grade.id,
                    "grade": grade.grade,
                    "moisture_bps": grade.moisture_bps,
                    "impurity_bps": grade.impurity_bps,
                    "evidence_cid": grade.evidence_cid,
                    "grader": grade.grader
                }

        # Query on-chain lineage
        on_chain_ancestors, on_chain_descendants = [], []
        if client.contract:
            try:
                lineage = client.contract.functions.getLineage(lot_id).call()
                on_chain_ancestors = list(lineage[0])
                on_chain_descendants = list(lineage[1])
            except Exception:
                pass

        audit_status = verify_audit_trail(client)

        pack_payload = {
            "version": "1.0.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "lot": {
                "id": lot.id,
                "owner": lot.owner,
                "crop_id": lot.crop_id,
                "weight_g": lot.weight_g,
                "initial_weight_g": lot.initial_weight_g,
                "loss_g": lot.loss_g,
                "loss_reason": lot.loss_reason,
                "status": lot.status,
                "allocated_weight_g": lot.allocated_weight_g
            },
            "lineage": {
                "parent_ids": parents,
                "on_chain_ancestors": on_chain_ancestors,
                "on_chain_descendants": on_chain_descendants
            },
            "quality_grade": grade_record,
            "audit_trail_verification": audit_status
        }

        cid, sha256_hex, storage_mode = pin_json(pack_payload)
        pack_payload["evidence_cid"] = cid
        pack_payload["evidence_sha256"] = sha256_hex
        pack_payload["storage"] = storage_mode

        return pack_payload
    finally:
        session.close()
