# AgroTrace AI — Architecture

> **Note:** The original hackathon submission report referenced Express/MongoDB.  
> The actual built system uses FastAPI/SQLite as described below.

## Stack

| Layer | Technology | Version | Notes |
|-------|-----------|---------|-------|
| Smart Contracts | Solidity + Hardhat | 0.8.24 / Hardhat 2.x | Chain 31337 (local), optional Sepolia testnet |
| Contract Library | OpenZeppelin | ^5.x | AccessControl, EIP712, ECDSA, MerkleProof |
| Backend API | Python FastAPI | 0.162 | Port 8080; routes at `/` and `/api` |
| ASGI Server | Uvicorn | 0.54 | Bound to 127.0.0.1:8080 |
| Blockchain Client | web3.py | 7.16 | v6-compatible snake_case API |
| Optimization | QpiAI Opt (`qpiai-opt`) | SDK | QUBO/annealing P1/P2/P3 |
| Quantum Circuits | QpiAI QCloud (`qpiai-quantum`) | SDK | QAOA, Bell/QRNG |
| Fallback Solver | PuLP + dwave-neal | 3.3.2 / 0.6 | LP exact + simulated annealing |
| Database | SQLite | (stdlib) | Read-model cache via SQLAlchemy 2.1 |
| IPFS / Storage | Kubo or local-cas | - | Evidence pinning |
| Frontend | React + Vite | 19.3 / 8.3 | Port 5173 |
| i18n | Custom JSON | - | EN, HI, KN, TA |
| Maps | Google Maps JS API | v3 | Lazy-loaded, graceful degradation |
| PWA | Vite PWA plugin | - | Service worker + manifest |

## Web3 Justification

AgroTrace uses blockchain because agricultural supply chains need:

1. **Immutable audit trail** — `auditHead = keccak256(prev, payload)` on every state change
2. **Permissioned roles** — AccessControl (FARMER, GRADER, PROCESSOR, AUDITOR, etc.)
3. **On-chain mass balance** — `Σchildren + loss == parent` enforced in Solidity
4. **Tamper-evidence** — SQLite cache vs on-chain audit head comparison
5. **EIP-712 signed attestations** — inspector signs off-chain; relayer submits; no key exposure

## Data Flow

```
Farmer → registerLot → splitLot → transferLot
  ↓
Grader → attestGrade (or attestGradeSigned via EIP-712)
  ↓
QpiAI Opt (P1 QUBO) → allocation solution → commitAllocation
  ↓
Processor → submitClaim → settle / resolveDispute (P2 MIS/MVC)
```

## Rubric Mapping

| Rubric | Evidence |
|--------|---------|
| A1 — Blockchain Usage | AgroTrace.sol: roles, audit head, lot registry, DAG |
| A2a — QpiAI Opt | P1 allocation, P2 dispute, P3 deduction; real runs in evidence/ |
| A2b — QpiAI QCloud | QAOA + Bell/QRNG; real runs in evidence/ |
| A3 — Product Quality | Role screens, i18n (4 langs), PWA offline, Maps tracking |
