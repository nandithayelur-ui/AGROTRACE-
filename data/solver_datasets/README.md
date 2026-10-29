# AgroTrace AI demo dataset v2
Money = paise (int). Weight = kg. Regenerate: `python generate_agrotrace_dataset.py`
users.json (roles + permissions) | tolerances.json | lots.json | operations.json (transfer/split/merge, mass balance)
alerts.json | grade_attestations.json | contracts.json | settlements.json | settlement_requests.json (good + bad)
audit_chain.json / audit_chain_tampered.json | optimizer_input.json (+ exact reference answer)
attack_scenarios.json (8 attacks) | expected_results.json (dashboard KPIs + reconcile)
Audit hash rule: signature = sha256(canonical_json(payload) + user_id + timestamp); hash = sha256(prev_hash + signature); genesis prev = 64 zeros.

## Solver datasets (generate_solver_datasets.py)
claim_conflict_graph.json (P2 MIS/MVC, 13 claims, 10 conflict edges + exact answer) | qaoa_instance.json (10-var QUBO + exact optimum)
deduction_partition_disputes.json (P3, 3 disputes of 8/10/12 items + optimal split) | feasibility_test_cases.json (7 allocation checks)
solver_run_fixtures.json (mode flags: fallback_local / error; no qpiai_real record is shipped) | onchain_commit_payloads.json
