import sys
from datetime import datetime, timezone
from pathlib import Path
import requests

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import config
from chain.client import ChainClient


def run_all_checks() -> dict:
    opt_key = config.QPIAI_OPT_API_KEY
    opt_status = "MISSING"
    opt_hint = "Set QPIAI_OPT_API_KEY in .env"
    if opt_key:
        try:
            from qpiai_opt.opt_solvers import Client
            client = Client(api_key=opt_key)
            if client.health():
                opt_status = "OK"
                opt_hint = "Authenticated with QpiAI Opt platform"
            else:
                opt_status = "NETWORK"
                opt_hint = "Opt server unreachable"
        except Exception as e:
            opt_status = "UNAUTHORIZED"
            opt_hint = str(e)[:60]

    qcloud_key = config.QPIAI_QCLOUD_API_KEY
    qcloud_status = "MISSING"
    qcloud_hint = "Set QPIAI_QCLOUD_API_KEY in .env"
    if qcloud_key:
        try:
            from qpiai_quantum.authentication import QpiAIQuantumAuth
            auth = QpiAIQuantumAuth()
            auth.login(qcloud_key)
            qcloud_status = "OK"
            qcloud_hint = "Authenticated with QpiAI QCloud"
        except Exception as e:
            qcloud_status = "UNAUTHORIZED"
            qcloud_hint = str(e)[:60]

    client = ChainClient()
    chain_ok = client.is_connected()
    chain_status = "OK" if chain_ok else "NETWORK"

    storage_type = "local-cas"
    try:
        r = requests.get(f"{config.IPFS_API}/api/v0/version", timeout=1)
        if r.status_code == 200:
            storage_type = "ipfs"
    except Exception:
        pass

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "services": {
            "qpiai_opt": {"status": opt_status, "ref": config.mask_key(opt_key), "hint": opt_hint},
            "qpiai_qcloud": {"status": qcloud_status, "ref": config.mask_key(qcloud_key), "hint": qcloud_hint},
            "chain": {"status": chain_status, "ref": config.CHAIN_RPC},
            "evidence_storage": {"status": "OK", "storage": storage_type, "ref": storage_type}
        }
    }


if __name__ == "__main__":
    report = run_all_checks()
    print("=" * 80)
    print(f"AGROTRACE AI - SERVICE & KEY HEALTH CHECK ({report['timestamp']})")
    print("=" * 80)
    for svc, details in report["services"].items():
        st = details["status"]
        ref = details.get("ref", "")
        hint = details.get("hint", "")
        print(f"[{st:<10}] {svc:<18} | ref={ref:<18} | {hint}")
    print("=" * 80)
