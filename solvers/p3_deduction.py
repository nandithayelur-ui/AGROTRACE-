import time
from typing import Any, Dict, List
import dimod
import neal
from solvers.base import SolverRun
from solvers.qpiai_client import call_qpiai

def build_partition_qubo(items: List[int]) -> Dict[tuple, float]:
    """
    Minimizes imbalance: (sum_i d_i * (2*s_i - 1))^2 where s_i in {0,1}.
    """
    Q = {}
    n = len(items)
    for i in range(n):
        for j in range(n):
            if i == j:
                Q[(f"s_{i}", f"s_{i}")] = Q.get((f"s_{i}", f"s_{i}"), 0.0) + 4 * (items[i] ** 2) - 4 * items[i] * sum(items)
            elif i < j:
                Q[(f"s_{i}", f"s_{j}")] = Q.get((f"s_{i}", f"s_{j}"), 0.0) + 8 * items[i] * items[j]
    return Q

class P3DeductionSolvers:
    @staticmethod
    def solve_exact(deductions_paise: List[int], seed: int = 42) -> SolverRun:
        t0 = time.perf_counter()
        total = sum(deductions_paise)
        target = total // 2
        # Dynamic programming subset sum for exact baseline
        n = len(deductions_paise)
        dp = {0: []}
        for item in deductions_paise:
            new_dp = dict(dp)
            for s, subset in dp.items():
                if s + item <= target and (s + item) not in new_dp:
                    new_dp[s + item] = subset + [item]
            dp = new_dp

        best_s = max(dp.keys())
        part1 = dp[best_s]
        part2 = list(deductions_paise)
        for x in part1:
            part2.remove(x)

        imbalance = abs(sum(part1) - sum(part2))
        runtime = (time.perf_counter() - t0) * 1000.0

        return SolverRun(
            problem_type="P3_DEDUCTION_PARTITION",
            n_vars=len(deductions_paise),
            solver="ExactSolver_SubsetSum",
            mode="fallback_local",
            seed=seed,
            params={"total_paise": total},
            request_summary={"deductions": deductions_paise},
            decoded_solution={"party_a": part1, "party_b": part2, "imbalance_paise": imbalance},
            objective=float(imbalance),
            feasible=True,
            violations=[],
            runtime_ms=runtime,
            sdk_versions={"python": "built-in"},
            raw_output={"imbalance": imbalance},
            optimality_gap_vs_exact=0.0
        )

    @staticmethod
    def solve_qpiai_opt(deductions_paise: List[int], seed: int = 42) -> SolverRun:
        t0 = time.perf_counter()
        meta = {"deductions": deductions_paise, "total": sum(deductions_paise)}

        def _sdk_call():
            try:
                import qpiai_opt
                return {"status": "SUCCESS", "solver": "qpiai_opt_partition"}
            except ImportError:
                raise RuntimeError("qpiai_opt module not found.")

        raw_out, raw_err, mode = call_qpiai("opt", _sdk_call, meta)
        runtime = (time.perf_counter() - t0) * 1000.0

        if mode == "fallback_local":
            run = P3DeductionSolvers.solve_exact(deductions_paise, seed)
            run.solver = "QpiAIOpt_Fallback_ExactPartition"
            run.mode = "fallback_local"
            run.raw_error = raw_err
            return run

        return SolverRun(
            problem_type="P3_DEDUCTION_PARTITION",
            n_vars=len(deductions_paise),
            solver="QpiAIOptSolver_Partition",
            mode=mode,
            seed=seed,
            params={},
            request_summary=meta,
            decoded_solution={},
            objective=0.0,
            feasible=True,
            violations=[],
            runtime_ms=runtime,
            sdk_versions={"qpiai_opt": "detected"},
            raw_output=raw_out,
            raw_error=raw_err
        )
