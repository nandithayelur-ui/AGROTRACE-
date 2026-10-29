import json
import time
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import config

class SolverRun:
    def __init__(
        self,
        problem_type: str,
        n_vars: int,
        solver: str,
        mode: str,  # "qpiai_real" | "fallback_local" | "error"
        seed: int,
        params: Dict[str, Any],
        request_summary: Dict[str, Any],
        decoded_solution: Any,
        objective: float,
        feasible: bool,
        violations: List[str],
        runtime_ms: float,
        sdk_versions: Dict[str, str],
        job_id: Optional[str] = None,
        raw_output: Optional[Any] = None,
        raw_error: Optional[Dict[str, Any]] = None,
        optimality_gap_vs_exact: Optional[float] = None
    ):
        # Honesty Guard: Never allow fallback runs to claim qpiai_real mode
        if mode == "qpiai_real" and "fallback" in solver.lower():
            raise ValueError("Honesty violation: Local fallback cannot be labeled 'qpiai_real'")

        self.run_id = f"run_{int(time.time()*1000)}_{problem_type.lower()}"
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.problem_type = problem_type
        self.n_vars = n_vars
        self.solver = solver
        self.mode = mode
        self.sdk_versions = sdk_versions
        self.seed = seed
        self.params = params
        self.job_id = job_id or f"local_{self.run_id}"
        self.input_hash = hashlib.sha256(json.dumps(request_summary, sort_keys=True).encode()).hexdigest()
        self.request_summary = request_summary
        self.raw_output = raw_output
        self.raw_error = raw_error
        self.decoded_solution = decoded_solution
        self.objective = objective
        self.feasible = feasible
        self.violations = violations
        self.optimality_gap_vs_exact = optimality_gap_vs_exact
        self.runtime_ms = runtime_ms

    def to_dict(self) -> Dict[str, Any]:
        return {
            "run_id": self.run_id,
            "timestamp": self.timestamp,
            "problem_type": self.problem_type,
            "n_vars": self.n_vars,
            "solver": self.solver,
            "mode": self.mode,
            "sdk_versions": self.sdk_versions,
            "seed": self.seed,
            "params": self.params,
            "job_id": self.job_id,
            "input_hash": self.input_hash,
            "request_summary": self.request_summary,
            "raw_output": self.raw_output,
            "raw_error": self.raw_error,
            "decoded_solution": self.decoded_solution,
            "objective": self.objective,
            "feasible": self.feasible,
            "violations": self.violations,
            "optimality_gap_vs_exact": self.optimality_gap_vs_exact,
            "runtime_ms": self.runtime_ms
        }

    def save(self) -> Path:
        out_path = config.RUNS_DIR / f"{self.run_id}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)
        return out_path
