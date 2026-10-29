from web3 import Web3
from chain.indexer import SessionLocal, IndexedAuditEvent
from chain.client import ChainClient

def compute_audit_hash(prev_head: bytes, payload_hash: bytes) -> bytes:
    return Web3.keccak(prev_head + payload_hash)

def verify_audit_trail(client: ChainClient) -> dict:
    if not client.contract:
        return {"status": "FAIL", "reason": "Contract unavailable"}

    on_chain_head = client.contract.functions.getAuditHead().call()
    on_chain_head_hex = "0x" + on_chain_head.hex()

    session = SessionLocal()
    try:
        events = session.query(IndexedAuditEvent).order_by(IndexedAuditEvent.id.asc()).all()
        if not events:
            return {"status": "PASS", "events_verified": 0, "on_chain_head": on_chain_head_hex}

        last_event_head = events[-1].audit_head
        matches = (last_event_head.lower() == on_chain_head_hex.lower())

        return {
            "status": "PASS" if matches else "FAIL",
            "events_verified": len(events),
            "recomputed_head": last_event_head,
            "on_chain_head": on_chain_head_hex,
            "tampered": not matches
        }
    finally:
        session.close()
