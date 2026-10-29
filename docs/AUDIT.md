# AgroTrace AI — Audit Report

**Date:** 2026-10-30  
**Auditor:** Autonomous Agent (AgroTrace AI Build System)  
**Project:** WEB3-01, Quant-A-Maze 3.0, Web3 Track

---

## What Works (Baseline)

| Component | Status | Notes |
|-----------|--------|-------|
| Python venv (3.14.7) | ✅ | All core packages installed |
| FastAPI 0.162 + Uvicorn | ✅ | Binds to port 8080 |
| web3.py 7.16 | ✅ | Connects to Hardhat chain |
| SQLAlchemy 2.1 + SQLite | ✅ | Read model caching |
| PuLP 3.3.2 | ✅ | LP solver with dual-API guard |
| NetworkX 3.6 | ✅ | Lineage DAG traversal |
| `config.py` | ✅ | HARDHAT_ACCOUNTS (0-9), ROLE_ACCOUNTS, mask_key |
| `verify/audit.py` | ✅ | verify_audit_trail, detect_tampering_simulation |
| `scripts/check_keys.py` | ✅ | run_all_checks() |
| `solvers/p1_allocation.py` | ✅ | PuLP 4.x + 2.x/3.x guard |
| `frontend/src/api.js` | ✅ | No markdown link bug; uses `/api` prefix |
| `vite.config.js` | ✅ | Proxy to 8080 |
| 46 Python tests | ✅ | Passing (3 skipped by env flag) |

## Bugs Found and Fixed

| # | Bug | Location | Fix Applied |
|---|-----|----------|-------------|
| 1 | `.transactionHash.hex()` — drops `0x` prefix | `chain/indexer.py:153` | Changed to `Web3.to_hex()` |
| 2 | Hardhat localhost port was 8546 | `hardhat.config.js` | Changed to 8545 |
| 3 | `.gitignore` incomplete | `.gitignore` | Added all spec-required entries |
| 4 | `test_module_contract.py` missing | `tests/` | Created with all guardrail checks |
| 5 | EIP-712 `attestGradeSigned` missing | `contracts/AgroTrace.sol` | Added with ECDSA + EIP712 |
| 6 | Merkle `anchorBatch`/`verifyRecord` missing | `contracts/AgroTrace.sol` | Added with MerkleProof |
| 7 | Testnet config missing | `hardhat.config.js` | Added optional testnet via env |

## What Was Added

- `tests/test_module_contract.py` — guardrail contract tests
- `start_all.bat` — one-click startup
- `stop_all.bat` — shutdown
- `make_source_zip.bat` — source archive
- `docs/AUDIT.md` — this file
- `docs/ARCHITECTURE.md` — stack documentation
- `docs/VERIFICATION.md` — gate tracking

## Architecture Note

The submitted hackathon report referenced Express/MongoDB. The **built system** uses:
- **Backend:** Python FastAPI (not Express) on port 8080
- **Database:** SQLite (not MongoDB), used as a read-model cache
- **Blockchain:** Solidity 0.8.24 on Hardhat (chain 31337)
- **Quantum:** QpiAI Opt + QCloud SDKs

This mismatch is documented in `docs/ARCHITECTURE.md`.
