"""Load the versioned AgroTrace solver datasets shipped with the prototype."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

import config


DATASET_DIR = config.BASE_DIR / "data" / "solver_datasets"


@lru_cache(maxsize=None)
def load_dataset(filename: str) -> Any:
    """Return a JSON dataset and fail with a useful error if it is absent."""
    source = DATASET_DIR / filename
    if not source.is_file():
        raise FileNotFoundError(f"Required dataset is missing: {source}")
    with source.open("r", encoding="utf-8") as dataset_file:
        return json.load(dataset_file)


def claim_conflict_instance() -> tuple[list[dict[str, Any]], list[tuple[str, str]]]:
    """Return claims and incompatible-claim edges for the P2 solver."""
    graph = load_dataset("claim_conflict_graph.json")
    claims = list(graph["claims"])
    conflicts = [(str(edge["a"]), str(edge["b"])) for edge in graph["edges"]]
    return claims, conflicts


def qaoa_qubo() -> dict[tuple[str, str], float]:
    """Build the claim-conflict QUBO in the supplied variable ordering."""
    instance = load_dataset("qaoa_instance.json")
    variables: list[str] = list(instance["variables"])
    qubo: dict[tuple[str, str], float] = {}
    for left_index, right_index, value in instance["Q_linear"]:
        qubo[(variables[left_index], variables[right_index])] = float(value)
    for left_index, right_index, value in instance["Q_quadratic"]:
        qubo[(variables[left_index], variables[right_index])] = float(value)
    return qubo


def dataset_summary() -> dict[str, Any]:
    """Provide safe, display-ready facts about the supplied benchmark data."""
    conflict_graph = load_dataset("claim_conflict_graph.json")
    qaoa = load_dataset("qaoa_instance.json")
    disputes = load_dataset("deduction_partition_disputes.json")
    feasibility = load_dataset("feasibility_test_cases.json")
    fixtures = load_dataset("solver_run_fixtures.json")
    return {
        "source": "User-supplied AgroTrace solver dataset",
        "claims": len(conflict_graph["claims"]),
        "conflicts": len(conflict_graph["edges"]),
        "qaoa_variables": len(qaoa["variables"]),
        "qaoa_edges": len(qaoa["edges"]),
        "dispute_cases": len(disputes),
        "feasibility_cases": len(feasibility),
        "fixture_modes": sorted({str(fixture["mode"]) for fixture in fixtures}),
        "qaoa_shots": int(qaoa["qaoa_config"]["shots"]),
        "qaoa_pass_threshold": float(qaoa["qaoa_config"]["pass_threshold"]),
    }
