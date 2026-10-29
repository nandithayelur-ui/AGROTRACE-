import json
import hashlib
from pathlib import Path
from typing import Any, Dict, Tuple
import requests
import config

def compute_sha256(data_bytes: bytes) -> str:
    return hashlib.sha256(data_bytes).hexdigest()

def pin_json(data: Dict[str, Any]) -> Tuple[str, str, str]:
    """
    Pins a JSON document to IPFS or the local Content-Addressed Store.
    Returns: (cid, sha256_hex, storage_mode)
    storage_mode is strictly: "ipfs" | "local-cas"
    """
    serialized = json.dumps(data, sort_keys=True, indent=2).encode("utf-8")
    sha256_hex = compute_sha256(serialized)

    # 1. Try IPFS daemon if reachable
    try:
        files = {"file": ("data.json", serialized, "application/json")}
        resp = requests.post(f"{config.IPFS_API}/api/v0/add", files=files, timeout=3)
        if resp.status_code == 200:
            cid = resp.json().get("Hash")
            if cid:
                return cid, sha256_hex, "ipfs"
    except Exception:
        pass

    # 2. Honest Fallback: Save to ./local_cas/
    cid = f"bafy_cas_{sha256_hex[:32]}"
    out_file = config.LOCAL_CAS_DIR / f"{cid}.json"
    with open(out_file, "wb") as f:
        f.write(serialized)

    return cid, sha256_hex, "local-cas"

def fetch_json(cid: str) -> Dict[str, Any]:
    """Retrieves a JSON document by CID from IPFS or local-cas."""
    if cid.startswith("bafy_cas_"):
        file_path = config.LOCAL_CAS_DIR / f"{cid}.json"
        if not file_path.exists():
            raise FileNotFoundError(f"CID {cid} not found in local CAS storage.")
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Try IPFS
    try:
        resp = requests.post(f"{config.IPFS_API}/api/v0/cat?arg={cid}", timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass

    # Check local store as backup
    file_path = config.LOCAL_CAS_DIR / f"{cid}.json"
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    raise FileNotFoundError(f"CID {cid} could not be resolved.")
