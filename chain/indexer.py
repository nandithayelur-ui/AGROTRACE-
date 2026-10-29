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
        """Rebuild the local read model from current on-chain state.

        This demo indexer is intentionally small, so a full replay is safer
        than an incremental cursor: the contract's public getters are the
        source of truth for mutable lot fields. In particular, it prevents a
        browser refresh from adding the same transfer loss repeatedly.
        """
        if not self.contract:
            return 0
        latest_block = self.client.get_latest_block_number()
        if latest_block < from_block:
            return 0

        session = SessionLocal()
        try:
            # Clear only the derived SQLite read model. The chain remains
            # unchanged; this makes an accidental stale cache recoverable.
            session.query(IndexedAuditEvent).delete(synchronize_session=False)
            session.query(IndexedGrade).delete(synchronize_session=False)
            session.query(IndexedContract).delete(synchronize_session=False)
            session.query(IndexedLot).delete(synchronize_session=False)

            event_groups = {
                "LotRegistered": self.contract.events.LotRegistered().get_logs(from_block=from_block, to_block=latest_block),
                "LotTransferred": self.contract.events.LotTransferred().get_logs(from_block=from_block, to_block=latest_block),
                "LotSplit": self.contract.events.LotSplit().get_logs(from_block=from_block, to_block=latest_block),
                "GradeAttested": self.contract.events.GradeAttested().get_logs(from_block=from_block, to_block=latest_block),
                "ContractCreated": self.contract.events.ContractCreated().get_logs(from_block=from_block, to_block=latest_block),
            }
            registration_weights = {
                int(event.args["lotId"]): int(event.args["weightG"])
                for event in event_groups["LotRegistered"]
            }
            parent_ids: dict[int, list[int]] = {}
            for event in event_groups["LotSplit"]:
                for child_id in event.args["childLotIds"]:
                    parent_ids[int(child_id)] = [int(event.args["parentLotId"])]

            statuses = ("CREATED", "IN_TRANSIT", "RECEIVED", "GRADED", "ALLOCATED", "SETTLED", "DISPUTED")
            lot_count = int(self.contract.functions.lotCounter().call())
            for lot_id in range(1, lot_count + 1):
                lot = self.contract.functions.lots(lot_id).call()
                current_weight = int(lot[3])
                session.add(IndexedLot(
                    id=int(lot[0]), owner=str(lot[1]), crop_id=str(lot[2]),
                    weight_g=current_weight,
                    initial_weight_g=registration_weights.get(lot_id, current_weight + int(lot[4])),
                    loss_g=int(lot[4]), loss_reason=int(lot[5]), grade_att_id=int(lot[6]),
                    status=statuses[int(lot[7])], allocated_weight_g=int(lot[8]),
                    parent_ids_json=json.dumps(parent_ids.get(lot_id, [])),
                ))

            for event in event_groups["GradeAttested"]:
                args = event.args
                session.add(IndexedGrade(
                    id=int(args["attestationId"]), lot_id=int(args["lotId"]), grade=int(args["grade"]),
                    evidence_cid=str(args["evidenceCid"]),
                ))

            contract_count = int(self.contract.functions.contractCounter().call())
            for contract_id in range(1, contract_count + 1):
                contract = self.contract.functions.contracts(contract_id).call()
                session.add(IndexedContract(
                    id=int(contract[0]), processor=str(contract[1]), crop_id=str(contract[2]), qty_g=int(contract[3]),
                    min_grade=int(contract[4]), base_price_paise=int(contract[5]),
                    allocated_qty_g=int(contract[8]), active=bool(contract[9]),
                ))

            event_count = 0
            for event_name, events in event_groups.items():
                for event in events:
                    self._record_audit(session, event, event_name, dict(event.args))
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
            payload_json=json.dumps(
                payload,
                sort_keys=True,
                default=lambda value: value.hex() if isinstance(value, bytes) else str(value),
            ),
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
