import json
from pathlib import Path
from typing import Any, Dict, Optional
from web3 import Web3
from web3.contract import Contract
import config

ARTIFACT_PATH = Path(config.BASE_DIR) / "artifacts" / "contracts" / "AgroTrace.sol" / "AgroTrace.json"

class ChainClient:
    def __init__(self, rpc_url: Optional[str] = None, contract_address: Optional[str] = None):
        self.rpc_url = rpc_url or config.CHAIN_RPC
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        self.contract_address = contract_address or config.CONTRACT_ADDRESS
        self.abi = self._load_abi()
        self.contract: Optional[Contract] = None
        if self.contract_address and self.w3.is_address(self.contract_address):
            self.contract = self.w3.eth.contract(
                address=Web3.to_checksum_address(self.contract_address),
                abi=self.abi
            )

    def _load_abi(self) -> list:
        if not ARTIFACT_PATH.exists():
            return []
        with open(ARTIFACT_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("abi", [])

    def is_connected(self) -> bool:
        return self.w3.is_connected()

    def get_latest_block_number(self) -> int:
        return self.w3.eth.block_number

    def send_tx(self, role_name: str, fn_name: str, *args) -> Dict[str, Any]:
        if not self.contract:
            raise RuntimeError("Contract address not configured or invalid.")
        account_info = config.ROLE_ACCOUNTS.get(role_name, config.ROLE_ACCOUNTS["ADMIN"])
        sender_address = Web3.to_checksum_address(account_info["address"])
        private_key = account_info["private_key"]

        nonce = self.w3.eth.get_transaction_count(sender_address)
        fn = getattr(self.contract.functions, fn_name)(*args)
        tx = fn.build_transaction({
            "from": sender_address,
            "nonce": nonce,
            "gas": 3_000_000,
            "gasPrice": self.w3.eth.gas_price,
            "chainId": self.w3.eth.chain_id,
        })
        signed = self.w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed.raw_transaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt
