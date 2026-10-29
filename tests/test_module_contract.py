"""
Gate 11: Module contract test.
Imports each required name and fails if any is missing.
"""
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


def test_config_exports():
    import config
    assert hasattr(config, "HARDHAT_ACCOUNTS"), "HARDHAT_ACCOUNTS missing from config"
    assert hasattr(config, "ROLE_ACCOUNTS"), "ROLE_ACCOUNTS missing from config"
    assert len(config.HARDHAT_ACCOUNTS) == 10, "Expected 10 Hardhat accounts (0-9)"
    for role in ("ADMIN", "FARMER", "FARMER_2", "COLLECTOR", "WAREHOUSE", "WAREHOUSE_2",
                 "GRADER", "PROCESSOR", "PROCESSOR_2", "AUDITOR"):
        assert role in config.ROLE_ACCOUNTS, f"ROLE_ACCOUNTS missing role: {role}"


def test_audit_exports():
    from verify.audit import verify_audit_trail, detect_tampering_simulation
    assert callable(verify_audit_trail)
    assert callable(detect_tampering_simulation)


def test_check_keys_exports():
    from scripts.check_keys import run_all_checks
    assert callable(run_all_checks)


def test_tx_hash_not_bare_hex():
    """
    Guard: chain/indexer.py must use Web3.to_hex(), never .transactionHash.hex()
    The .hex() method on HexBytes drops the '0x' prefix in some web3.py versions.
    """
    import ast
    indexer_path = ROOT_DIR / "chain" / "indexer.py"
    source = indexer_path.read_text(encoding="utf-8")
    assert ".transactionHash.hex()" not in source, (
        "chain/indexer.py still uses .transactionHash.hex() — must use Web3.to_hex()"
    )


def test_no_fromBlock_camelCase():
    """Guard: web3.py v6 requires snake_case from_block= / to_block=."""
    import re
    chain_dir = ROOT_DIR / "chain"
    for py_file in chain_dir.glob("*.py"):
        source = py_file.read_text(encoding="utf-8")
        assert not re.search(r'fromBlock|toBlock', source), (
            f"{py_file.name} uses camelCase fromBlock/toBlock — must use from_block/to_block"
        )


def test_no_query_enum_kwarg():
    """Guard: FastAPI Query(enum=[...]) crashes Uvicorn on startup."""
    api_dir = ROOT_DIR / "api"
    for py_file in api_dir.glob("*.py"):
        source = py_file.read_text(encoding="utf-8")
        assert "Query(" not in source or "enum=[" not in source, (
            f"{py_file.name} uses Query(enum=[...]) — use typed params or Literal instead"
        )


def test_scripts_have_sys_path_guard():
    """Guard: every scripts/*.py must prepend ROOT_DIR to sys.path."""
    scripts_dir = ROOT_DIR / "scripts"
    for py_file in scripts_dir.glob("*.py"):
        source = py_file.read_text(encoding="utf-8")
        # Allow files that don't import local packages
        if "import config" in source or "from solvers" in source or "from chain" in source or "from verify" in source:
            assert "sys.path.insert" in source, (
                f"{py_file.name} imports local packages but has no sys.path.insert guard"
            )
