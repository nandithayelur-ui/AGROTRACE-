 AgroTrace AIQuant-A-Maze 3.0 | Web3 & Quantum-Optimized Agricultural Supply ChainAgroTrace AI is an enterprise-grade decentralized platform combining blockchain immutability with quantum-optimized routing to eliminate supply chain leakage, automate procurement dispatch, and secure tamper-evident audit trails.🏛️ System Architecture[ Hardhat Local Node (31337) ] <== RPC ==> [ Web3.py Client (chain/client.py) ]
              |                                            |
      AgroTrace.sol                                 chain/indexer.py
  - Role-based Access                                      |
  - Integer Mass-Balancing (grams)                 [ SQLite Cache ]
  - Tamper-Evident Keccak256 Audit Head                    |
              |                                            |
              +-------------------+------------------------+
                                  |
                      [ Verification Engines ]
                      - verify/reconcile.py
                      - verify/audit.py
                      - verify/feasibility.py
                                  |
                     [ Solvers & Optimization ]
                     - solvers/p1_allocation.py (QUBO)
                     - solvers/p2_dispute.py (MIS/MVC)
                     - solvers/p3_deduction.py
                     - solvers/qcloud_qaoa.py (QpiAI QAOA)
                                  |
                     [ FastAPI Orchestrator ] (Port 8080)
                     /lots, /optimize, /attacks
                                  |
                     [ React + Vite Dashboard ] (Port 5173)
----------------------------------------------------------------------------------------------------
Tech StackLayerTechnologiesSmart ContractsSolidity ^0.8.24, Hardhat, OpenZeppelin (Role-based access, DAG lot registry)Backend APIPython FastAPI (Port 8080), web3.py, SQLite cacheSolvers & QuantumQpiAI Opt & QCloud SDK (qpiai_quantum, PuLP 4.x)Frontend UIReact, Vite (Port 5173) Core FeaturesLot Registry & DAG Lineage: Track crop ancestry with strict integer mass-balance conservation ($\Sigma \text{children} + \text{loss} \le \text{parent}$) and shrinkage caps enforced on-chain.QpiAI Optimization: Commercial procurement allocation via QUBO matrix formulations and claim dispute resolution via Maximum Independent Set (MIS/MVC).Quantum Execution & Honesty Guard: Parameterized QAOA circuits and Bell-state QRNG experiments with strict execution validation (qpiai_real vs. fallback_local).Security Test Suite: Automated defense validations against double settlements, role impersonation, weight-creation fraud, and cache tampering. Getting StartedPrerequisitesPython (v3.11 – v3.14)Node.js LTS (v20 or v22)1. Run the Backend API# Activate virtual environment
.venv\Scripts\activate

# Start FastAPI server on port 8080
uvicorn api.main:app --port 8080 --reload
2. Run the Frontend DashboardOpen a separate terminal window:cd frontend
npm install
npm run dev
Access the dashboard at http://localhost:5173.🔍 API Verification EndpointsHealth Check: GET http://127.0.0.1:8080/healthSolver Comparison: GET http://127.0.0.1:8080/optimize/compareAudit Verification: GET http://127.0.0.1:8080/audit/verify📄 LicenseDistributed under the MIT License.
