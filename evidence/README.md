# AgroTrace AI — Evidence Pack & Benchmark Results

This directory contains the curated solver runs, benchmark outputs, and cryptographic commitments for the Hackathon WEB3-01 Quant-A-Maze 3.0 project.

## Directory Structure

- `benchmarks/`: Benchmark CSVs comparing solvers across problem sizes (5, 10, 20, 40, 80 lots x 3 seeds).
- `runs/`: Structured run records saved as JSON.
- `packer.py`: Utility to generate self-contained evidence tarball with IPFS/local-cas CID commitments.
- `storage.py`: Content-addressed storage adapter (IPFS Kubo `:5001` or `./local_cas/`).

## Run Schema

Each JSON run record contains:
- `run_id`: UUID
- `timestamp`: ISO-8601 UTC
- `problem_type`: `P1_ALLOCATION`, `P2_DISPUTE`, `P3_DEDUCTION`, `QCLOUD_QAOA`, `QCLOUD_BELL`
- `n_vars`: Number of decision variables
- `solver`: `exact`, `anneal`, `qpiai_opt`, `qpiai_quantum`
- `mode`: `qpiai_real` | `fallback_local` | `error` (Honesty principle: local runs are NEVER labeled qpiai_real)
- `feasible`: Boolean verification from `verify/feasibility.py`
- `objective`: Objective value
- `gap_vs_exact`: Optimality gap compared to exact classical PuLP baseline
- `runtime_ms`: Execution time in milliseconds
- `cid`: Content-addressed storage identifier
- `on_chain_tx`: Blockchain transaction hash when committed
