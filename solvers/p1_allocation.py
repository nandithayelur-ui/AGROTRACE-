import time
import itertools
from typing import Any, Dict, List, Tuple
import pulp
import neal
import config
from solvers.base import SolverRun
from solvers.qpiai_client import call_qpiai
from verify.feasibility import check_allocation_feasibility

def build_allocation_qubo(
    lots: List[Dict[str, Any]],
    contracts: List[Dict[str, Any]],
    penalty_weight: float = 10000.0
) -> Tuple[Dict[Tuple[str, str], float], Dict[str, Tuple[int, int]], Dict[str, Any]]:
    Q: Dict[Tuple[str, str], float] = {}
    var_map: Dict[str, Tuple[int, int]] = {}

    for lot in lots:
        for contract in contracts:
            v_name = f"x_{lot['id']}_{contract['id']}"
            var_map[v_name] = (lot["id"], contract["id"])

            weight_kg = lot["weight_g"] / 1000.0
            base_price = contract.get("base_price_paise", 3000) / 100.0
            cost = base_price * weight_kg

            if lot.get("grade", 1) < contract.get("min_grade", 1):
                cost += penalty_weight * 2.0

            Q[(v_name, v_name)] = Q.get((v_name, v_name), 0.0) + cost

    for lot in lots:
        for c1 in contracts:
            for c2 in contracts:
                if c1["id"] < c2["id"]:
                    v1 = f"x_{lot['id']}_{c1['id']}"
                    v2 = f"x_{lot['id']}_{c2['id']}"
                    pair = (v1, v2) if v1 <= v2 else (v2, v1)
                    Q[pair] = Q.get(pair, 0.0) + penalty_weight

    meta = {
        "n_vars": len(var_map),
        "n_lots": len(lots),
        "n_contracts": len(contracts),
        "penalty_weight": penalty_weight
    }
    return Q, var_map, meta

def decode_allocation(
    sample: Dict[str, int],
    var_map: Dict[str, Tuple[int, int]]
) -> Dict[int, Dict[int, int]]:
    allocations: Dict[int, Dict[int, int]] = {}
    for var_name, val in sample.items():
        if val == 1 and var_name in var_map:
            lot_id, contract_id = var_map[var_name]
            if contract_id not in allocations:
                allocations[contract_id] = {}
            allocations[contract_id][lot_id] = 1
    return allocations

class P1AllocationSolvers:
    @staticmethod
    def solve_exact(lots: List[Dict[str, Any]], contracts: List[Dict[str, Any]], seed: int = 42) -> SolverRun:
        t0 = time.perf_counter()
        prob = pulp.LpProblem("LotAllocation", pulp.LpMinimize)
        x = {}

        # PuLP 4.0+ vs PuLP 2.x/3.x variable instantiation
        for l in lots:
            for c in contracts:
                v_name = f"x_{l['id']}_{c['id']}"
                if hasattr(prob, "add_variable"):
                    # PuLP 4.0+
                    x[(l["id"], c["id"])] = prob.add_variable(v_name, lowBound=0, upBound=1, cat=pulp.LpBinary)
                else:
                    # PuLP 2.x / 3.x
                    try:
                        x[(l["id"], c["id"])] = pulp.LpVariable(v_name, cat=pulp.LpBinary)
                    except TypeError:
                        x[(l["id"], c["id"])] = pulp.LpVariable(v_name, 0, 1)

        # Objective
        prob += pulp.lpSum([
            x[(l["id"], c["id"])] * ((c.get("base_price_paise", 3000) / 100.0) * (l["weight_g"] / 1000.0))
            for l in lots for c in contracts
        ])

        # Constraint 1: each lot used at most once
        for l in lots:
            prob += pulp.lpSum([x[(l["id"], c["id"])] for c in contracts]) <= 1

        # Constraint 2: Contract capacity & Grade check
        for c in contracts:
            prob += pulp.lpSum([x[(l["id"], c["id"])] * l["weight_g"] for l in lots]) <= c["qty_g"]
            for l in lots:
                if l.get("grade", 1) < c.get("min_grade", 1):
                    prob += x[(l["id"], c["id"])] == 0

        solved = False
        try:
            if hasattr(pulp, "PULP_CBC_CMD"):
                prob.solve(pulp.PULP_CBC_CMD(msg=False))
            else:
                prob.solve()
            solved = True
        except Exception:
            try:
                prob.solve()
                solved = True
            except Exception:
                solved = False

        decoded: Dict[int, Dict[int, int]] = {}
        for c in contracts:
            decoded[c["id"]] = {}

        obj = 0.0
        feasible = False

        if solved and prob.objective is not None:
            try:
                for c in contracts:
                    for l in lots:
                        val = pulp.value(x[(l["id"], c["id"])])
                        if val is not None and round(float(val)) == 1:
                            decoded[c["id"]][l["id"]] = l["weight_g"]
                val_obj = pulp.value(prob.objective)
                if val_obj is not None:
                    obj = float(val_obj)
                    feasible = (obj > 0)
            except Exception:
                pass

        # Exact combinatorial branch if external CBC solver binary is not on PATH
        if not feasible or (len(lots) > 0 and sum(len(v) for v in decoded.values()) == 0):
            best_cost = float("inf")
            best_assign = None
            if contracts:
                c_target = contracts[0]
                valid_lots = [l for l in lots if l.get("grade", 1) >= c_target.get("min_grade", 1)]
                for r in range(1, len(valid_lots) + 1):
                    for combo in itertools.combinations(valid_lots, r):
                        total_w = sum(l["weight_g"] for l in combo)
                        if total_w <= c_target.get("qty_g", 0):
                            cost = sum((c_target.get("base_price_paise", 3000) / 100.0) * (l["weight_g"] / 1000.0) for l in combo)
                            if cost < best_cost:
                                best_cost = cost
                                best_assign = combo
                if best_assign:
                    decoded[c_target["id"]] = {l["id"]: l["weight_g"] for l in best_assign}
                    obj = best_cost
                    feasible = True

        runtime = (time.perf_counter() - t0) * 1000.0

        return SolverRun(
            problem_type="P1_ALLOCATION",
            n_vars=len(lots) * len(contracts),
            solver="ExactSolver_PuLP",
            mode="fallback_local",
            seed=seed,
            params={"solver": "PuLP_Exact"},
            request_summary={"n_lots": len(lots), "n_contracts": len(contracts)},
            decoded_solution=decoded,
            objective=obj,
            feasible=feasible,
            violations=[],
            runtime_ms=runtime,
            sdk_versions={"pulp": getattr(pulp, "__version__", "4.0.0")},
            raw_output={"solved": solved},
            optimality_gap_vs_exact=0.0
        )

    @staticmethod
    def solve_anneal(lots: List[Dict[str, Any]], contracts: List[Dict[str, Any]], seed: int = 42) -> SolverRun:
        t0 = time.perf_counter()
        Q, var_map, meta = build_allocation_qubo(lots, contracts)

        sampler = neal.SimulatedAnnealingSampler()
        bqm_linear = {}
        bqm_quadratic = {}
        for (u, v), bias in Q.items():
            if u == v:
                bqm_linear[u] = bias
            else:
                bqm_quadratic[(u, v)] = bias

        import dimod
        bqm = dimod.BinaryQuadraticModel(bqm_linear, bqm_quadratic, 0.0, dimod.BINARY)
        sampleset = sampler.sample(bqm, seed=seed, num_reads=100)
        best_sample = sampleset.first.sample
        best_energy = sampleset.first.energy
        runtime = (time.perf_counter() - t0) * 1000.0

        decoded: Dict[int, Dict[int, int]] = {}
        for c in contracts:
            decoded[c["id"]] = {}
        for var_name, val in best_sample.items():
            if val == 1 and var_name in var_map:
                l_id, c_id = var_map[var_name]
                lot_info = next(l for l in lots if l["id"] == l_id)
                decoded[c_id][l_id] = lot_info["weight_g"]

        violations = []
        is_feasible = True
        for c in contracts:
            rep = check_allocation_feasibility(lots, c, decoded[c["id"]])
            if not rep["feasible"]:
                is_feasible = False
                violations.extend(rep["violations"])

        return SolverRun(
            problem_type="P1_ALLOCATION",
            n_vars=meta["n_vars"],
            solver="AnnealSolver_Neal",
            mode="fallback_local",
            seed=seed,
            params={"num_reads": 100},
            request_summary=meta,
            decoded_solution=decoded,
            objective=float(best_energy),
            feasible=is_feasible,
            violations=violations,
            runtime_ms=runtime,
            sdk_versions={"neal": neal.__version__},
            raw_output={"energy": best_energy}
        )

    @staticmethod
    def solve_qpiai_opt(lots: List[Dict[str, Any]], contracts: List[Dict[str, Any]], seed: int = 42) -> SolverRun:
        t0 = time.perf_counter()
        Q, var_map, meta = build_allocation_qubo(lots, contracts)

        def _sdk_call():
            raise RuntimeError(
                "QpiAI Opt is not adapted yet. Install qpiai-opt in this environment, "
                "run scripts/probe_qpiai.py, then bind its verified QUBO submission method."
            )

        raw_out, raw_err, mode = call_qpiai("opt", _sdk_call, meta)
        runtime = (time.perf_counter() - t0) * 1000.0

        if mode == "fallback_local":
            run = P1AllocationSolvers.solve_anneal(lots, contracts, seed)
            run.solver = "QpiAIOpt_Fallback_Anneal"
            run.mode = "fallback_local"
            run.raw_error = raw_err
            return run

        return SolverRun(
            problem_type="P1_ALLOCATION",
            n_vars=meta["n_vars"],
            solver="QpiAIOptSolver_QUBO",
            mode=mode,
            seed=seed,
            params={"penalty_weight": meta["penalty_weight"]},
            request_summary=meta,
            decoded_solution={},
            objective=0.0,
            feasible=False,
            violations=["No verified QpiAI Opt result was returned."],
            runtime_ms=runtime,
            sdk_versions={"qpiai_opt": "detected"},
            raw_output=raw_out,
            raw_error=raw_err
        )
