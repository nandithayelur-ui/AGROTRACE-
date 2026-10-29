"""Authenticated QpiAI QCloud experiments for AgroTrace solver evidence."""

from __future__ import annotations

import time
from typing import Any

import config
from qpiai_quantum.algorithms.opt.problems.base import OptimizationProblem
from qpiai_quantum.algorithms.opt.solvers.qaoa import QAOASolver
from qpiai_quantum.authentication.auth import QpiAIQuantumAuth
from qpiai_quantum.state_preparation.bell_state import create_bell_state

from solvers.base import SolverRun
from solvers.qpiai_client import call_qpiai


class QuboProblem(OptimizationProblem):
    """Convert a binary QUBO into the Pauli-Z terms required by SDK QAOA."""

    def __init__(self, qubo: dict[tuple[str, str], float]) -> None:
        super().__init__()
        self.qubo = qubo
        self.variables = sorted({variable for term in qubo for variable in term})
        self.position = {variable: index for index, variable in enumerate(self.variables)}
        self.n_qubits = len(self.variables)

    def _construct_hamiltonian(self) -> list[tuple[list[tuple[int, str]], float]]:
        return self._get_hamiltonian_terms()

    def _get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]:
        terms: list[tuple[list[tuple[int, str]], float]] = []
        for (left, right), coefficient in self.qubo.items():
            left_index, right_index = self.position[left], self.position[right]
            if left == right:
                terms.extend([([], coefficient / 2), ([(left_index, "Z")], -coefficient / 2)])
            else:
                terms.extend([
                    ([], coefficient / 4),
                    ([(left_index, "Z")], -coefficient / 4),
                    ([(right_index, "Z")], -coefficient / 4),
                    ([(left_index, "Z"), (right_index, "Z")], coefficient / 4),
                ])
        return terms

    def decode_solution(self, bitstring: str) -> dict[str, int]:
        bits = bitstring[::-1]
        return {variable: int(bits[index]) for variable, index in self.position.items()}

    def validate_solution(self, solution: dict[str, int]) -> tuple[bool, str]:
        valid = set(solution) == set(self.variables) and all(bit in (0, 1) for bit in solution.values())
        return valid, "Valid QUBO sample" if valid else "Invalid QUBO sample"

    def compute_solution_quality(self, solution: dict[str, int]) -> dict[str, float]:
        energy = sum(coefficient * solution[left] * solution[right] for (left, right), coefficient in self.qubo.items())
        return {"qubo_energy": float(energy)}


def _counts(result: Any) -> dict[str, int]:
    """Normalize SDK result types without relying on a private result class."""
    counts = getattr(result, "counts", None)
    if counts is None and hasattr(result, "get"):
        counts = result.get().get("counts", {})
    return {str(key): int(value) for key, value in (counts or {}).items()}


class QCloudQuantumSolver:
    """Run small, relevant QCloud tasks and preserve raw evidence in SolverRun."""

    @staticmethod
    def run_qaoa(
        qubo_matrix: dict[tuple[str, str], float],
        p_steps: int = 1,
        shots: int = 512,
        seed: int = 42,
    ) -> SolverRun:
        if not qubo_matrix:
            return SolverRun(
                problem_type="QAOA_REDUCED_CLAIM_CONFLICT", n_vars=0,
                solver="QpiAI_QCloud_QAOA", mode="error", seed=seed, params={},
                request_summary={"problem": "claim_conflict_qubo"}, decoded_solution={},
                objective=0.0, feasible=False,
                violations=["A non-empty claim-conflict QUBO is required."],
                runtime_ms=0.0, sdk_versions={"qpiai_quantum": "0.7.5"},
                raw_error={"code": "BAD_INPUT", "message": "QUBO is empty."},
            )

        problem = QuboProblem(qubo_matrix)
        summary = {"problem": "reduced_claim_conflict_qubo", "n_vars": problem.n_qubits, "p_steps": p_steps, "shots": shots}
        started = time.perf_counter()

        def submit_qcloud_qaoa() -> dict[str, Any]:
            QpiAIQuantumAuth.login(config.QPIAI_QCLOUD_API_KEY)
            solver = QAOASolver(
                problem=problem, layers=p_steps, optimizer="COBYLA", max_iterations=20,
                verbose=False, name="AgroTrace claim-conflict QAOA",
            )
            result = solver.run(
                shots=shots, experiment_name="AgroTrace reduced claim-conflict QAOA",
                device_name="QpiAI-QSV-Simulator",
            )
            return {
                "bitstrings": result.counts, "optimal_bitstring": result.bitstring,
                "solution": result.solution, "optimal_energy": result.optimal_energy,
                "valid": result.is_valid, "validation_message": result.validation_message,
                "quality_metrics": result.quality_metrics, "metadata": result.metadata,
            }

        raw_output, raw_error, mode = call_qpiai("qcloud", submit_qcloud_qaoa, summary)
        runtime = (time.perf_counter() - started) * 1000.0
        if mode != "qpiai_real":
            return SolverRun(
                problem_type="QAOA_REDUCED_CLAIM_CONFLICT", n_vars=problem.n_qubits,
                solver="QpiAI_QCloud_QAOA", mode=mode, seed=seed,
                params={"p_steps": p_steps, "shots": shots}, request_summary=summary,
                decoded_solution={}, objective=0.0, feasible=False,
                violations=["No verified QCloud QAOA result was returned."],
                runtime_ms=runtime, sdk_versions={"qpiai_quantum": "0.7.5"},
                raw_error=raw_error,
            )
        return SolverRun(
            problem_type="QAOA_REDUCED_CLAIM_CONFLICT", n_vars=problem.n_qubits,
            solver="QpiAI_QCloud_QAOA", mode="qpiai_real", seed=seed,
            params={"p_steps": p_steps, "shots": shots, "backend": "QpiAI-QSV-Simulator"},
            request_summary=summary, decoded_solution=raw_output["solution"],
            objective=float(raw_output["optimal_energy"]), feasible=bool(raw_output["valid"]),
            violations=[] if raw_output["valid"] else [raw_output["validation_message"]],
            runtime_ms=runtime, sdk_versions={"qpiai_quantum": "0.7.5"},
            raw_output=raw_output,
        )

    @staticmethod
    def run_qrng_bell_experiment(shots: int = 512) -> dict[str, Any]:
        """Run a real QCloud Bell experiment; never synthesize measurement counts."""
        summary = {"experiment": "BellState_QRNG", "shots": shots, "backend": "QpiAI-QSV-Simulator"}
        started = time.perf_counter()

        def submit_bell() -> dict[str, Any]:
            QpiAIQuantumAuth.login(config.QPIAI_QCLOUD_API_KEY)
            bell = create_bell_state("|Ψ+>")
            circuit = bell.build_circuit(measure=True)
            result = circuit.run(
                shots=shots, experiment_name="AgroTrace Bell QRNG evidence",
                device_name="QpiAI-QSV-Simulator",
            )
            return {"counts": _counts(result), "expected_outcomes": bell.get_expected_outcomes()}

        raw_output, raw_error, mode = call_qpiai("qcloud", submit_bell, summary)
        return {
            "experiment": "BellState_QRNG", "mode": mode, "shots": shots,
            "counts": raw_output["counts"] if raw_output else {},
            "expected_outcomes": raw_output["expected_outcomes"] if raw_output else {},
            "runtime_ms": (time.perf_counter() - started) * 1000.0,
            "raw_error": raw_error,
            "status": "COMPLETED" if mode == "qpiai_real" else "NOT_COMPLETED",
        }

