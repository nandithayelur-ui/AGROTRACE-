#!/usr/bin/env python3
import csv
import sys
import time
from pathlib import Path

# Add project root to sys.path so solvers/ and config can be imported directly
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import config
from solvers.p1_allocation import P1AllocationSolvers

def generate_benchmark_data(n_lots: int, n_contracts: int):
    lots = [
        {"id": i, "weight_g": 500000 + ((i * 17000) % 500000), "allocated_weight_g": 0, "grade": 2 + (i % 2)}
        for i in range(1, n_lots + 1)
    ]
    contracts = [
        {"id": j, "qty_g": (n_lots * 600000) // n_contracts, "min_grade": 2, "base_price_paise": 3000 + j*100}
        for j in range(1, n_contracts + 1)
    ]
    return lots, contracts

def run_benchmarks():
    out_file = config.BENCHMARKS_DIR / "results.csv"
    fieldnames = [
        "instance_lots", "instance_contracts", "solver", "mode", "n_vars",
        "objective", "gap_vs_exact_pct", "feasible", "runtime_ms"
    ]

    print("=" * 80)
    print("AGROTRACE AI - SYSTEM BENCHMARK (P1 ALLOCATION)")
    print(f"Writing results to: {out_file}")
    print("=" * 80)

    rows = []
    lot_sizes = [5, 10, 20]
    contracts_count = 3

    for n_l in lot_sizes:
        print(f"\nEvaluating Instance: {n_l} Lots x {contracts_count} Contracts...")
        lots, contracts = generate_benchmark_data(n_l, contracts_count)

        run_exact = P1AllocationSolvers.solve_exact(lots, contracts)
        exact_obj = run_exact.objective
        rows.append({
            "instance_lots": n_l,
            "instance_contracts": contracts_count,
            "solver": run_exact.solver,
            "mode": run_exact.mode,
            "n_vars": run_exact.n_vars,
            "objective": f"{run_exact.objective:.2f}",
            "gap_vs_exact_pct": "0.00%",
            "feasible": run_exact.feasible,
            "runtime_ms": f"{run_exact.runtime_ms:.2f}"
        })

        run_anneal = P1AllocationSolvers.solve_anneal(lots, contracts)
        gap = ((run_anneal.objective - exact_obj) / exact_obj * 100.0) if exact_obj > 0 else 0.0
        rows.append({
            "instance_lots": n_l,
            "instance_contracts": contracts_count,
            "solver": run_anneal.solver,
            "mode": run_anneal.mode,
            "n_vars": run_anneal.n_vars,
            "objective": f"{run_anneal.objective:.2f}",
            "gap_vs_exact_pct": f"{max(0.0, gap):.2f}%",
            "feasible": run_anneal.feasible,
            "runtime_ms": f"{run_anneal.runtime_ms:.2f}"
        })

        print(f"  Exact : Obj={run_exact.objective:.2f} in {run_exact.runtime_ms:.2f}ms")
        print(f"  Anneal: Obj={run_anneal.objective:.2f} in {run_anneal.runtime_ms:.2f}ms (Gap: {max(0.0, gap):.2f}%)")

    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("\nBenchmark completed successfully.")

if __name__ == "__main__":
    run_benchmarks()
