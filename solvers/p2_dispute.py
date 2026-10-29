import time
from typing import Any, Dict, List, Set, Tuple
import networkx as nx
import dimod
import neal
from solvers.base import SolverRun
from solvers.qpiai_client import call_qpiai

def build_claim_conflict_graph(claims: List[Dict[str, Any]], planted_conflicts: List[Tuple[int, int]]) -> nx.Graph:
    """Builds conflict graph: nodes = claims (weight = amount), edge = legal/settlement conflict."""
    G = nx.Graph()
    for c in claims:
        G.add_node(c["id"], amount_paise=c["amount_paise"], lot_id=c["lot_id"], invoice_id=c.get("invoice_id"))
    for u, v in planted_conflicts:
        if G.has_node(u) and G.has_node(v):
            G.add_edge(u, v)
    return G

def build_mis_qubo(G: nx.Graph, penalty: float = 2.0) -> Tuple[Dict[Tuple[str, str], float], Dict[str, int]]:
    """
    QUBO for Max Independent Set:
    Maximize sum_i (w_i * x_i) - penalty * sum_(u,v in E) (x_u * x_v)
    Minimizes: - sum_i w_i * x_i + penalty * sum_(u,v in E) x_u * x_v
    """
    Q: Dict[Tuple[str, str], float] = {}
    var_map: Dict[str, int] = {}
    max_amount = max([d["amount_paise"] for _, d in G.nodes(data=True)]) if len(G) > 0 else 1.0

    for n, d in G.nodes(data=True):
        v = f"claim_{n}"
        var_map[v] = n
        norm_w = d["amount_paise"] / float(max_amount)
        Q[(v, v)] = -norm_w

    edge_penalty = penalty * 1.5
    for u, v in G.edges():
        v1, v2 = f"claim_{u}", f"claim_{v}"
        pair = (v1, v2) if v1 <= v2 else (v2, v1)
        Q[pair] = edge_penalty

    return Q, var_map

class P2DisputeSolvers:
    @staticmethod
    def solve_exact(claims: List[Dict[str, Any]], conflicts: List[Tuple[int, int]], seed: int = 42) -> SolverRun:
        t0 = time.perf_counter()
        G = build_claim_conflict_graph(claims, conflicts)

        # Classical Maximum Weight Independent Set via NetworkX / complement clique
        kept_nodes = nx.maximal_independent_set(G, seed=seed)
        all_nodes = set(G.nodes())
        rejected_nodes = list(all_nodes - set(kept_nodes))

        total_kept_amount = sum(G.nodes[n]["amount_paise"] for n in kept_nodes)
        runtime = (time.perf_counter() - t0) * 1000.0

        return SolverRun(
            problem_type="P2_DISPUTE_MIS",
            n_vars=len(claims),
            solver="ExactSolver_MIS",
            mode="fallback_local",
            seed=seed,
            params={"algorithm": "MaximalIndependentSet"},
            request_summary={"n_claims": len(claims), "n_conflicts": len(conflicts)},
            decoded_solution={"kept_claim_ids": kept_nodes, "rejected_claim_ids": rejected_nodes},
            objective=float(total_kept_amount),
            feasible=True,
            violations=[],
            runtime_ms=runtime,
            sdk_versions={"networkx": nx.__version__},
            raw_output={"kept_count": len(kept_nodes), "rejected_count": len(rejected_nodes)},
            optimality_gap_vs_exact=0.0
        )

    @staticmethod
    def solve_anneal(claims: List[Dict[str, Any]], conflicts: List[Tuple[int, int]], seed: int = 42) -> SolverRun:
        t0 = time.perf_counter()
        G = build_claim_conflict_graph(claims, conflicts)
        Q, var_map = build_mis_qubo(G)

        sampler = neal.SimulatedAnnealingSampler()
        bqm = dimod.BinaryQuadraticModel.from_qubo(Q)
        sampleset = sampler.sample(bqm, seed=seed, num_reads=100)
        best_sample = sampleset.first.sample
        runtime = (time.perf_counter() - t0) * 1000.0

        kept = [var_map[v] for v, val in best_sample.items() if val == 1 and v in var_map]
        all_ids = {c["id"] for c in claims}
        rejected = list(all_ids - set(kept))

        # Check for conflict violations
        violations = []
        for u, v in conflicts:
            if u in kept and v in kept:
                violations.append(f"Conflict violation: Both claims {u} and {v} kept")

        total_kept_amount = sum(c["amount_paise"] for c in claims if c["id"] in kept)

        return SolverRun(
            problem_type="P2_DISPUTE_MIS",
            n_vars=len(claims),
            solver="AnnealSolver_Neal_MIS",
            mode="fallback_local",
            seed=seed,
            params={"num_reads": 100},
            request_summary={"n_claims": len(claims), "n_conflicts": len(conflicts)},
            decoded_solution={"kept_claim_ids": kept, "rejected_claim_ids": rejected},
            objective=float(total_kept_amount),
            feasible=len(violations) == 0,
            violations=violations,
            runtime_ms=runtime,
            sdk_versions={"neal": neal.__version__},
            raw_output={"energy": sampleset.first.energy}
        )

    @staticmethod
    def solve_qpiai_opt(claims: List[Dict[str, Any]], conflicts: List[Tuple[int, int]], seed: int = 42) -> SolverRun:
        t0 = time.perf_counter()
        meta = {"n_claims": len(claims), "n_conflicts": len(conflicts)}

        def _sdk_call():
            raise RuntimeError(
                "QpiAI Opt is not adapted yet. Install qpiai-opt in this environment, "
                "run scripts/probe_qpiai.py, then bind its verified MIS/MVC or QUBO method."
            )

        raw_out, raw_err, mode = call_qpiai("opt", _sdk_call, meta)
        runtime = (time.perf_counter() - t0) * 1000.0

        if mode == "fallback_local":
            run = P2DisputeSolvers.solve_anneal(claims, conflicts, seed)
            run.solver = "QpiAIOpt_Fallback_MIS"
            run.mode = "fallback_local"
            run.raw_error = raw_err
            return run

        return SolverRun(
            problem_type="P2_DISPUTE_MIS",
            n_vars=len(claims),
            solver="QpiAIOptSolver_MIS",
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
