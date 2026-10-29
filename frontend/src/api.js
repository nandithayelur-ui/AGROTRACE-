const BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8080";

async function request(path, options = {}) {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || `Request failed: ${res.status}`);
  }

  return res.json();
}

export const agroApi = {
  getHealth: () => request("/health"),
  getLots: () => request("/lots"),
  getLineage: (lotId) => request(`/lots/${lotId}/lineage`),
  getReconcile: () => request("/reconcile"),
  getAuditVerify: () => request("/audit/verify"),
  compareSolvers: () => request("/optimize/compare"),

  optimizeAllocation: (solver = "exact", commit = true) =>
    request(`/optimize/allocation?solver=${solver}&commit=${commit}`, {
      method: "POST",
    }),

  resolveDisputes: (solver = "exact", lotId = 2, commit = true) =>
    request(
      `/disputes/resolve?solver=${solver}&lot_id=${lotId}&commit=${commit}`,
      { method: "POST" }
    ),

  runQuantum: (experiment = "bell_qrng") =>
    request(`/quantum/run?experiment=${experiment}`, {
      method: "POST",
    }),

  getRuns: () => request("/runs"),
  getEvidence: (lotId) => request(`/evidence/${lotId}`),
  runAttack: (name) => request(`/attacks/${name}`, { method: "POST" }),
};
