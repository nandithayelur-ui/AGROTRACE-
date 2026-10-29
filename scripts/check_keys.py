#!/usr/bin/env python3
import importlib.metadata as metadata
import sys
from datetime import datetime, timezone
from pathlib import Path
import requests

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import config


def get_sdk_version(pkg_name: str) -> str:
    try:
        return metadata.version(pkg_name)
    except metadata.PackageNotFoundError:
        return "not_installed"


def check_qpiai_opt() -> dict:
    masked = config.mask_key(config.QPIAI_OPT_API_KEY)
    sdk_ver = get_sdk_version("qpiai-opt")
    if not config.QPIAI_OPT_API_KEY:
        return {
            "service": "qpiai_opt",
            "status": "MISSING",
            "masked_key": masked,
            "sdk_version": sdk_ver,
            "hint": "Set QPIAI_OPT_API_KEY in .env.",
        }
    return {
        "service": "qpiai_opt",
        "status": "OK",
        "masked_key": masked,
        "sdk_version": sdk_ver,
        "hint": "Key present.",
    }


def check_qpiai_qcloud() -> dict:
    masked = config.mask_key(config.QPIAI_QCLOUD_API_KEY)
    sdk_ver = get_sdk_version("qpiai-quantum")
    if not config.QPIAI_QCLOUD_API_KEY:
        return {
            "service": "qpiai_qcloud",
            "status": "MISSING",
            "masked_key": masked,
            "sdk_version": sdk_ver,
            "hint": "Set QPIAI_QCLOUD_API_KEY in .env.",
        }
    return {
        "service": "qpiai_qcloud",
        "status": "OK",
        "masked_key": masked,
        "sdk_version": sdk_ver,
        "hint": "Key present.",
    }


def check_chain_rpc() -> dict:
    try:
        resp = requests.post(
            config.CHAIN_RPC,
            json={"jsonrpc": "2.0", "method": "eth_chainId", "params": [], "id": 1},
            timeout=2,
        )
        if resp.status_code == 200 and "result" in resp.json():
            return {"service": "chain_rpc", "status": "OK", "endpoint": config.CHAIN_RPC, "hint": "Hardhat node reachable."}
    except Exception:
        pass
    return {"service": "chain_rpc", "status": "NETWORK", "endpoint": config.CHAIN_RPC, "hint": "Start node with `npx hardhat node`."}


def check_ipfs() -> dict:
    try:
        resp = requests.post(f"{config.IPFS_API}/api/v0/version", timeout=2)
        if resp.status_code == 200:
            return {"service": "evidence_storage", "status": "OK", "storage": "ipfs", "endpoint": config.IPFS_API}
    except Exception:
        pass
    return {"service": "evidence_storage", "status": "OK", "storage": "local-cas", "endpoint": str(config.LOCAL_CAS_DIR)}


def run_all_checks() -> dict:
    return {
        "last_check_utc": datetime.now(timezone.utc).isoformat(),
        "allow_fallback": config.ALLOW_FALLBACK,
        "services": {
            "qpiai_opt": check_qpiai_opt(),
            "qpiai_qcloud": check_qpiai_qcloud(),
            "chain": check_chain_rpc(),
            "evidence_storage": check_ipfs(),
        },
    }


def main():
    report = run_all_checks()
    print("=" * 80)
    print(f"AGROTRACE AI - SERVICE & KEY HEALTH CHECK ({report['last_check_utc']})")
    print("=" * 80)
    for name, info in report["services"].items():
        status = info.get("status")
        masked = info.get("masked_key", info.get("storage", info.get("endpoint", "")))
        hint = info.get("hint", "")
        print(f"[{status:<10}] {name:<18} | ref={masked:<15} | (Hint: {hint})")
    print("=" * 80)


if __name__ == "__main__":
    main()
