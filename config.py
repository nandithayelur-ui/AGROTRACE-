import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
# Local demo services are frequently restarted on a fresh port. The project
# file must be authoritative instead of inheriting a stale parent-process URL.
load_dotenv(BASE_DIR / ".env", override=True)


def mask_key(key: str | None) -> str:
    if not key or not key.strip():
        return "MISSING"
    k = key.strip()
    if len(k) <= 8:
        return f"{k[:2]}…{k[-2:]}" if len(k) >= 4 else "****"
    return f"{k[:4]}…{k[-4:]}"


QPIAI_OPT_API_KEY: str = os.getenv("QPIAI_OPT_API_KEY", "").strip()
QPIAI_QCLOUD_API_KEY: str = os.getenv("QPIAI_QCLOUD_API_KEY", "").strip()
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

# Standard deterministic Hardhat local node accounts (0-9) mapped to demo roles
HARDHAT_ACCOUNTS = [
    {
        "index": 0,
        "role": "ADMIN",
        "name": "Platform Admin",
        "address": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
        "private_key": "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80",
    },
    {
        "index": 1,
        "role": "FARMER",
        "name": "Ravi of Mandya",
        "address": "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
        "private_key": "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d",
    },
    {
        "index": 2,
        "role": "FARMER",
        "name": "Meena",
        "address": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC",
        "private_key": "0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a",
    },
    {
        "index": 3,
        "role": "COLLECTOR",
        "name": "Suresh",
        "address": "0x90F79bf6EB2c4f870365E785982E1f101E93b906",
        "private_key": "0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6",
    },
    {
        "index": 4,
        "role": "WAREHOUSE",
        "name": "Mandya Central Warehouse",
        "address": "0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65",
        "private_key": "0x47e179ec197488593b187f80a00eb0da91f1b9d0b13f8733639f19c30a34926a",
    },
    {
        "index": 5,
        "role": "WAREHOUSE",
        "name": "Mysuru Grain Depot",
        "address": "0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc",
        "private_key": "0x8b3a350cf5c34c9194ca85829a2df0ec3153be0318b5e2d3348e872092edffba",
    },
    {
        "index": 6,
        "role": "GRADER",
        "name": "Agmark Grader Kavitha",
        "address": "0x976EA74026E726554dB657fA54763abd0C3a0aa9",
        "private_key": "0x92db14e403b83dfe3df233f83dfa3a0d7096f21ca9b0d6d6b8d88b2b4ec1564e",
    },
    {
        "index": 7,
        "role": "PROCESSOR",
        "name": "Annapurna Mills",
        "address": "0x14dC79964da2C08b23698B3D3cc7Ca32193d9955",
        "private_key": "0x4bbbf85ce3377467afe5d46f804f221813b2bb87f24d81f60f1fcdbf7cbf4356",
    },
    {
        "index": 8,
        "role": "PROCESSOR",
        "name": "Kaveri Foods",
        "address": "0x23618e81E3f5cdF7f54C3d65f7FBc0aBf5B21E8f",
        "private_key": "0xdbda1821b80551c9d65939329250298aa3472ba22feea921c0cf5d620ea67b97",
    },
    {
        "index": 9,
        "role": "AUDITOR",
        "name": "FCI Quality Auditor",
        "address": "0xa0Ee7A142d267C1f36714E4a8F75612F20a79720",
        "private_key": "0x2a871d0798f97d79848a013d4936a73bf4cc922c825d33c1cf7073dff6d409c6",
    },
]

ROLE_ACCOUNTS = {
    "ADMIN": HARDHAT_ACCOUNTS[0],
    "FARMER": HARDHAT_ACCOUNTS[1],
    "FARMER_2": HARDHAT_ACCOUNTS[2],
    "COLLECTOR": HARDHAT_ACCOUNTS[3],
    "WAREHOUSE": HARDHAT_ACCOUNTS[4],
    "WAREHOUSE_2": HARDHAT_ACCOUNTS[5],
    "GRADER": HARDHAT_ACCOUNTS[6],
    "PROCESSOR": HARDHAT_ACCOUNTS[7],
    "PROCESSOR_2": HARDHAT_ACCOUNTS[8],
    "AUDITOR": HARDHAT_ACCOUNTS[9],
}
