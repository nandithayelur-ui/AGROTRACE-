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
    # A locally present key is configuration, not evidence of a successful
    # authenticated provider run. Actual solver calls record that separately.
    opt_status = "CONFIGURED" if opt_key else "MISSING"

    qcloud_key = config.QPIAI_QCLOUD_API_KEY
    qcloud_status = "CONFIGURED" if qcloud_key else "MISSING"

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
            "qpiai_opt": {"status": opt_status, "ref": config.mask_key(opt_key)},
            "qpiai_qcloud": {"status": qcloud_status, "ref": config.mask_key(qcloud_key)},
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
        hint = f"(Hint: Set {svc.upper()}_API_KEY in .env.)" if st == "MISSING" else ""
        print(f"[{st:<10}] {svc:<18} | ref={ref:<18} | {hint}")
    print("=" * 80)
