import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def mask_key(key: str | None) -> str:
    if not key or not key.strip():
        return "MISSING"
    k = key.strip()
    if len(k) <= 8:
        return f"{k[:2]}…{k[-2:]}" if len(k) >= 4 else "****"
    return f"{k[:4]}…{k[-4:]}"


QPIAI_OPT_API_KEY: str = os.getenv("93160d1859c91fc290b7cc178bd4ad30bd7c9db910843cc84db7f85387d9e3c3", "").strip()
QPIAI_QCLOUD_API_KEY: str = os.getenv("b3ea05f644aaa6f5396c507ac1c9718d4ac4d352a2a69fd5aba99b28f623dbc6", "").strip()
QPIAI_OPT_URL: str = os.getenv("QPIAI_OPT_URL", "").strip()
QPIAI_QCLOUD_URL: str = os.getenv("QPIAI_QCLOUD_URL", "").strip()

ALLOW_FALLBACK: bool = os.getenv("ALLOW_FALLBACK", "false").strip().lower() == "true"
IPFS_API: str = os.getenv("IPFS_API", "http://127.0.0.1:5001").strip().rstrip("/")
CHAIN_RPC: str = os.getenv("CHAIN_RPC", "http://127.0.0.1:8545").strip()
CONTRACT_ADDRESS: str = os.getenv("CONTRACT_ADDRESS", "").strip()

DB_PATH = BASE_DIR / "agrotrace_cache.db"
RUNS_DIR = BASE_DIR / "runs"
BENCHMARKS_DIR = BASE_DIR / "benchmarks"
LOCAL_CAS_DIR = BASE_DIR / "local_cas"

for d in (RUNS_DIR, BENCHMARKS_DIR, LOCAL_CAS_DIR):
    d.mkdir(parents=True, exist_ok=True)