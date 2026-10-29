import json
from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from web3 import Web3
import config
from chain.client import ChainClient

Base = declarative_base()

class IndexedLot(Base):
    __tablename__ = "lots"
    id = Column(Integer, primary_key=True)
    owner = Column(String(42), nullable=False)
    crop_id = Column(String(64), nullable=False)
    weight_g = Column(BigInteger, nullable=False)
    initial_weight_g = Column(BigInteger, nullable=False)
    loss_g = Column(BigInteger, default=0)
    loss_reason = Column(Integer, default=0)
    grade_att_id = Column(Integer, default=0)
    status = Column(String(32), default="CREATED")
    allocated_weight_g = Column(BigInteger, default=0)
    parent_ids_json = Column(Text, default="[]")

class IndexedGrade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    lot_id = Column(Integer, nullable=False)
    grade = Column(Integer, nullable=False)
    moisture_bps = Column(Integer, default=0)
    impurity_bps = Column(Integer, default=0)
    evidence_cid = Column(String(128))
    evidence_sha256 = Column(String(66))
    grader = Column(String(42))

class IndexedContract(Base):
    __tablename__ = "procurement_contracts"
    id = Column(Integer, primary_key=True)
    processor = Column(String(42))
    crop_id = Column(String(64))
    qty_g = Column(BigInteger)
    min_grade = Column(Integer)
    base_price_paise = Column(BigInteger)
    allocated_qty_g = Column(BigInteger, default=0)
    active = Column(Boolean, default=True)

class IndexedAuditEvent(Base):
    __tablename__ = "audit_events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    block_number = Column(Integer, nullable=False)
    tx_hash = Column(String(66), nullable=False)
    event_name = Column(String(64), nullable=False)
    payload_json = Column(Text, nullable=False)
    audit_head = Column(String(66), nullable=False)

engine = create_engine(f"sqlite:///{config.DB_PATH}", echo=False)
SessionLocal = sessionmaker(bind=engine)

class EventIndexer:
    def __init__(self, client: ChainClient):
        self.client = client
        self.contract = client.contract
        Base.metadata.create_all(bind=engine)

    def sync_events(self, from_block: int = 0) -> int:
        if not self.contract:
            return 0
        latest_block = self.client.get_latest_block_number()
        if latest_block < from_block:
            return 0

        session = SessionLocal()
        event_count = 0
        try:
            events = self.contract.events.LotRegistered().get_logs(fromBlock=from_block, toBlock=latest_block)
            for e in events:
                args = e.args
                lot_id = args["lotId"]
                existing = session.query(IndexedLot).filter_by(id=lot_id).first()
                if not existing:
                    session.add(IndexedLot(
                        id=lot_id,
                        owner=args["owner"],
                        crop_id=args["cropId"],
                        weight_g=args["weightG"],
                        initial_weight_g=args["weightG"],
                        parent_ids_json="[]"
                    ))
                self._record_audit(session, e, "LotRegistered", {
                    "lotId": lot_id, "owner": args["owner"], "weightG": args["weightG"]
                })
                event_count += 1

            events = self.contract.events.LotTransferred().get_logs(fromBlock=from_block, toBlock=latest_block)
            for e in events:
                args = e.args
                lot = session.query(IndexedLot).filter_by(id=args["lotId"]).first()
                if lot:
                    lot.owner = args["to"]
                    lot.weight_g = args["receivedWeightG"]
                    lot.loss_g += args["lossG"]
                    lot.loss_reason = args["reason"]
                    lot.status = "RECEIVED"
                self._record_audit(session, e, "LotTransferred", {
                    "lotId": args["lotId"], "from": args["from"], "to": args["to"],
                    "receivedWeightG": args["receivedWeightG"], "lossG": args["lossG"]
                })
                event_count += 1

            events = self.contract.events.LotSplit().get_logs(fromBlock=from_block, toBlock=latest_block)
            for e in events:
                args = e.args
                parent_id = args["parentLotId"]
                parent = session.query(IndexedLot).filter_by(id=parent_id).first()
                if parent:
                    parent.status = "ALLOCATED"
                    parent.weight_g = 0
                for c_id in args["childLotIds"]:
                    child = session.query(IndexedLot).filter_by(id=c_id).first()
                    if not child and parent:
                        session.add(IndexedLot(
                            id=c_id,
                            owner=parent.owner,
                            crop_id=parent.crop_id,
                            weight_g=0,
                            initial_weight_g=0,
                            parent_ids_json=json.dumps([parent_id]),
                            grade_att_id=parent.grade_att_id,
                            status="GRADED" if parent.grade_att_id else "CREATED"
                        ))
                self._record_audit(session, e, "LotSplit", {
                    "parentLotId": parent_id, "childLotIds": list(args["childLotIds"]), "lossG": args["lossG"]
                })
                event_count += 1

            events = self.contract.events.GradeAttested().get_logs(fromBlock=from_block, toBlock=latest_block)
            for e in events:
                args = e.args
                att_id = args["attestationId"]
                lot_id = args["lotId"]
                existing = session.query(IndexedGrade).filter_by(id=att_id).first()
                if not existing:
                    session.add(IndexedGrade(
                        id=att_id,
                        lot_id=lot_id,
                        grade=args["grade"],
                        evidence_cid=args["evidenceCid"]
                    ))
                lot = session.query(IndexedLot).filter_by(id=lot_id).first()
                if lot:
                    lot.grade_att_id = att_id
                    lot.status = "GRADED"
                self._record_audit(session, e, "GradeAttested", {
                    "attestationId": att_id, "lotId": lot_id, "grade": args["grade"]
                })
                event_count += 1

            events = self.contract.events.ContractCreated().get_logs(fromBlock=from_block, toBlock=latest_block)
            for e in events:
                args = e.args
                c_id = args["contractId"]
                if not session.query(IndexedContract).filter_by(id=c_id).first():
                    session.add(IndexedContract(
                        id=c_id,
                        processor=args["processor"],
                        crop_id=args["cropId"],
                        qty_g=args["qtyG"]
                    ))
                self._record_audit(session, e, "ContractCreated", {
                    "contractId": c_id, "cropId": args["cropId"], "qtyG": args["qtyG"]
                })
                event_count += 1

            session.commit()
            return event_count
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def _record_audit(self, session, event_obj, name: str, payload: dict):
        head_val = event_obj.args.get("newAuditHead", b"")
        head_hex = "0x" + head_val.hex() if isinstance(head_val, bytes) else str(head_val)
        session.add(IndexedAuditEvent(
            block_number=event_obj.blockNumber,
            tx_hash=event_obj.transactionHash.hex(),
            event_name=name,
            payload_json=json.dumps(payload, sort_keys=True),
            audit_head=head_hex
        ))

if __name__ == "__main__":
    client = ChainClient()
    if client.is_connected() and client.contract:
        indexer = EventIndexer(client)
        synced = indexer.sync_events()
        print(f"Indexed {synced} events into SQLite database: {config.DB_PATH}")
    else:
        print("Chain node or contract not available; verify Hardhat node and CONTRACT_ADDRESS in .env.")
