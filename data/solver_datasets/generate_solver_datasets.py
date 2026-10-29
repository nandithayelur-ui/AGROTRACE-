"""
AgroTrace AI - solver datasets (P1 allocation checks, P2 claim-conflict MIS/MVC, P3 number partition, QAOA instance).
Run AFTER generate_agrotrace_dataset.py (reads data/*.json). Money in paise. Deterministic.
"""
import json, itertools, hashlib
D = lambda n: json.load(open(f"data/{n}.json"))
sha = lambda s: hashlib.sha256(s.encode()).hexdigest()
canon = lambda o: json.dumps(o, sort_keys=True, separators=(",", ":"))
lots = {l["id"]: l for l in D("lots")}; contracts = {c["id"]: c for c in D("contracts")}
opt = D("optimizer_input"); RANK = {"A": 3, "B": 2, "C": 1}

# ===================================================== P2: claim-conflict graph (MIS / MVC)
def anc(l):                                  # all ancestors of a lot via parent_lot_ids
    out, st = set(), list(lots[l]["parent_lot_ids"])
    while st:
        p = st.pop()
        if p not in out: out.add(p); st += lots[p]["parent_lot_ids"]
    return out
def claim(i, lot, inv, who, kg, typ, price, g):
    amt = round(kg * price * {"A": 1.0, "B": 0.95, "C": 0.88}[g]) if amt_override.get(i) is None else amt_override[i]
    return dict(id=f"CLM-{i:03d}", lot_id=lot, invoice_id=inv, claimant_id=who, claimed_kg=kg, claim_type=typ, amount_paise=amt)
amt_override = {1: 1624400, 2: 1624400, 4: 1483000, 13: 1066700}
claims = [
 claim(1,"LOT-2026-104","INV-9001","U-WH1",598,"FULL",2800,"A"),
 claim(2,"LOT-2026-104","INV-9101","U-SURESH",598,"FULL",2800,"A"),      # duplicate claim on same lot
 claim(3,"LOT-2026-084","INV-9103","U-WH1",600,"FULL",2800,"A"),         # ancestor of 104
 claim(4,"LOT-2026-105","INV-9002","U-WH2",495,"FULL",3000,"A"),
 claim(5,"LOT-2026-100","INV-9001","U-WH2",700,"FULL",2850,"A"),         # re-uses invoice of CLM-001
 claim(6,"LOT-2026-095","INV-9201","U-SURESH",1982,"FULL",2850,"B"),     # ancestor of 099/100/101
 claim(7,"LOT-2026-102","INV-9202","U-WH1",600,"PARTIAL",2950,"B"),
 claim(8,"LOT-2026-102","INV-9203","U-SURESH",600,"PARTIAL",2950,"B"),   # 600+600 > 1000 kg
 claim(9,"LOT-2026-101","INV-9204","U-WH2",472,"FULL",2250,"C"),         # descendant of 095
 claim(10,"LOT-2026-097","INV-9205","U-WH2",500,"FULL",2850,"A"),
 claim(11,"LOT-2026-094","INV-9206","U-WH2",1470,"FULL",2800,"A"),       # ancestor of 096/097/098
 claim(12,"LOT-2026-098","INV-9207","U-WH2",465,"FULL",2950,"B"),
 claim(13,"LOT-2026-107","INV-9003","U-NANDI",383,"FULL",2800,"A"),      # no conflicts
]
edges = []
for a, b in itertools.combinations(claims, 2):
    t = None
    if a["lot_id"] == b["lot_id"]:
        if a["claim_type"] == "PARTIAL" and b["claim_type"] == "PARTIAL":
            if a["claimed_kg"] + b["claimed_kg"] > lots[a["lot_id"]]["weight_kg"]: t = "OVER_QUANTITY"
        else: t = "SAME_LOT"
    if a["invoice_id"] == b["invoice_id"] and a["lot_id"] != b["lot_id"]: t = "SAME_INVOICE"
    elif a["lot_id"] != b["lot_id"] and (a["lot_id"] in anc(b["lot_id"]) or b["lot_id"] in anc(a["lot_id"])): t = "ANCESTOR_DESCENDANT"
    if t: edges.append(dict(a=a["id"], b=b["id"], type=t))
idx = {c["id"]: i for i, c in enumerate(claims)}; n = len(claims); W = [c["amount_paise"] for c in claims]
E = [(idx[e["a"]], idx[e["b"]]) for e in edges]
best = (-1, 0)
for m in range(1 << n):
    if any((m >> i) & 1 and (m >> j) & 1 for i, j in E): continue
    w = sum(W[i] for i in range(n) if (m >> i) & 1)
    if w > best[0]: best = (w, m)
mis = [claims[i]["id"] for i in range(n) if (best[1] >> i) & 1]; mvc = [c["id"] for c in claims if c["id"] not in mis]
for e in E: assert not (claims[e[0]]["id"] in mis and claims[e[1]]["id"] in mis)
conflict = dict(description="Nodes=claims weighted by amount_paise; edges=conflicts. MIS = max-value mutually compatible claims to APPROVE; MVC (complement) = claims to REJECT.",
    claims=claims, edges=edges,
    reference_exact_solution=dict(approve_mis=mis, reject_mvc=mvc, approved_value_paise=best[0], rejected_value_paise=sum(W) - best[0], total_claimed_paise=sum(W)))

# ===================================================== QAOA instance: 10-node subgraph -> QUBO
sub_ids = ["CLM-001","CLM-002","CLM-003","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009","CLM-010","CLM-011"]
si = {c: i for i, c in enumerate(sub_ids)}
sw = [claims[idx[c]]["amount_paise"] for c in sub_ids]; tot = sum(sw)
nw = [round(w / tot, 6) for w in sw]                      # normalised weights for QAOA angles
sedges = [(si[e["a"]], si[e["b"]]) for e in edges if e["a"] in si and e["b"] in si]
P = round(max(nw) + 0.01, 6)                              # penalty > max weight => any conflict is never profitable
def qubo_val(x): return sum(-nw[i]*x[i] for i in range(10)) + sum(P*x[i]*x[j] for i, j in sedges)
bq = min(itertools.product([0, 1], repeat=10), key=qubo_val)
qaoa = dict(description="10-variable MIS QUBO (minimise). C(x) = -sum w_i x_i + P * sum_{(i,j) in E} x_i x_j. For QAOA p=1..2 on QCloud/simulator; compare to exact baseline.",
    variables=sub_ids, normalised_weights=nw, penalty_P=P, edges=[[sub_ids[i], sub_ids[j]] for i, j in sedges],
    Q_linear=[[i, i, -nw[i]] for i in range(10)], Q_quadratic=[[i, j, P] for i, j in sedges],
    exact_optimum=dict(bitstring="".join(map(str, bq)), selected=[sub_ids[i] for i in range(10) if bq[i]], qubo_value=round(qubo_val(bq), 6),
                       value_paise=sum(sw[i] for i in range(10) if bq[i])),
    qaoa_config=dict(depths=[1, 2], shots=1024, metric="approximation_ratio = (best feasible value found) / (exact optimum value)", pass_threshold=0.9),
    bitstring_order="bit i corresponds to variables[i], left to right")

# ===================================================== P3: number partition (fair split of disputed deductions)
def partition(items):
    v = [x["amount_paise"] for x in items]; T = sum(v); best = (None, None)
    for m in range(1 << (len(v) - 1)):                    # fix last item to side B to halve search
        s = sum(v[i] for i in range(len(v)) if (m >> i) & 1); d = abs(T - 2 * s)
        if best[0] is None or d < best[0]: best = (d, m)
    A = [items[i]["id"] for i in range(len(v)) if (best[1] >> i) & 1]
    sa = sum(x["amount_paise"] for x in items if x["id"] in A)
    return dict(party_a_items=A, party_b_items=[x["id"] for x in items if x["id"] not in A], party_a_total_paise=sa, party_b_total_paise=T - sa, disparity_paise=best[0])
def mk(did, lot, cid, a, b, rows):
    items = [dict(id=f"{did}-I{k+1:02d}", description=d, amount_paise=v) for k, (d, v) in enumerate(rows)]
    return dict(id=did, lot_id=lot, contract_id=cid, party_a=a, party_b=b, items=items, total_paise=sum(v for _, v in rows), reference_exact_solution=partition(items))
partitions = [
 mk("DSP-001","LOT-2026-106","C-210","U-GREENFEED","U-WH2",[("Shortfall penalty (10 kg)",2000),("Transit moisture loss",21800),("Storage loss share",15000),("Re-bagging cost",8800),("Weighbridge re-test",3300),("Demurrage (2 days)",12500),("Cleaning cost",4700),("Handling charge",9600),("Fumigation",27100),("Sampling fee",6300)]),
 mk("DSP-002","LOT-2026-104","C-208","U-NANDI","U-WH1",[("Transport loss 2 kg",5600),("Handling",50000),("Unloading delay",18200),("Re-weigh fee",2500),("Sampling fee",4100),("Gunny bag cost",11800),("Moisture adjustment",14900),("Storage rent",20700)]),
 mk("DSP-003","LOT-2026-092","C-208","U-SURESH","U-WH2",[("Transport loss above tolerance (15 kg)",42000),("Moisture re-test",3500),("Extra drying cost",26400),("Truck waiting charge",15800),("Spillage at yard",7200),("Re-sorting labour",12100),("Bag replacement",9300),("Weighbridge fee",2800),("Insurance excess",18600),("Fumigation",9900),("Documentation fee",1500),("Quality sampling",5200)]),
]

# ===================================================== P1: feasibility-checker test cases + on-chain payloads
elig = {l["id"]: l for l in opt["lots"]}; opencon = {c["id"]: c for c in opt["contracts"]}
def check(alloc):
    v, used, got = [], {}, {}
    for a in alloc:
        l, c = a["lot_id"], a["contract_id"]
        used[l] = used.get(l, 0) + 1
        if l not in lots: v.append(f"UNKNOWN_LOT:{l}"); continue
        if lots[l]["is_consumed"]: v.append(f"LOT_NOT_AVAILABLE:{l}"); continue
        if not lots[l]["grade"]: v.append(f"UNVERIFIED_LOT:{l}"); continue
        if RANK[lots[l]["grade"]] < RANK[opencon[c]["min_grade"]]: v.append(f"GRADE_BELOW_MINIMUM:{l}->{c}")
        got[c] = got.get(c, 0) + lots[l]["weight_kg"]
    v += [f"LOT_OVER_ASSIGNED:{l}" for l, k in used.items() if k > 1]
    v += [f"CAPACITY_EXCEEDED:{c} ({g}>{opencon[c]['capacity_kg']})" for c, g in got.items() if g > opencon[c]["capacity_kg"]]
    return dict(feasible=not v, violations=v)
good = opt["reference_exact_solution"]["allocation"]
cases = [("valid_reference_optimum", good), ("lot_over_assigned", [dict(lot_id="LOT-2026-100", contract_id="C-211"), dict(lot_id="LOT-2026-100", contract_id="C-212")]),
 ("grade_below_minimum", [dict(lot_id="LOT-2026-101", contract_id="C-212")]), ("capacity_exceeded", [dict(lot_id="LOT-2026-102", contract_id="C-212"), dict(lot_id="LOT-2026-098", contract_id="C-212")]),
 ("unverified_lot_no_attestation", [dict(lot_id="LOT-2026-103", contract_id="C-213")]), ("lot_already_consumed_by_split", [dict(lot_id="LOT-2026-095", contract_id="C-213")]),
 ("unknown_lot", [dict(lot_id="LOT-2026-777", contract_id="C-213")])]
feas = [dict(name=n, allocation=a, expected=check(a)) for n, a in cases]
assert feas[0]["expected"]["feasible"]

alloc_run = dict(problem="P1_allocation", solver="exact_local", allocation=good, **{k: opt["reference_exact_solution"][k] for k in ("net_value_paise", "delivered_kg")})
dispute_run = dict(problem="P2_claim_conflict", solver="exact_local", approve=mis, reject=mvc, approved_value_paise=best[0])
def run(rid, prob, solver, mode, out=None, err=None):
    r = dict(id=rid, problem=prob, solver=solver, mode=mode, timeout_s=30, retries=2, fixture=True, output=out, error=err)
    r["output_hash"] = sha(canon(out)) if out else None; r["demo_cid"] = "bafybei-demo-" + r["output_hash"][:16] if out else None; return r
runs = [run("RUN-001","P1_allocation","exact_local","fallback_local",alloc_run), run("RUN-002","P2_claim_conflict","exact_local","fallback_local",dispute_run),
 run("RUN-003","P1_allocation","qpiai_opt","error",None,dict(code="QPIAI_OPT_API_KEY_MISSING",message="Key not configured; no result produced. Local solver output must NOT be relabelled qpiai_real.")),
 run("RUN-004","QAOA_claim_subgraph","qpiai_quantum","error",None,dict(code="QCLOUD_TIMEOUT",message="Job exceeded 30 s; retries exhausted."))]
onchain = dict(note="Demo CIDs are hash-derived placeholders, not real IPFS pins.",
  commitAllocation=dict(args=dict(allocation_hash=runs[0]["output_hash"], solver_run_cid=runs[0]["demo_cid"], lot_ids=[a["lot_id"] for a in good], contract_ids=[a["contract_id"] for a in good]), expected_verification=dict(mass_balance=True, lineage=True, grade=True, result="COMMIT_OK")),
  commitAllocation_bad=dict(args=dict(lot_ids=["LOT-2026-100","LOT-2026-100"], contract_ids=["C-211","C-212"]), expected_verification=dict(result="REVERT", reason="LOT_OVER_ASSIGNED")),
  resolveDispute=dict(args=dict(rejected_claim_ids=mvc, approved_claim_ids=mis, solver_run_cid=runs[1]["demo_cid"]), expected_verification=dict(result="RESOLVED", double_payment_possible=False)))

def dump(n, o): json.dump(o, open(f"data/{n}.json", "w"), indent=2)
dump("claim_conflict_graph", conflict); dump("qaoa_instance", qaoa); dump("deduction_partition_disputes", partitions)
dump("feasibility_test_cases", feas); dump("solver_run_fixtures", runs); dump("onchain_commit_payloads", onchain)
print("claims", n, "edges", len(edges), {t: sum(e["type"] == t for e in edges) for t in {e["type"] for e in edges}})
print("MIS approve", mis, best[0], "reject", mvc)
print("QAOA opt", qaoa["exact_optimum"]["selected"], qaoa["exact_optimum"]["value_paise"], "edges", len(sedges))
for p in partitions: print(p["id"], len(p["items"]), p["total_paise"], p["reference_exact_solution"]["disparity_paise"])
for f in feas: print(f["name"], f["expected"])
