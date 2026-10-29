# QpiAI SDK Real API Surface (Probed)

`
Python Version: 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)]
================================================================================
1. INSTALLED DISTRIBUTIONS MATCHING 'qpiai' / 'qcloud' / 'opt'
================================================================================
- qpiai-quantum == 0.7.5
  top_level.txt: ['qpiai_quantum']
  py files (1): ['__editable___qpiai_quantum_0_7_5_finder.py']

Discovered Root Modules: ['__editable__.qpiai_quantum-0.7.5.pth', '__editable___qpiai_quantum_0_7_5_finder', 'qpiai_quantum']

================================================================================
2. INTROSPECTING MODULE TREE: __editable__.qpiai_quantum-0.7.5.pth
================================================================================
Failed to import __editable__.qpiai_quantum-0.7.5.pth: ModuleNotFoundError: No module named '__editable__'

================================================================================
2. INTROSPECTING MODULE TREE: __editable___qpiai_quantum_0_7_5_finder
================================================================================

--- Module: __editable___qpiai_quantum_0_7_5_finder ---
  [Func]  install()

================================================================================
2. INTROSPECTING MODULE TREE: qpiai_quantum
================================================================================

--- Module: qpiai_quantum ---
  Doc: QpiAI Quantum SDK |  | A comprehensive Python-based quantum computing framework providing
  [Class] Backend(self, /, *args, **kwargs)
  [Class] BaseError(self, *message)
      .__init__(self, *message)
  [Class] BellStateGenerator(self, state_type: str = '|Ψ+>')
      .__init__(self, state_type: str = '|Ψ+>')
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .compare_all_bell_states(shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None)
      .get_all_bell_states() -> dict[str, 'BellStateGenerator']
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.4) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] BernsteinVazirani(self, num_qubits: int, hidden_string: str | None = None)
      .__init__(self, num_qubits: int, hidden_string: str | None = None)
      .build_circuit(self, hidden_string: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .find_hidden_string(self, shots: int = 1024, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .get_theoretical_result(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] ClassicalRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] ClusterStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .compare_different_sizes(qubit_range: list[int] = [2, 3, 4], shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None) -> dict[int, qpiai_quantum.results.base_result.BaseQuantumResult]
      .get_circuit_depth(self) -> int
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.5) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] DensityMatrix(self, data: list | numpy.ndarray | qpiai_quantum.circuit.circuit.Circuit | ForwardRef('DensityMatrix'), dims: list[int] | None = None, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local')
      .__init__(self, data: list | numpy.ndarray | qpiai_quantum.circuit.circuit.Circuit | ForwardRef('DensityMatrix'), dims: list[int] | None = None, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local')
      .copy(self) -> 'DensityMatrix'
      .entropy(self) -> float
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .from_circuit_object(circuit: qpiai_quantum.circuit.circuit.Circuit, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local') -> 'DensityMatrix'
      .from_formalism(formalism_dm) -> 'DensityMatrix'
      .from_label(label: str) -> 'DensityMatrix'
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .partial_trace(self, qubits_to_keep: list, dims: list | None = None) -> numpy.ndarray
      .probabilities(self) -> numpy.ndarray
      .probabilities_dict(self, decimals: int | None = None) -> dict
      .purity(self) -> float
      .to_formalism(self)
      .to_statevector(self)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] DeutschJozsa(self, num_qubits: int, oracle_type: str | None = None)
      .__init__(self, num_qubits: int, oracle_type: str | None = None)
      .build_circuit(self, oracle_type: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .determine_function_type(self, shots: int = 1024, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .get_theoretical_result(self) -> dict[str, typing.Any]
      .interpret_result(result) -> str
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] GHZStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .calculate_entanglement_depth(self) -> int
      .compare_different_sizes(qubit_range: list[int] = [3, 4, 5], shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None) -> dict[int, qpiai_quantum.results.base_result.BaseQuantumResult]
      .compare_with_product_state(self, result: qpiai_quantum.results.base_result.BaseQuantumResult) -> dict[str, float]
      .create_multiple_sizes(min_qubits: int = 3, max_qubits: int = 6) -> dict[int, 'GHZStateGenerator']
      .get_circuit_depth(self) -> int
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.4) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] GroverSearch(self, num_qubits: int, target: str | None = None)
      .__init__(self, num_qubits: int, target: str | None = None)
      .build_circuit(self, target: str | None = None, iterations: int | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .get_success_probability(self, iterations: int | None = None) -> float
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] JobManager(self, /, *args, **kwargs)
      .cancel_job(self, job_id: str) -> dict[str, typing.Any]
      .clear_resource_cache()
      .delete_job(self, job_id: str) -> dict[str, typing.Any]
      .get_current_job(self) -> dict[str, Any] | None
      .get_experiment_id_by_name(self, experiment_name: str) -> str
      .get_job_history(self, period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(self, job_id: str, device_name: str | None = None) -> 'JobResult'
      .get_job_status(self, job_id: str) -> dict[str, Any] | None
      .list_compute_resources(self) -> list[dict[str, typing.Any]]
      .submit_and_wait_for_results_qasm(self, qasm_string_or_circuit: str | qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False, use_events: bool = True, timeout: int = 300) -> qpiai_quantum.jobmanager.job_result.JobResult
      .submit_circuit_job(self, circuit: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str | None = None, compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .submit_qasm_job(self, qasm_string: str, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .track_job(func, job_name: str)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QFT(self, num_qubits: int, inverse: bool = False)
      .__init__(self, num_qubits: int, inverse: bool = False)
      .apply_inverse_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .apply_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .build_circuit(self, initialize_superposition: bool = False, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QRNG(self, n_bits: int = 8)
      .__init__(self, n_bits: int = 8)
      .build_circuit(self, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .generate(self, shots: int = 1, output_format: str = 'int', device_name: str = 'QpiAI-QSV-Local') -> int | bytes | str | list
      .generate_batch(self, count: int, output_format: str = 'int') -> list[int | bytes | str]
      .get_info(self)
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QpiAIQuantumAuth(self, /, *args, **kwargs)
      .list_compute_resources(display: bool = True)
      .login(api_key: str | None) -> str
      .logout() -> str
      .me(api_key: str | None = None) -> dict
      .verify_api_key() -> bool
  [Class] QuantumRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] ShorsAlgorithm(self, N: int)
      .__init__(self, N: int)
      .build_circuit(self, a: int, precision_qubits: int) -> qpiai_quantum.circuit.circuit.Circuit
      .factor(self, max_attempts: int = 10, device_name: str = 'QpiAI-QSV-Local') -> tuple[int, int] | None
      .find_period(self, a: int, precision_qubits: int | None = None, device_name: str = 'QpiAI-QSV-Local') -> int
      .gcd(a: int, b: int) -> int
      .get_info(self) -> dict[str, typing.Any]
      .is_power(n: int) -> tuple[int, int] | None
      .is_prime(n: int) -> bool
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] SimonAlgorithm(self, num_qubits: int, hidden_string: str | None = None, oracle_function: collections.abc.Callable | None = None)
      .__init__(self, num_qubits: int, hidden_string: str | None = None, oracle_function: collections.abc.Callable | None = None)
      .build_circuit(self, hidden_string: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .find_hidden_string(self, max_attempts: int | None = None, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] Statevector(self, data: 'list | np.ndarray | Circuit | Statevector', dims: 'list[int] | None' = None, experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local')
      .__init__(self, data: 'list | np.ndarray | Circuit | Statevector', dims: 'list[int] | None' = None, experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local')
      .copy(self) -> 'Statevector'
      .evolve(self, other: 'Circuit | np.ndarray') -> 'Statevector'
      .from_circuit_object(circuit: 'Circuit', experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local') -> 'Statevector'
      .from_label(label: 'str') -> 'Statevector'
      .is_valid(self, atol: 'float' = 1e-08) -> 'bool'
      .probabilities(self) -> 'np.ndarray'
      .probabilities_dict(self, decimals: 'int | None' = None) -> 'dict'
      .purity(self) -> 'float'
      .to_density_matrix(self)
      .to_dict(self, decimals: 'int' = 8) -> 'dict'
  [Class] VQESolver(self, n_qubits: int, hamiltonian: Any = None, ansatz: str | collections.abc.Callable = 'standard', optimizer: str = 'adam', max_iterations: int = 100, initial_point: numpy.ndarray | list[float] | None = None, verbose: bool = True, name: str = 'VQE')
      .__init__(self, n_qubits: int, hamiltonian: Any = None, ansatz: str | collections.abc.Callable = 'standard', optimizer: str = 'adam', max_iterations: int = 100, initial_point: numpy.ndarray | list[float] | None = None, verbose: bool = True, name: str = 'VQE')
      .build_circuit(self, parameters: numpy.ndarray | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> qpiai_quantum.algorithms.opt.solvers.vqe.VQEResult
      .to_dict(self, result: 'VQEResult') -> dict[str, typing.Any]
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
      .with_ansatz(self, ansatz)
      .with_backend_config(self, method: str = 'statevector', device_name: str = 'sim')
      .with_device_name(self, device_name: str)
      .with_experiment_name(self, experiment_name: str)
      .with_initial_point(self, point)
      .with_max_iterations(self, max_iter)
      .with_method(self, method: str)
      .with_optimizer(self, optimizer)
      .with_reverse_bits(self, reverse_bits: bool)
      .with_shots(self, shots)
      .with_verbose(self, verbose: bool)
  [Class] WStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .calculate_robustness(self, particle_loss_count: int = 1) -> float
      .compare_with_ghz_robustness(self, particle_loss_count: int = 1) -> dict[str, float]
      .count_excitations(self, result: qpiai_quantum.results.base_result.BaseQuantumResult) -> dict[int, int]
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.2) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.adapters ---
  [Class] QuantumAppAdapter(self)
      .__init__(self)
      .resolve_backend(self, backend: qpiai_quantum.jobmanager.backend.Backend)

--- Module: qpiai_quantum.adapters.quantum_app_adapter ---
  [Class] Backend(self, /, *args, **kwargs)
  [Class] QuantumAppAdapter(self)
      .__init__(self)
      .resolve_backend(self, backend: qpiai_quantum.jobmanager.backend.Backend)
  [Class] ResolvedBackend(self, ID: str, backend_name: str, address: str, health_check: str, run: str) -> None
      .__init__(self, ID: str, backend_name: str, address: str, health_check: str, run: str) -> None
  [Func]  get_active_auth_header() -> dict[str, str] | None
  [Func]  get_server_url() -> str
  [Func]  get_user() -> qpiai_quantum.authentication.user.SDKUser | None

--- Module: qpiai_quantum.algorithms ---
  [Class] AmplitudeEstimation(self, num_evaluation_qubits: int)
      .__init__(self, num_evaluation_qubits: int)
      .build_circuit(self, problem: qpiai_quantum.algorithms.amplitude_estimation.EstimationProblem) -> qpiai_quantum.circuit.circuit.Circuit
      .estimate(self, problem: qpiai_quantum.algorithms.amplitude_estimation.EstimationProblem, shots: int = 1024, device_name: str = 'QpiAI-QSV-Local') -> float
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] BernsteinVazirani(self, num_qubits: int, hidden_string: str | None = None)
      .__init__(self, num_qubits: int, hidden_string: str | None = None)
      .build_circuit(self, hidden_string: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .find_hidden_string(self, shots: int = 1024, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .get_theoretical_result(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] DeutschJozsa(self, num_qubits: int, oracle_type: str | None = None)
      .__init__(self, num_qubits: int, oracle_type: str | None = None)
      .build_circuit(self, oracle_type: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .determine_function_type(self, shots: int = 1024, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .get_theoretical_result(self) -> dict[str, typing.Any]
      .interpret_result(result) -> str
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] EstimationProblem(self, state_preparation: qpiai_quantum.circuit.circuit.Circuit, objective_qubits: list[int], is_good_state: collections.abc.Callable[[str], bool] | None = None)
      .__init__(self, state_preparation: qpiai_quantum.circuit.circuit.Circuit, objective_qubits: list[int], is_good_state: collections.abc.Callable[[str], bool] | None = None)
  [Class] GroverSearch(self, num_qubits: int, target: str | None = None)
      .__init__(self, num_qubits: int, target: str | None = None)
      .build_circuit(self, target: str | None = None, iterations: int | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .get_success_probability(self, iterations: int | None = None) -> float
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] IterativeAmplitudeEstimation(self, epsilon_target: float, alpha: float)
      .__init__(self, epsilon_target: float, alpha: float)
      .build_circuit(self, problem: qpiai_quantum.algorithms.amplitude_estimation.EstimationProblem, k: int) -> qpiai_quantum.circuit.circuit.Circuit
      .estimate(self, problem: qpiai_quantum.algorithms.amplitude_estimation.EstimationProblem, shots: int = 1000, device_name: str = 'QpiAI-QSV-Local') -> float
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QFT(self, num_qubits: int, inverse: bool = False)
      .__init__(self, num_qubits: int, inverse: bool = False)
      .apply_inverse_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .apply_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .build_circuit(self, initialize_superposition: bool = False, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QRNG(self, n_bits: int = 8)
      .__init__(self, n_bits: int = 8)
      .build_circuit(self, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .generate(self, shots: int = 1, output_format: str = 'int', device_name: str = 'QpiAI-QSV-Local') -> int | bytes | str | list
      .generate_batch(self, count: int, output_format: str = 'int') -> list[int | bytes | str]
      .get_info(self)
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumPhaseEstimation(self, precision_qubits: int, eigenstate_qubits: int)
      .__init__(self, precision_qubits: int, eigenstate_qubits: int)
      .build_circuit(self, unitary: str = 'T', eigenstate_preparation: collections.abc.Callable | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .estimate_phase(self, unitary: str = 'T', eigenstate_preparation: collections.abc.Callable | None = None, device_name: str = 'QpiAI-QSV-Local') -> float
      .get_info(self) -> dict[str, typing.Any]
      .get_theoretical_phase(self, unitary: str) -> float
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] ShorsAlgorithm(self, N: int)
      .__init__(self, N: int)
      .build_circuit(self, a: int, precision_qubits: int) -> qpiai_quantum.circuit.circuit.Circuit
      .factor(self, max_attempts: int = 10, device_name: str = 'QpiAI-QSV-Local') -> tuple[int, int] | None
      .find_period(self, a: int, precision_qubits: int | None = None, device_name: str = 'QpiAI-QSV-Local') -> int
      .gcd(a: int, b: int) -> int
      .get_info(self) -> dict[str, typing.Any]
      .is_power(n: int) -> tuple[int, int] | None
      .is_prime(n: int) -> bool
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] SimonAlgorithm(self, num_qubits: int, hidden_string: str | None = None, oracle_function: collections.abc.Callable | None = None)
      .__init__(self, num_qubits: int, hidden_string: str | None = None, oracle_function: collections.abc.Callable | None = None)
      .build_circuit(self, hidden_string: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .find_hidden_string(self, max_attempts: int | None = None, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] VQESolver(self, n_qubits: int, hamiltonian: Any = None, ansatz: str | collections.abc.Callable = 'standard', optimizer: str = 'adam', max_iterations: int = 100, initial_point: numpy.ndarray | list[float] | None = None, verbose: bool = True, name: str = 'VQE')
      .__init__(self, n_qubits: int, hamiltonian: Any = None, ansatz: str | collections.abc.Callable = 'standard', optimizer: str = 'adam', max_iterations: int = 100, initial_point: numpy.ndarray | list[float] | None = None, verbose: bool = True, name: str = 'VQE')
      .build_circuit(self, parameters: numpy.ndarray | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> qpiai_quantum.algorithms.opt.solvers.vqe.VQEResult
      .to_dict(self, result: 'VQEResult') -> dict[str, typing.Any]
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
      .with_ansatz(self, ansatz)
      .with_backend_config(self, method: str = 'statevector', device_name: str = 'sim')
      .with_device_name(self, device_name: str)
      .with_experiment_name(self, experiment_name: str)
      .with_initial_point(self, point)
      .with_max_iterations(self, max_iter)
      .with_method(self, method: str)
      .with_optimizer(self, optimizer)
      .with_reverse_bits(self, reverse_bits: bool)
      .with_shots(self, shots)
      .with_verbose(self, verbose: bool)
  [Func]  plot_vqe_results_comprehensive(result, figsize=(16, 12))

--- Module: qpiai_quantum.algorithms.amplitude_estimation ---
  [Class] AmplitudeEstimation(self, num_evaluation_qubits: int)
      .__init__(self, num_evaluation_qubits: int)
      .build_circuit(self, problem: qpiai_quantum.algorithms.amplitude_estimation.EstimationProblem) -> qpiai_quantum.circuit.circuit.Circuit
      .estimate(self, problem: qpiai_quantum.algorithms.amplitude_estimation.EstimationProblem, shots: int = 1024, device_name: str = 'QpiAI-QSV-Local') -> float
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] BarrierOperation(self, *qubits: int | list[int])
      .__init__(self, *qubits: int | list[int])
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CCXGate(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .__init__(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CPGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CSwapGate(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .__init__(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CXGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CYGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CZGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] EstimationProblem(self, state_preparation: qpiai_quantum.circuit.circuit.Circuit, objective_qubits: list[int], is_good_state: collections.abc.Callable[[str], bool] | None = None)
      .__init__(self, state_preparation: qpiai_quantum.circuit.circuit.Circuit, objective_qubits: list[int], is_good_state: collections.abc.Callable[[str], bool] | None = None)
  [Class] HGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] IDGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] IterativeAmplitudeEstimation(self, epsilon_target: float, alpha: float)
      .__init__(self, epsilon_target: float, alpha: float)
      .build_circuit(self, problem: qpiai_quantum.algorithms.amplitude_estimation.EstimationProblem, k: int) -> qpiai_quantum.circuit.circuit.Circuit
      .estimate(self, problem: qpiai_quantum.algorithms.amplitude_estimation.EstimationProblem, shots: int = 1000, device_name: str = 'QpiAI-QSV-Local') -> float
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] MCXGate(self, control_qubits: list[int], target_qubit: int)
      .__init__(self, control_qubits: list[int], target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] MeasureOperation(self, qubit: int, clbit: int)
      .__init__(self, qubit: int, clbit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] OperationType(self, /, *args, **kwargs)
  [Class] PGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] QFT(self, num_qubits: int, inverse: bool = False)
      .__init__(self, num_qubits: int, inverse: bool = False)
      .apply_inverse_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .apply_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .build_circuit(self, initialize_superposition: bool = False, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] RXGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RYGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RZGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RZZGate(self, qubit1: int, qubit2: int, theta: float)
      .__init__(self, qubit1: int, qubit2: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SDGGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SwapGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] TDGGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] TGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] XGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] YGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ZGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]

--- Module: qpiai_quantum.algorithms.base ---
  [Class] Backend(self, /, *args, **kwargs)
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] CircuitError(self, *message)
      .__init__(self, *message)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.bernstein_vazirani ---
  Doc: Bernstein-Vazirani Algorithm Implementation |  | The Bernstein-Vazirani algorithm determines a hidden bitstring s ∈ {0,1}^n
  [Class] BernsteinVazirani(self, num_qubits: int, hidden_string: str | None = None)
      .__init__(self, num_qubits: int, hidden_string: str | None = None)
      .build_circuit(self, hidden_string: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .find_hidden_string(self, shots: int = 1024, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .get_theoretical_result(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.deutsch_jozsa ---
  Doc: Deutsch-Jozsa Algorithm Implementation |  | The Deutsch-Jozsa algorithm determines whether a given boolean function
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] DeutschJozsa(self, num_qubits: int, oracle_type: str | None = None)
      .__init__(self, num_qubits: int, oracle_type: str | None = None)
      .build_circuit(self, oracle_type: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .determine_function_type(self, shots: int = 1024, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .get_theoretical_result(self) -> dict[str, typing.Any]
      .interpret_result(result) -> str
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.grover ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] GroverSearch(self, num_qubits: int, target: str | None = None)
      .__init__(self, num_qubits: int, target: str | None = None)
      .build_circuit(self, target: str | None = None, iterations: int | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .get_success_probability(self, iterations: int | None = None) -> float
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.opt ---
  Doc: Optimization algorithms and related components.

--- Module: qpiai_quantum.algorithms.opt.ansatz ---
  [Func]  count_parameters(circuit: qpiai_quantum.circuit.circuit.Circuit) -> int
  [Func]  custom_ansatz(*args, **kwargs)
  [Func]  hardware_efficient_ansatz(n_qubits: int, depth: int = 2, entanglement: str = 'linear') -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  qaoa_ansatz_from_problem(problem: Any, layers: int = 1) -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  standard_qaoa_ansatz(n_qubits: int, hamiltonian: Any, layers: int = 1, mixer: str = 'x') -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  standard_vqe_ansatz(n_qubits: int, layers: int = 2, entanglement: str = 'linear') -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  two_local_ansatz(n_qubits: int, rotation_blocks: str = 'ry', entanglement_blocks: str = 'cz', reps: int = 3) -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.algorithms.opt.ansatz.custom ---
  Doc: Custom ansatz template.
  [Func]  custom_ansatz(*args, **kwargs)

--- Module: qpiai_quantum.algorithms.opt.ansatz.hardware_efficient ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] QuantumRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Func]  hardware_efficient_ansatz(n_qubits: int, depth: int = 2, entanglement: str = 'linear') -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  two_local_ansatz(n_qubits: int, rotation_blocks: str = 'ry', entanglement_blocks: str = 'cz', reps: int = 3) -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.algorithms.opt.ansatz.standard ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] QuantumRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Func]  count_parameters(circuit: qpiai_quantum.circuit.circuit.Circuit) -> int
  [Func]  qaoa_ansatz_from_problem(problem: Any, layers: int = 1) -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  standard_qaoa_ansatz(n_qubits: int, hamiltonian: Any, layers: int = 1, mixer: str = 'x') -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  standard_vqe_ansatz(n_qubits: int, layers: int = 2, entanglement: str = 'linear') -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.algorithms.opt.problems ---
  [Class] MaxCutProblem(self, graph: networkx.classes.graph.Graph)
      .__init__(self, graph: networkx.classes.graph.Graph)
      .compute_solution_quality(self, solution: dict[str, typing.Any]) -> dict[str, float]
      .decode_solution(self, bitstring: str) -> dict[str, typing.Any]
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
      .validate_solution(self, solution: dict[str, typing.Any]) -> tuple[bool, str]
  [Class] PortfolioOptimizationProblem(self, returns: numpy.ndarray, risk_matrix: numpy.ndarray, budget: float = 1.0, risk_tolerance: float = 1.0)
      .__init__(self, returns: numpy.ndarray, risk_matrix: numpy.ndarray, budget: float = 1.0, risk_tolerance: float = 1.0)
      .compute_solution_quality(self, solution: dict[str, typing.Any]) -> dict[str, float]
      .decode_solution(self, bitstring: str) -> dict[str, typing.Any]
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
      .validate_solution(self, solution: dict[str, typing.Any]) -> tuple[bool, str]

--- Module: qpiai_quantum.algorithms.opt.problems.base ---
  [Class] OptimizationProblem(self)
      .__init__(self)
      .compute_solution_quality(self, solution: dict[str, typing.Any]) -> dict[str, float]
      .decode_solution(self, bitstring: str) -> dict[str, typing.Any]
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
      .validate_solution(self, solution: dict[str, typing.Any]) -> tuple[bool, str]

--- Module: qpiai_quantum.algorithms.opt.problems.optimization ---

--- Module: qpiai_quantum.algorithms.opt.solvers ---
  [Class] QAOASolver(self, problem: Any = None, layers: int = 1, optimizer: str = 'COBYLA', max_iterations: int = 100, initial_params: numpy.ndarray | None = None, ansatz: str | collections.abc.Callable = 'standard', mixer: str = 'x', verbose: bool = True, name: str = 'QAOA')
      .__init__(self, problem: Any = None, layers: int = 1, optimizer: str = 'COBYLA', max_iterations: int = 100, initial_params: numpy.ndarray | None = None, ansatz: str | collections.abc.Callable = 'standard', mixer: str = 'x', verbose: bool = True, name: str = 'QAOA')
      .build_circuit(self, parameters: numpy.ndarray | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .get_name(self) -> str
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> qpiai_quantum.algorithms.opt.solvers.qaoa.QAOAResult
      .to_dict(self, result: 'QAOAResult') -> dict[str, typing.Any]
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
      .with_ansatz(self, ansatz: str | collections.abc.Callable)
      .with_backend_config(self, method: str = 'statevector', device_name: str = 'sim')
      .with_initial_params(self, params: numpy.ndarray)
      .with_layers(self, layers: int)
      .with_max_iterations(self, max_iter: int)
      .with_mixer(self, mixer: str)
      .with_optimizer(self, optimizer: str)
      .with_shots(self, shots: int)
      .with_verbose(self, verbose: bool)
  [Class] VQESolver(self, n_qubits: int, hamiltonian: Any = None, ansatz: str | collections.abc.Callable = 'standard', optimizer: str = 'adam', max_iterations: int = 100, initial_point: numpy.ndarray | list[float] | None = None, verbose: bool = True, name: str = 'VQE')
      .__init__(self, n_qubits: int, hamiltonian: Any = None, ansatz: str | collections.abc.Callable = 'standard', optimizer: str = 'adam', max_iterations: int = 100, initial_point: numpy.ndarray | list[float] | None = None, verbose: bool = True, name: str = 'VQE')
      .build_circuit(self, parameters: numpy.ndarray | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> qpiai_quantum.algorithms.opt.solvers.vqe.VQEResult
      .to_dict(self, result: 'VQEResult') -> dict[str, typing.Any]
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
      .with_ansatz(self, ansatz)
      .with_backend_config(self, method: str = 'statevector', device_name: str = 'sim')
      .with_device_name(self, device_name: str)
      .with_experiment_name(self, experiment_name: str)
      .with_initial_point(self, point)
      .with_max_iterations(self, max_iter)
      .with_method(self, method: str)
      .with_optimizer(self, optimizer)
      .with_reverse_bits(self, reverse_bits: bool)
      .with_shots(self, shots)
      .with_verbose(self, verbose: bool)

--- Module: qpiai_quantum.algorithms.opt.solvers.qaoa ---
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] JobManager(self, /, *args, **kwargs)
      .cancel_job(self, job_id: str) -> dict[str, typing.Any]
      .clear_resource_cache()
      .delete_job(self, job_id: str) -> dict[str, typing.Any]
      .get_current_job(self) -> dict[str, Any] | None
      .get_experiment_id_by_name(self, experiment_name: str) -> str
      .get_job_history(self, period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(self, job_id: str, device_name: str | None = None) -> 'JobResult'
      .get_job_status(self, job_id: str) -> dict[str, Any] | None
      .list_compute_resources(self) -> list[dict[str, typing.Any]]
      .submit_and_wait_for_results_qasm(self, qasm_string_or_circuit: str | qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False, use_events: bool = True, timeout: int = 300) -> qpiai_quantum.jobmanager.job_result.JobResult
      .submit_circuit_job(self, circuit: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str | None = None, compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .submit_qasm_job(self, qasm_string: str, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .track_job(func, job_name: str)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] OperationType(self, /, *args, **kwargs)
  [Class] QAOAResult(self, optimal_parameters: list[float], optimal_energy: float, energy_history: list[float], param_history: list[list[float]], solution: Any, bitstring: str, counts: dict[str, int], is_valid: bool, validation_message: str, quality_metrics: dict[str, typing.Any], metadata: dict[str, typing.Any]) -> None
      .__init__(self, optimal_parameters: list[float], optimal_energy: float, energy_history: list[float], param_history: list[list[float]], solution: Any, bitstring: str, counts: dict[str, int], is_valid: bool, validation_message: str, quality_metrics: dict[str, typing.Any], metadata: dict[str, typing.Any]) -> None
  [Class] QAOASolver(self, problem: Any = None, layers: int = 1, optimizer: str = 'COBYLA', max_iterations: int = 100, initial_params: numpy.ndarray | None = None, ansatz: str | collections.abc.Callable = 'standard', mixer: str = 'x', verbose: bool = True, name: str = 'QAOA')
      .__init__(self, problem: Any = None, layers: int = 1, optimizer: str = 'COBYLA', max_iterations: int = 100, initial_params: numpy.ndarray | None = None, ansatz: str | collections.abc.Callable = 'standard', mixer: str = 'x', verbose: bool = True, name: str = 'QAOA')
      .build_circuit(self, parameters: numpy.ndarray | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .get_name(self) -> str
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> qpiai_quantum.algorithms.opt.solvers.qaoa.QAOAResult
      .to_dict(self, result: 'QAOAResult') -> dict[str, typing.Any]
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
      .with_ansatz(self, ansatz: str | collections.abc.Callable)
      .with_backend_config(self, method: str = 'statevector', device_name: str = 'sim')
      .with_initial_params(self, params: numpy.ndarray)
      .with_layers(self, layers: int)
      .with_max_iterations(self, max_iter: int)
      .with_mixer(self, mixer: str)
      .with_optimizer(self, optimizer: str)
      .with_shots(self, shots: int)
      .with_verbose(self, verbose: bool)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Func]  adam_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  cobyla_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, maxfun: int | None = None, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  count_parameters(circuit: qpiai_quantum.circuit.circuit.Circuit) -> int
  [Func]  genetic_algorithm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, population_size: int = 50, mutation_rate: float = 0.1, crossover_rate: float = 0.8, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  gradient_descent_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.01, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  hardware_efficient_ansatz(n_qubits: int, depth: int = 2, entanglement: str = 'linear') -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  l_bfgs_b_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray] | None = None, initial_point: numpy.ndarray = None, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  nelder_mead_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  particle_swarm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, n_particles: int = 30, w: float = 0.9, c1: float = 2.0, c2: float = 2.0, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  powell_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  slsqp_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, constraints: list[dict] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  spsa_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, maxiter: int = 100, tol: float = 1e-06, learning_rate: float = 0.1, perturbation_scale: float = 0.1, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  standard_qaoa_ansatz(n_qubits: int, hamiltonian: Any, layers: int = 1, mixer: str = 'x') -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.algorithms.opt.solvers.vqe ---
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] JobManager(self, /, *args, **kwargs)
      .cancel_job(self, job_id: str) -> dict[str, typing.Any]
      .clear_resource_cache()
      .delete_job(self, job_id: str) -> dict[str, typing.Any]
      .get_current_job(self) -> dict[str, Any] | None
      .get_experiment_id_by_name(self, experiment_name: str) -> str
      .get_job_history(self, period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(self, job_id: str, device_name: str | None = None) -> 'JobResult'
      .get_job_status(self, job_id: str) -> dict[str, Any] | None
      .list_compute_resources(self) -> list[dict[str, typing.Any]]
      .submit_and_wait_for_results_qasm(self, qasm_string_or_circuit: str | qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False, use_events: bool = True, timeout: int = 300) -> qpiai_quantum.jobmanager.job_result.JobResult
      .submit_circuit_job(self, circuit: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str | None = None, compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .submit_qasm_job(self, qasm_string: str, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .track_job(func, job_name: str)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] OperationType(self, /, *args, **kwargs)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] VQEResult(self, optimal_parameters: list[float], optimal_energy: float, energy_history: list[float], param_history: list[list[float]], bitstring: str, counts: dict[str, int], metadata: dict[str, typing.Any], energy_standard_error: float | None = None) -> None
      .__init__(self, optimal_parameters: list[float], optimal_energy: float, energy_history: list[float], param_history: list[list[float]], bitstring: str, counts: dict[str, int], metadata: dict[str, typing.Any], energy_standard_error: float | None = None) -> None
  [Class] VQESolver(self, n_qubits: int, hamiltonian: Any = None, ansatz: str | collections.abc.Callable = 'standard', optimizer: str = 'adam', max_iterations: int = 100, initial_point: numpy.ndarray | list[float] | None = None, verbose: bool = True, name: str = 'VQE')
      .__init__(self, n_qubits: int, hamiltonian: Any = None, ansatz: str | collections.abc.Callable = 'standard', optimizer: str = 'adam', max_iterations: int = 100, initial_point: numpy.ndarray | list[float] | None = None, verbose: bool = True, name: str = 'VQE')
      .build_circuit(self, parameters: numpy.ndarray | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> qpiai_quantum.algorithms.opt.solvers.vqe.VQEResult
      .to_dict(self, result: 'VQEResult') -> dict[str, typing.Any]
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
      .with_ansatz(self, ansatz)
      .with_backend_config(self, method: str = 'statevector', device_name: str = 'sim')
      .with_device_name(self, device_name: str)
      .with_experiment_name(self, experiment_name: str)
      .with_initial_point(self, point)
      .with_max_iterations(self, max_iter)
      .with_method(self, method: str)
      .with_optimizer(self, optimizer)
      .with_reverse_bits(self, reverse_bits: bool)
      .with_shots(self, shots)
      .with_verbose(self, verbose: bool)
  [Func]  adam_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  cobyla_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, maxfun: int | None = None, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  count_parameters(circuit: qpiai_quantum.circuit.circuit.Circuit) -> int
  [Func]  genetic_algorithm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, population_size: int = 50, mutation_rate: float = 0.1, crossover_rate: float = 0.8, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  gradient_descent_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.01, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  hardware_efficient_ansatz(n_qubits: int, depth: int = 2, entanglement: str = 'linear') -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  l_bfgs_b_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray] | None = None, initial_point: numpy.ndarray = None, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  nelder_mead_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  particle_swarm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, n_particles: int = 30, w: float = 0.9, c1: float = 2.0, c2: float = 2.0, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  powell_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  slsqp_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, constraints: list[dict] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  spsa_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, maxiter: int = 100, tol: float = 1e-06, learning_rate: float = 0.1, perturbation_scale: float = 0.1, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  standard_vqe_ansatz(n_qubits: int, layers: int = 2, entanglement: str = 'linear') -> qpiai_quantum.circuit.circuit.Circuit
  [Func]  two_local_ansatz(n_qubits: int, rotation_blocks: str = 'ry', entanglement_blocks: str = 'cz', reps: int = 3) -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.algorithms.phase_estimation ---
  Doc: Quantum Phase Estimation Algorithm Implementation |  | Quantum Phase Estimation is a key subroutine in many quantum algorithms,
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QFT(self, num_qubits: int, inverse: bool = False)
      .__init__(self, num_qubits: int, inverse: bool = False)
      .apply_inverse_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .apply_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .build_circuit(self, initialize_superposition: bool = False, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumPhaseEstimation(self, precision_qubits: int, eigenstate_qubits: int)
      .__init__(self, precision_qubits: int, eigenstate_qubits: int)
      .build_circuit(self, unitary: str = 'T', eigenstate_preparation: collections.abc.Callable | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .estimate_phase(self, unitary: str = 'T', eigenstate_preparation: collections.abc.Callable | None = None, device_name: str = 'QpiAI-QSV-Local') -> float
      .get_info(self) -> dict[str, typing.Any]
      .get_theoretical_phase(self, unitary: str) -> float
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.qft ---
  Doc: Quantum Fourier Transform (QFT) Algorithm Implementation
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QFT(self, num_qubits: int, inverse: bool = False)
      .__init__(self, num_qubits: int, inverse: bool = False)
      .apply_inverse_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .apply_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .build_circuit(self, initialize_superposition: bool = False, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.qrng ---
  Doc: Quantum Random Number Generator (QRNG) |  | Generates random numbers by exploiting quantum mechanical uncertainty.
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QRNG(self, n_bits: int = 8)
      .__init__(self, n_bits: int = 8)
      .build_circuit(self, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .generate(self, shots: int = 1, output_format: str = 'int', device_name: str = 'QpiAI-QSV-Local') -> int | bytes | str | list
      .generate_batch(self, count: int, output_format: str = 'int') -> list[int | bytes | str]
      .get_info(self)
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.shor ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QFT(self, num_qubits: int, inverse: bool = False)
      .__init__(self, num_qubits: int, inverse: bool = False)
      .apply_inverse_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .apply_qft_to_circuit(circuit: qpiai_quantum.circuit.circuit.Circuit, start: int, n: int)
      .build_circuit(self, initialize_superposition: bool = False, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] ShorsAlgorithm(self, N: int)
      .__init__(self, N: int)
      .build_circuit(self, a: int, precision_qubits: int) -> qpiai_quantum.circuit.circuit.Circuit
      .factor(self, max_attempts: int = 10, device_name: str = 'QpiAI-QSV-Local') -> tuple[int, int] | None
      .find_period(self, a: int, precision_qubits: int | None = None, device_name: str = 'QpiAI-QSV-Local') -> int
      .gcd(a: int, b: int) -> int
      .get_info(self) -> dict[str, typing.Any]
      .is_power(n: int) -> tuple[int, int] | None
      .is_prime(n: int) -> bool
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.simon ---
  Doc: Simon's Algorithm Implementation |  | Simon's algorithm finds hidden bitstring patterns with exponential speedup
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] SimonAlgorithm(self, num_qubits: int, hidden_string: str | None = None, oracle_function: collections.abc.Callable | None = None)
      .__init__(self, num_qubits: int, hidden_string: str | None = None, oracle_function: collections.abc.Callable | None = None)
      .build_circuit(self, hidden_string: str | None = None) -> qpiai_quantum.circuit.circuit.Circuit
      .find_hidden_string(self, max_attempts: int | None = None, device_name: str = 'QpiAI-QSV-Local') -> str
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.algorithms.utils ---
  [Func]  adagrad_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.01, epsilon: float = 1e-08, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  adam_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  amplitude_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]
  [Func]  angle_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]
  [Func]  basis_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]
  [Func]  cg_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray] | None = None, initial_point: numpy.ndarray = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  cobyla_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, maxfun: int | None = None, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  differential_evolution_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, tol: float = 1e-06, popsize: int = 15, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  genetic_algorithm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, population_size: int = 50, mutation_rate: float = 0.1, crossover_rate: float = 0.8, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  gradient_descent_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.01, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  l_bfgs_b_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray] | None = None, initial_point: numpy.ndarray = None, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  nelder_mead_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  particle_swarm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, n_particles: int = 30, w: float = 0.9, c1: float = 2.0, c2: float = 2.0, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  plot_vqe_results_comprehensive(result, figsize=(16, 12))
  [Func]  slsqp_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, constraints: list[dict] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  spsa_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, maxiter: int = 100, tol: float = 1e-06, learning_rate: float = 0.1, perturbation_scale: float = 0.1, **kwargs) -> tuple[numpy.ndarray, float, dict]

--- Module: qpiai_quantum.algorithms.utils.encoders ---
  [Func]  amplitude_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]
  [Func]  angle_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]
  [Func]  basis_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]

--- Module: qpiai_quantum.algorithms.utils.encoders.amplitude ---
  Doc: Amplitude encoding for quantum data.
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Func]  amplitude_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]

--- Module: qpiai_quantum.algorithms.utils.encoders.angle ---
  Doc: Angle encoding for quantum data.
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Func]  angle_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]

--- Module: qpiai_quantum.algorithms.utils.encoders.basis ---
  Doc: Basis encoding for quantum data.
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Func]  basis_encode(data: numpy.ndarray, circuit: qpiai_quantum.circuit.circuit.Circuit | None = None, qubits: list[int] | None = None) -> tuple[qpiai_quantum.circuit.circuit.Circuit, list[int]]

--- Module: qpiai_quantum.algorithms.utils.optimizers ---
  [Func]  adagrad_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.01, epsilon: float = 1e-08, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  adam_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  cg_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray] | None = None, initial_point: numpy.ndarray = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  cobyla_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, maxfun: int | None = None, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  differential_evolution_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, tol: float = 1e-06, popsize: int = 15, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  genetic_algorithm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, population_size: int = 50, mutation_rate: float = 0.1, crossover_rate: float = 0.8, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  gradient_descent_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.01, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  l_bfgs_b_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray] | None = None, initial_point: numpy.ndarray = None, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  nelder_mead_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  particle_swarm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, n_particles: int = 30, w: float = 0.9, c1: float = 2.0, c2: float = 2.0, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  powell_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  slsqp_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, constraints: list[dict] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  spsa_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, maxiter: int = 100, tol: float = 1e-06, learning_rate: float = 0.1, perturbation_scale: float = 0.1, **kwargs) -> tuple[numpy.ndarray, float, dict]

--- Module: qpiai_quantum.algorithms.utils.optimizers.gradient_based ---
  Doc: Gradient-based optimization methods with complete history tracking.
  [Class] HistoryTracker(self)
      .__init__(self)
      .create_callback(self, user_callback: collections.abc.Callable | None = None)
      .create_wrapped_objective(self, objective: collections.abc.Callable[[numpy.ndarray], float])
      .reset(self)
  [Func]  adagrad_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.01, epsilon: float = 1e-08, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  adam_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  cg_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray] | None = None, initial_point: numpy.ndarray = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  gradient_descent_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray], initial_point: numpy.ndarray, learning_rate: float = 0.01, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  l_bfgs_b_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], gradient: collections.abc.Callable[[numpy.ndarray], numpy.ndarray] | None = None, initial_point: numpy.ndarray = None, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]

--- Module: qpiai_quantum.algorithms.utils.optimizers.gradient_free ---
  [Class] HistoryTracker(self)
      .__init__(self)
      .create_callback(self, user_callback: collections.abc.Callable | None = None)
      .create_wrapped_objective(self, objective: collections.abc.Callable[[numpy.ndarray], float])
      .reset(self)
  [Func]  cobyla_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, maxfun: int | None = None, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  differential_evolution_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, tol: float = 1e-06, popsize: int = 15, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  genetic_algorithm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, population_size: int = 50, mutation_rate: float = 0.1, crossover_rate: float = 0.8, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  nelder_mead_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  particle_swarm_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], bounds: list[tuple[float, float]], maxiter: int = 100, n_particles: int = 30, w: float = 0.9, c1: float = 2.0, c2: float = 2.0, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  powell_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  slsqp_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, bounds: list[tuple[float, float]] | None = None, constraints: list[dict] | None = None, maxiter: int = 100, tol: float = 1e-06, **kwargs) -> tuple[numpy.ndarray, float, dict]
  [Func]  spsa_optimize(objective: collections.abc.Callable[[numpy.ndarray], float], initial_point: numpy.ndarray, maxiter: int = 100, tol: float = 1e-06, learning_rate: float = 0.1, perturbation_scale: float = 0.1, **kwargs) -> tuple[numpy.ndarray, float, dict]

--- Module: qpiai_quantum.algorithms.utils.visualize ---
  [Func]  plot_vqe_results_comprehensive(result, figsize=(16, 12))

--- Module: qpiai_quantum.algorithms.utils.visualize.visualize ---
  Doc: Comprehensive visualization suite for VQE results. | Provides multiple plot types for analyzing optimization convergence.
  [Func]  plot_comparison_multi_runs(results_dict, figsize=(14, 6))
  [Func]  plot_convergence_metrics(result, ax=None)
  [Func]  plot_energy_convergence(result, ax=None)
  [Func]  plot_energy_improvements(result, ax=None)
  [Func]  plot_measurement_distribution(result, ax=None, top_n=8)
  [Func]  plot_parameter_evolution(result, ax=None, max_params=6)
  [Func]  plot_parameter_heatmap(result, ax=None)
  [Func]  plot_parameter_trajectory_2d(result, param_indices=(0, 1), ax=None)
  [Func]  plot_rolling_statistics(result, ax=None, window=10)
  [Func]  plot_summary_statistics(result, ax=None)
  [Func]  plot_vqe_results_comprehensive(result, figsize=(16, 12))

--- Module: qpiai_quantum.applications ---

--- Module: qpiai_quantum.applications.chemistry ---
  [Class] FermionOperator(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
      .__init__(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
  [Class] MolecularDriver(self, geometry: str = 'H 0 0 0; H 0 0 0.735', basis: str = 'sto-3g', charge: int = 0, multiplicity: int = 1)
      .__init__(self, geometry: str = 'H 0 0 0; H 0 0 0.735', basis: str = 'sto-3g', charge: int = 0, multiplicity: int = 1)
      .run(self) -> qpiai_quantum.applications.chemistry.drivers.MolecularProperties
  [Class] MolecularProperties(self, n_electrons: int, n_orbitals: int, nuclear_repulsion_energy: float, hf_energy: float, hf_state: list[int], one_body_integrals: numpy.ndarray, two_body_integrals: numpy.ndarray) -> None
      .__init__(self, n_electrons: int, n_orbitals: int, nuclear_repulsion_energy: float, hf_energy: float, hf_state: list[int], one_body_integrals: numpy.ndarray, two_body_integrals: numpy.ndarray) -> None
      .get_fermionic_hamiltonian(self) -> qpiai_quantum.applications.chemistry.mappers.FermionOperator
  [Func]  bravyi_kitaev(fermion_op: qpiai_quantum.applications.chemistry.mappers.FermionOperator, n_qubits: int) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  jordan_wigner(fermion_op: qpiai_quantum.applications.chemistry.mappers.FermionOperator) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  uccsd_ansatz(n_qubits: 'int', n_electrons: 'int', mapping: 'str' = 'jordan_wigner') -> 'Circuit'

--- Module: qpiai_quantum.applications.chemistry.drivers ---
  [Class] FermionOperator(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
      .__init__(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
  [Class] MolecularDriver(self, geometry: str = 'H 0 0 0; H 0 0 0.735', basis: str = 'sto-3g', charge: int = 0, multiplicity: int = 1)
      .__init__(self, geometry: str = 'H 0 0 0; H 0 0 0.735', basis: str = 'sto-3g', charge: int = 0, multiplicity: int = 1)
      .run(self) -> qpiai_quantum.applications.chemistry.drivers.MolecularProperties
  [Class] MolecularProperties(self, n_electrons: int, n_orbitals: int, nuclear_repulsion_energy: float, hf_energy: float, hf_state: list[int], one_body_integrals: numpy.ndarray, two_body_integrals: numpy.ndarray) -> None
      .__init__(self, n_electrons: int, n_orbitals: int, nuclear_repulsion_energy: float, hf_energy: float, hf_state: list[int], one_body_integrals: numpy.ndarray, two_body_integrals: numpy.ndarray) -> None
      .get_fermionic_hamiltonian(self) -> qpiai_quantum.applications.chemistry.mappers.FermionOperator

--- Module: qpiai_quantum.applications.chemistry.mappers ---
  [Class] FermionOperator(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
      .__init__(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
  [Func]  bravyi_kitaev(fermion_op: qpiai_quantum.applications.chemistry.mappers.FermionOperator, n_qubits: int) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  jordan_wigner(fermion_op: qpiai_quantum.applications.chemistry.mappers.FermionOperator) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  multiply_paulis(pauli1: dict[int, str], coeff1: complex, pauli2: dict[int, str], coeff2: complex) -> tuple[dict[int, str], complex]

--- Module: qpiai_quantum.applications.chemistry.uccsd ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] FermionOperator(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
      .__init__(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
  [Class] OperationType(self, /, *args, **kwargs)
  [Func]  bravyi_kitaev(fermion_op: qpiai_quantum.applications.chemistry.mappers.FermionOperator, n_qubits: int) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  jordan_wigner(fermion_op: qpiai_quantum.applications.chemistry.mappers.FermionOperator) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  uccsd_ansatz(n_qubits: 'int', n_electrons: 'int', mapping: 'str' = 'jordan_wigner') -> 'Circuit'

--- Module: qpiai_quantum.applications.matter ---
  [Class] ChainLattice(self, n_sites: int)
      .__init__(self, n_sites: int)
      .get_edges(self, pbc: bool = False) -> list[tuple[int, int]]
  [Class] Lattice(self, /, *args, **kwargs)
      .get_edges(self, pbc: bool = False) -> list[tuple[int, int]]
  [Class] QITESolver(self, terms: list[tuple[list[tuple[int, str]], float]] | qpiai_quantum.applications.matter.models.QubitHamiltonian, n_qubits: int)
      .__init__(self, terms: list[tuple[list[tuple[int, str]], float]] | qpiai_quantum.applications.matter.models.QubitHamiltonian, n_qubits: int)
      .compute_ground_state(self, steps: int = 50, delta_tau: float = 0.1, initial_state: numpy.ndarray | None = None) -> tuple[float, numpy.ndarray]
  [Class] QubitHamiltonian(self, terms: list[tuple[list[tuple[int, str]], float]])
      .__init__(self, terms: list[tuple[list[tuple[int, str]], float]])
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
  [Class] SquareLattice(self, width: int, height: int)
      .__init__(self, width: int, height: int)
      .get_edges(self, pbc: bool = False) -> list[tuple[int, int]]
  [Func]  fermi_hubbard(lattice: qpiai_quantum.applications.matter.lattices.Lattice, t: float, U: float, pbc: bool = False, mapping: str = 'jordan_wigner') -> qpiai_quantum.applications.matter.models.QubitHamiltonian
  [Func]  heisenberg_hva_ansatz(lattice: 'Lattice', layers: 'int' = 1) -> 'Circuit'
  [Func]  heisenberg_xyz(lattice: qpiai_quantum.applications.matter.lattices.Lattice, Jx: float, Jy: float, Jz: float, h: float = 0.0, pbc: bool = False) -> qpiai_quantum.applications.matter.models.QubitHamiltonian
  [Func]  transverse_field_ising(lattice: qpiai_quantum.applications.matter.lattices.Lattice, J: float, g: float, pbc: bool = False) -> qpiai_quantum.applications.matter.models.QubitHamiltonian

--- Module: qpiai_quantum.applications.matter.ansatz ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] Lattice(self, /, *args, **kwargs)
      .get_edges(self, pbc: bool = False) -> list[tuple[int, int]]
  [Class] OperationType(self, /, *args, **kwargs)
  [Func]  heisenberg_hva_ansatz(lattice: 'Lattice', layers: 'int' = 1) -> 'Circuit'

--- Module: qpiai_quantum.applications.matter.lattices ---
  [Class] ChainLattice(self, n_sites: int)
      .__init__(self, n_sites: int)
      .get_edges(self, pbc: bool = False) -> list[tuple[int, int]]
  [Class] Lattice(self, /, *args, **kwargs)
      .get_edges(self, pbc: bool = False) -> list[tuple[int, int]]
  [Class] SquareLattice(self, width: int, height: int)
      .__init__(self, width: int, height: int)
      .get_edges(self, pbc: bool = False) -> list[tuple[int, int]]

--- Module: qpiai_quantum.applications.matter.models ---
  [Class] FermionOperator(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
      .__init__(self, terms: dict[tuple[tuple[int, int], ...], float | complex] | None = None)
  [Class] Lattice(self, /, *args, **kwargs)
      .get_edges(self, pbc: bool = False) -> list[tuple[int, int]]
  [Class] QubitHamiltonian(self, terms: list[tuple[list[tuple[int, str]], float]])
      .__init__(self, terms: list[tuple[list[tuple[int, str]], float]])
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  bravyi_kitaev(fermion_op: qpiai_quantum.applications.chemistry.mappers.FermionOperator, n_qubits: int) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  fermi_hubbard(lattice: qpiai_quantum.applications.matter.lattices.Lattice, t: float, U: float, pbc: bool = False, mapping: str = 'jordan_wigner') -> qpiai_quantum.applications.matter.models.QubitHamiltonian
  [Func]  heisenberg_xyz(lattice: qpiai_quantum.applications.matter.lattices.Lattice, Jx: float, Jy: float, Jz: float, h: float = 0.0, pbc: bool = False) -> qpiai_quantum.applications.matter.models.QubitHamiltonian
  [Func]  jordan_wigner(fermion_op: qpiai_quantum.applications.chemistry.mappers.FermionOperator) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  transverse_field_ising(lattice: qpiai_quantum.applications.matter.lattices.Lattice, J: float, g: float, pbc: bool = False) -> qpiai_quantum.applications.matter.models.QubitHamiltonian

--- Module: qpiai_quantum.applications.matter.qite ---
  [Class] QITESolver(self, terms: list[tuple[list[tuple[int, str]], float]] | qpiai_quantum.applications.matter.models.QubitHamiltonian, n_qubits: int)
      .__init__(self, terms: list[tuple[list[tuple[int, str]], float]] | qpiai_quantum.applications.matter.models.QubitHamiltonian, n_qubits: int)
      .compute_ground_state(self, steps: int = 50, delta_tau: float = 0.1, initial_state: numpy.ndarray | None = None) -> tuple[float, numpy.ndarray]
  [Class] QubitHamiltonian(self, terms: list[tuple[list[tuple[int, str]], float]])
      .__init__(self, terms: list[tuple[list[tuple[int, str]], float]])
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
  [Func]  hamiltonian_to_matrix(hamiltonian: list[tuple[list[tuple[int, str]], float]] | qpiai_quantum.applications.matter.models.QubitHamiltonian, n_qubits: int) -> numpy.ndarray

--- Module: qpiai_quantum.applications.optimization ---
  [Class] MaxCutProblem(self, graph: networkx.classes.graph.Graph)
      .__init__(self, graph: networkx.classes.graph.Graph)
      .compute_solution_quality(self, solution: dict[str, typing.Any]) -> dict[str, float]
      .decode_solution(self, bitstring: str) -> dict[str, typing.Any]
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
      .validate_solution(self, solution: dict[str, typing.Any]) -> tuple[bool, str]
  [Class] PortfolioOptimizationProblem(self, returns: numpy.ndarray, risk_matrix: numpy.ndarray, budget: float = 1.0, risk_tolerance: float = 1.0)
      .__init__(self, returns: numpy.ndarray, risk_matrix: numpy.ndarray, budget: float = 1.0, risk_tolerance: float = 1.0)
      .compute_solution_quality(self, solution: dict[str, typing.Any]) -> dict[str, float]
      .decode_solution(self, bitstring: str) -> dict[str, typing.Any]
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
      .validate_solution(self, solution: dict[str, typing.Any]) -> tuple[bool, str]

--- Module: qpiai_quantum.applications.optimization.problems ---
  [Class] MaxCutProblem(self, graph: networkx.classes.graph.Graph)
      .__init__(self, graph: networkx.classes.graph.Graph)
      .compute_solution_quality(self, solution: dict[str, typing.Any]) -> dict[str, float]
      .decode_solution(self, bitstring: str) -> dict[str, typing.Any]
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
      .validate_solution(self, solution: dict[str, typing.Any]) -> tuple[bool, str]
  [Class] OptimizationProblem(self)
      .__init__(self)
      .compute_solution_quality(self, solution: dict[str, typing.Any]) -> dict[str, float]
      .decode_solution(self, bitstring: str) -> dict[str, typing.Any]
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
      .validate_solution(self, solution: dict[str, typing.Any]) -> tuple[bool, str]
  [Class] PortfolioOptimizationProblem(self, returns: numpy.ndarray, risk_matrix: numpy.ndarray, budget: float = 1.0, risk_tolerance: float = 1.0)
      .__init__(self, returns: numpy.ndarray, risk_matrix: numpy.ndarray, budget: float = 1.0, risk_tolerance: float = 1.0)
      .compute_solution_quality(self, solution: dict[str, typing.Any]) -> dict[str, float]
      .decode_solution(self, bitstring: str) -> dict[str, typing.Any]
      .get_hamiltonian_terms(self) -> list[tuple[list[tuple[int, str]], float]]
      .validate_solution(self, solution: dict[str, typing.Any]) -> tuple[bool, str]

--- Module: qpiai_quantum.authentication ---
  [Class] AuthError(self, *message)
      .__init__(self, *message)
  [Class] QpiAIQuantumAuth(self, /, *args, **kwargs)
      .list_compute_resources(display: bool = True)
      .login(api_key: str | None) -> str
      .logout() -> str
      .me(api_key: str | None = None) -> dict
      .verify_api_key() -> bool

--- Module: qpiai_quantum.authentication.auth ---
  [Class] APIKeyEmptyError(self)
      .__init__(self)
  [Class] APIKeyInvalidError(self, message: str = 'The provided API key is not valid.')
      .__init__(self, message: str = 'The provided API key is not valid.')
  [Class] AuthError(self, *message)
      .__init__(self, *message)
  [Class] QpiAIQuantumAuth(self, /, *args, **kwargs)
      .list_compute_resources(display: bool = True)
      .login(api_key: str | None) -> str
      .logout() -> str
      .me(api_key: str | None = None) -> dict
      .verify_api_key() -> bool
  [Class] SDKUser(self, name: str, email: str, api_key: str) -> None
      .__init__(self, name: str, email: str, api_key: str) -> None
  [Class] UserNotFoundError(self)
      .__init__(self)
  [Func]  clear_user() -> None
  [Func]  get_active_api_key() -> str | None
  [Func]  get_api_url(endpoint: str) -> str
  [Func]  get_user() -> qpiai_quantum.authentication.user.SDKUser | None
  [Func]  normalize_api_key(api_key: str | None) -> str | None
  [Func]  set_user(user_data: qpiai_quantum.authentication.user.SDKUser | str) -> None

--- Module: qpiai_quantum.authentication.exceptions ---
  [Class] APIKeyEmptyError(self)
      .__init__(self)
  [Class] APIKeyExpiredError(self)
      .__init__(self)
  [Class] APIKeyInvalidError(self, message: str = 'The provided API key is not valid.')
      .__init__(self, message: str = 'The provided API key is not valid.')
  [Class] APIKeyRevokedError(self)
      .__init__(self)
  [Class] AuthError(self, *message)
      .__init__(self, *message)
  [Class] BaseError(self, *message)
      .__init__(self, *message)
  [Class] UserNotFoundError(self)
      .__init__(self)

--- Module: qpiai_quantum.authentication.user ---
  [Class] APIKeyInvalidError(self, message: str = 'The provided API key is not valid.')
      .__init__(self, message: str = 'The provided API key is not valid.')
  [Class] SDKUser(self, name: str, email: str, api_key: str) -> None
      .__init__(self, name: str, email: str, api_key: str) -> None
  [Func]  clear_user() -> None
  [Func]  get_active_api_key() -> str | None
  [Func]  get_active_auth_header() -> dict[str, str] | None
  [Func]  get_user() -> qpiai_quantum.authentication.user.SDKUser | None
  [Func]  normalize_api_key(api_key: str | None) -> str | None
  [Func]  resolve_api_key(api_key: str | None = None) -> str | None
  [Func]  set_user(user_data: qpiai_quantum.authentication.user.SDKUser | str) -> None
  [Func]  user_context(api_key: str)

--- Module: qpiai_quantum.circuit ---
  [Class] Bit(self, register: qpiai_quantum.circuit.register.Register, index: int)
      .__init__(self, register: qpiai_quantum.circuit.register.Register, index: int)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] ClBit(self, register, index)
      .__init__(self, register, index)
      .to_json(self)
  [Class] ClassicalRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] QuantumRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] Qubit(self, register, index)
      .__init__(self, register, index)
      .to_json(self)
  [Class] RandomCircuitGenerator(self, num_qubits: int, depth: int, max_gates: int | None = None, allow_parametric: bool = True, single_qubit_gates: list[str] | None = None, parametric_single_qubit_gates: list[str] | None = None, two_qubit_gates: list[str] | None = None, parametric_two_qubit_gates: list[str] | None = None, three_qubit_gates: list[str] | None = None, add_measurements: bool = True, single_qubit_probability: float = 0.6, two_qubit_probability: float = 0.3, parametric_probability: float = 0.3)
      .__init__(self, num_qubits: int, depth: int, max_gates: int | None = None, allow_parametric: bool = True, single_qubit_gates: list[str] | None = None, parametric_single_qubit_gates: list[str] | None = None, two_qubit_gates: list[str] | None = None, parametric_two_qubit_gates: list[str] | None = None, three_qubit_gates: list[str] | None = None, add_measurements: bool = True, single_qubit_probability: float = 0.6, two_qubit_probability: float = 0.3, parametric_probability: float = 0.3)
      .generate(self) -> qpiai_quantum.circuit.circuit.Circuit
  [Class] Register(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)

--- Module: qpiai_quantum.circuit.circuit ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] CircuitError(self, *message)
      .__init__(self, *message)
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ClassicalRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] IntermediateCircuitRepresentation(self, *registers, name, metadata)
      .__init__(self, *registers, name, metadata)
      .to_json(self)
  [Class] OperationType(self, /, *args, **kwargs)
  [Class] QuantumRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] Register(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
  [Class] StatevectorSimulator(self, /, *args, **kwargs)
      .run(self, circuit: 'Circuit', shots: int = 1024, seed: int | None = None, name: str | None = None, initial_state: numpy.ndarray | None = None) -> qpiai_quantum.simulator.result.QasmSimulatorResult

--- Module: qpiai_quantum.circuit.classicalregister ---
  [Class] Bit(self, register: qpiai_quantum.circuit.register.Register, index: int)
      .__init__(self, register: qpiai_quantum.circuit.register.Register, index: int)
  [Class] CircuitError(self, *message)
      .__init__(self, *message)
  [Class] ClBit(self, register, index)
      .__init__(self, register, index)
      .to_json(self)
  [Class] ClassicalRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] Register(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)

--- Module: qpiai_quantum.circuit.exceptions ---
  [Class] BaseError(self, *message)
      .__init__(self, *message)
  [Class] CircuitError(self, *message)
      .__init__(self, *message)
  [Class] DuplicateQubitError(self, message: str = 'Duplicate qubits are not allowed in the input.')
      .__init__(self, message: str = 'Duplicate qubits are not allowed in the input.')
  [Class] InvalidCircuitArgumentError(self, message: str = 'Invalid arguments for Circuit initialization.')
      .__init__(self, message: str = 'Invalid arguments for Circuit initialization.')
  [Class] InvalidRegisterNameError(self, message: str = 'Register name must be a non-empty string.')
      .__init__(self, message: str = 'Register name must be a non-empty string.')
  [Class] InvalidRegisterSizeError(self, message: str = 'Size of a register must be a positive integer.')
      .__init__(self, message: str = 'Size of a register must be a positive integer.')
  [Class] MeasurementError(self, message: str = 'Circuit contains measurement operations.')
      .__init__(self, message: str = 'Circuit contains measurement operations.')
  [Class] RegisterError(self, *message)
      .__init__(self, *message)

--- Module: qpiai_quantum.circuit.quantumregister ---
  [Class] Bit(self, register: qpiai_quantum.circuit.register.Register, index: int)
      .__init__(self, register: qpiai_quantum.circuit.register.Register, index: int)
  [Class] CircuitError(self, *message)
      .__init__(self, *message)
  [Class] QuantumRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] Qubit(self, register, index)
      .__init__(self, register, index)
      .to_json(self)
  [Class] Register(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)

--- Module: qpiai_quantum.circuit.random_circuit_generator ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] RandomCircuitGenerator(self, num_qubits: int, depth: int, max_gates: int | None = None, allow_parametric: bool = True, single_qubit_gates: list[str] | None = None, parametric_single_qubit_gates: list[str] | None = None, two_qubit_gates: list[str] | None = None, parametric_two_qubit_gates: list[str] | None = None, three_qubit_gates: list[str] | None = None, add_measurements: bool = True, single_qubit_probability: float = 0.6, two_qubit_probability: float = 0.3, parametric_probability: float = 0.3)
      .__init__(self, num_qubits: int, depth: int, max_gates: int | None = None, allow_parametric: bool = True, single_qubit_gates: list[str] | None = None, parametric_single_qubit_gates: list[str] | None = None, two_qubit_gates: list[str] | None = None, parametric_two_qubit_gates: list[str] | None = None, three_qubit_gates: list[str] | None = None, add_measurements: bool = True, single_qubit_probability: float = 0.6, two_qubit_probability: float = 0.3, parametric_probability: float = 0.3)
      .generate(self) -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.circuit.register ---
  [Class] Bit(self, register: qpiai_quantum.circuit.register.Register, index: int)
      .__init__(self, register: qpiai_quantum.circuit.register.Register, index: int)
  [Class] CircuitError(self, *message)
      .__init__(self, *message)
  [Class] Register(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)

--- Module: qpiai_quantum.circuitmanager ---
  [Class] CircuitManager(self, /, *args, **kwargs)
      .generate_name() -> str
      .save(name: str = None)

--- Module: qpiai_quantum.circuitmanager.circuit_manager ---
  [Class] CircuitManager(self, /, *args, **kwargs)
      .generate_name() -> str
      .save(name: str = None)

--- Module: qpiai_quantum.config ---
  Doc: QPIAI Quantum SDK Configuration Module |  | This module provides centralized configuration management for the QPIAI Quantum SDK,
  [Func]  get_api_url(endpoint: str) -> str
  [Func]  get_server_url() -> str
  [Func]  get_sse_url(job_id: str) -> str

--- Module: qpiai_quantum.creditestimator ---
  Doc: Client for QpiAI's hosted credit-estimator service.
  [Class] CreditEstimator(self, api_key: str | None = None, base_url: str | None = None, timeout: float | tuple[float, float] = (10, 120), session: requests.sessions.Session | None = None) -> None
      .__init__(self, api_key: str | None = None, base_url: str | None = None, timeout: float | tuple[float, float] = (10, 120), session: requests.sessions.Session | None = None) -> None
      .estimate_for_device(self, qasm: str, device_name: str) -> dict[str, typing.Any]
      .estimate_for_resource(self, qasm: str, compute_resource_id: str) -> dict[str, typing.Any]
  [Class] CreditEstimatorError(self, message: str, status_code: int | None = None) -> None
      .__init__(self, message: str, status_code: int | None = None) -> None

--- Module: qpiai_quantum.creditestimator.client ---
  Doc: Client for QpiAI's hosted credit-estimation API.
  [Class] CreditEstimator(self, api_key: str | None = None, base_url: str | None = None, timeout: float | tuple[float, float] = (10, 120), session: requests.sessions.Session | None = None) -> None
      .__init__(self, api_key: str | None = None, base_url: str | None = None, timeout: float | tuple[float, float] = (10, 120), session: requests.sessions.Session | None = None) -> None
      .estimate_for_device(self, qasm: str, device_name: str) -> dict[str, typing.Any]
      .estimate_for_resource(self, qasm: str, compute_resource_id: str) -> dict[str, typing.Any]
  [Class] CreditEstimatorError(self, message: str, status_code: int | None = None) -> None
      .__init__(self, message: str, status_code: int | None = None) -> None
  [Func]  get_api_url(endpoint: str) -> str
  [Func]  resolve_api_key(api_key: str | None = None) -> str | None

--- Module: qpiai_quantum.exceptions ---
  [Class] BaseError(self, *message)
      .__init__(self, *message)

--- Module: qpiai_quantum.formalism ---
  [Class] DensityMatrix(self, state: list[list[complex]] | numpy.ndarray)
      .ADC(self, param: float)
      .__init__(self, state: list[list[complex]] | numpy.ndarray)
      .basis_operators(argument: int)
      .check(density_matrix: 'DensityMatrix', verbose: bool = False) -> bool
      .check_MUB(a: list[numpy.ndarray], b: list[numpy.ndarray], verbose: bool = False) -> bool
      .concurrence(self) -> float
      .correlation_points(self, state: numpy.ndarray)
      .depol(self, param: float)
      .distinguishability(self, X, *varargin)
      .entangling_power_2q(U: numpy.ndarray)
      .eof(self)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .gate_expand_2_to_n(U, N, control=None, target=None, targets=None)
      .get_state(self) -> numpy.ndarray
      .has_symmetric_extension(self)
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .kraus(self, operator: list[numpy.ndarray])
      .l1_norm(self) -> float
      .max_bell_value(self)
      .partial_trace(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .partial_transpose(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .plot_correlation_space_2q(self, p_adc=False, p_depol=False)
      .purity(self) -> float
      .relative_entropy_coherence(self) -> float
      .reyni(self, base: float = 2, alpha: float = 1)
      .schmidt_rank(self)
      .show(self)
      .swap(N=None, targets=[0, 1])
      .teleportation_fidelity(self)
      .tensor_product(*args)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] RandomStateGenerator(self, /, *args, **kwargs)
      .generate(mixedness: float, seed: float)
      .wishart(n: int, s: int, seed: float)
  [Class] SpecialStates(self, /, *args, **kwargs)
      .haar_random_state(number_of_qubits: int, seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .isotropic_state(seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .mems(seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .werner_state(seed: float) -> tuple[qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix, list[float]]

--- Module: qpiai_quantum.formalism.density_matrix ---
  [Class] DensityMatrix(self, state: list[list[complex]] | numpy.ndarray)
      .ADC(self, param: float)
      .__init__(self, state: list[list[complex]] | numpy.ndarray)
      .basis_operators(argument: int)
      .check(density_matrix: 'DensityMatrix', verbose: bool = False) -> bool
      .check_MUB(a: list[numpy.ndarray], b: list[numpy.ndarray], verbose: bool = False) -> bool
      .concurrence(self) -> float
      .correlation_points(self, state: numpy.ndarray)
      .depol(self, param: float)
      .distinguishability(self, X, *varargin)
      .entangling_power_2q(U: numpy.ndarray)
      .eof(self)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .gate_expand_2_to_n(U, N, control=None, target=None, targets=None)
      .get_state(self) -> numpy.ndarray
      .has_symmetric_extension(self)
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .kraus(self, operator: list[numpy.ndarray])
      .l1_norm(self) -> float
      .max_bell_value(self)
      .partial_trace(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .partial_transpose(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .plot_correlation_space_2q(self, p_adc=False, p_depol=False)
      .purity(self) -> float
      .relative_entropy_coherence(self) -> float
      .reyni(self, base: float = 2, alpha: float = 1)
      .schmidt_rank(self)
      .show(self)
      .swap(N=None, targets=[0, 1])
      .teleportation_fidelity(self)
      .tensor_product(*args)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] RandomStateGenerator(self, /, *args, **kwargs)
      .generate(mixedness: float, seed: float)
      .wishart(n: int, s: int, seed: float)
  [Class] SpecialStates(self, /, *args, **kwargs)
      .haar_random_state(number_of_qubits: int, seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .isotropic_state(seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .mems(seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .werner_state(seed: float) -> tuple[qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix, list[float]]

--- Module: qpiai_quantum.formalism.density_matrix.base_density_matrix ---
  Doc: Base Density Matrix Class |  | Provides common functionality shared between different DensityMatrix implementations:
  [Class] BaseDensityMatrix(self, /, *args, **kwargs)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .partial_trace(self, qubits_to_keep: list, dims: list | None = None) -> numpy.ndarray
      .purity(self) -> float
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float

--- Module: qpiai_quantum.formalism.density_matrix.density_matrix ---
  [Class] BaseDensityMatrix(self, /, *args, **kwargs)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .partial_trace(self, qubits_to_keep: list, dims: list | None = None) -> numpy.ndarray
      .purity(self) -> float
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] DensityMatrix(self, state: list[list[complex]] | numpy.ndarray)
      .ADC(self, param: float)
      .__init__(self, state: list[list[complex]] | numpy.ndarray)
      .basis_operators(argument: int)
      .check(density_matrix: 'DensityMatrix', verbose: bool = False) -> bool
      .check_MUB(a: list[numpy.ndarray], b: list[numpy.ndarray], verbose: bool = False) -> bool
      .concurrence(self) -> float
      .correlation_points(self, state: numpy.ndarray)
      .depol(self, param: float)
      .distinguishability(self, X, *varargin)
      .entangling_power_2q(U: numpy.ndarray)
      .eof(self)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .gate_expand_2_to_n(U, N, control=None, target=None, targets=None)
      .get_state(self) -> numpy.ndarray
      .has_symmetric_extension(self)
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .kraus(self, operator: list[numpy.ndarray])
      .l1_norm(self) -> float
      .max_bell_value(self)
      .partial_trace(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .partial_transpose(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .plot_correlation_space_2q(self, p_adc=False, p_depol=False)
      .purity(self) -> float
      .relative_entropy_coherence(self) -> float
      .reyni(self, base: float = 2, alpha: float = 1)
      .schmidt_rank(self)
      .show(self)
      .swap(N=None, targets=[0, 1])
      .teleportation_fidelity(self)
      .tensor_product(*args)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] DensityMatrixException(self, *message)
      .__init__(self, *message)

--- Module: qpiai_quantum.formalism.density_matrix.exceptions ---
  [Class] BaseError(self, *message)
      .__init__(self, *message)
  [Class] DensityMatrixException(self, *message)
      .__init__(self, *message)

--- Module: qpiai_quantum.formalism.density_matrix.random_state_generator ---
  [Class] DensityMatrix(self, state: list[list[complex]] | numpy.ndarray)
      .ADC(self, param: float)
      .__init__(self, state: list[list[complex]] | numpy.ndarray)
      .basis_operators(argument: int)
      .check(density_matrix: 'DensityMatrix', verbose: bool = False) -> bool
      .check_MUB(a: list[numpy.ndarray], b: list[numpy.ndarray], verbose: bool = False) -> bool
      .concurrence(self) -> float
      .correlation_points(self, state: numpy.ndarray)
      .depol(self, param: float)
      .distinguishability(self, X, *varargin)
      .entangling_power_2q(U: numpy.ndarray)
      .eof(self)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .gate_expand_2_to_n(U, N, control=None, target=None, targets=None)
      .get_state(self) -> numpy.ndarray
      .has_symmetric_extension(self)
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .kraus(self, operator: list[numpy.ndarray])
      .l1_norm(self) -> float
      .max_bell_value(self)
      .partial_trace(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .partial_transpose(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .plot_correlation_space_2q(self, p_adc=False, p_depol=False)
      .purity(self) -> float
      .relative_entropy_coherence(self) -> float
      .reyni(self, base: float = 2, alpha: float = 1)
      .schmidt_rank(self)
      .show(self)
      .swap(N=None, targets=[0, 1])
      .teleportation_fidelity(self)
      .tensor_product(*args)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] RandomStateGenerator(self, /, *args, **kwargs)
      .generate(mixedness: float, seed: float)
      .wishart(n: int, s: int, seed: float)

--- Module: qpiai_quantum.formalism.density_matrix.states ---
  [Class] DensityMatrix(self, state: list[list[complex]] | numpy.ndarray)
      .ADC(self, param: float)
      .__init__(self, state: list[list[complex]] | numpy.ndarray)
      .basis_operators(argument: int)
      .check(density_matrix: 'DensityMatrix', verbose: bool = False) -> bool
      .check_MUB(a: list[numpy.ndarray], b: list[numpy.ndarray], verbose: bool = False) -> bool
      .concurrence(self) -> float
      .correlation_points(self, state: numpy.ndarray)
      .depol(self, param: float)
      .distinguishability(self, X, *varargin)
      .entangling_power_2q(U: numpy.ndarray)
      .eof(self)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .gate_expand_2_to_n(U, N, control=None, target=None, targets=None)
      .get_state(self) -> numpy.ndarray
      .has_symmetric_extension(self)
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .kraus(self, operator: list[numpy.ndarray])
      .l1_norm(self) -> float
      .max_bell_value(self)
      .partial_trace(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .partial_transpose(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .plot_correlation_space_2q(self, p_adc=False, p_depol=False)
      .purity(self) -> float
      .relative_entropy_coherence(self) -> float
      .reyni(self, base: float = 2, alpha: float = 1)
      .schmidt_rank(self)
      .show(self)
      .swap(N=None, targets=[0, 1])
      .teleportation_fidelity(self)
      .tensor_product(*args)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] DensityMatrixException(self, *message)
      .__init__(self, *message)
  [Class] SpecialStates(self, /, *args, **kwargs)
      .haar_random_state(number_of_qubits: int, seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .isotropic_state(seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .mems(seed: float) -> qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix
      .werner_state(seed: float) -> tuple[qpiai_quantum.formalism.density_matrix.density_matrix.DensityMatrix, list[float]]

--- Module: qpiai_quantum.icr ---
  [Class] BarrierOperation(self, *qubits: int | list[int])
      .__init__(self, *qubits: int | list[int])
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CCXGate(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .__init__(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CHGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CPGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CRXGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CRYGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CRZGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CSGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CSwapGate(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .__init__(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CXGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CYGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CZGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CustomControlOperation(self, *control: int, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .__init__(self, *control: int, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ECRGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] HGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] IDGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ISwapDGGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] IntermediateCircuitRepresentation(self, *registers, name, metadata)
      .__init__(self, *registers, name, metadata)
      .to_json(self)
  [Class] MeasureOperation(self, qubit: int, clbit: int)
      .__init__(self, qubit: int, clbit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] Operation(self, name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None)
      .__init__(self, name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] PGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RXGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RXXGate(self, qubit1: int, qubit2: int, theta: float)
      .__init__(self, qubit1: int, qubit2: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RYGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RYYGate(self, qubit1: int, qubit2: int, theta: float)
      .__init__(self, qubit1: int, qubit2: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RZGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RZZGate(self, qubit1: int, qubit2: int, theta: float)
      .__init__(self, qubit1: int, qubit2: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SDGGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SXDGGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SXGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SwapGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] TDGGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] TGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] UGate(self, qubit: int, theta: float, phi: float, lam: float)
      .__init__(self, qubit: int, theta: float, phi: float, lam: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] XGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] YGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ZGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]

--- Module: qpiai_quantum.icr.circuitevolution ---
  [Class] CircuitEvolutionList(self)
      .__init__(self)
      .append(self, operation)
      .append_to_head(self, operation)
      .append_to_tail(self, operation)
      .pop(self)
      .pop_head(self)
      .pop_tail(self)
  [Class] EvolutionNode(self, operation=None, prev=None, next=None)
      .__init__(self, operation=None, prev=None, next=None)

--- Module: qpiai_quantum.icr.circuitoperation ---
  [Class] BarrierOperation(self, *qubits: int | list[int])
      .__init__(self, *qubits: int | list[int])
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CCXGate(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .__init__(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CHGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CPGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CRXGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CRYGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CRZGate(self, control_qubit: int, target_qubit: int, theta: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CSDGGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CSGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CSwapGate(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .__init__(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CUGate(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float)
      .__init__(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CXGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CYGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CZGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] DCXGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ECRGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] HGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] IDGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ISwapDGGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ISwapGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] MCXGate(self, control_qubits: list[int], target_qubit: int)
      .__init__(self, control_qubits: list[int], target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] MeasureOperation(self, qubit: int, clbit: int)
      .__init__(self, qubit: int, clbit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] Operation(self, name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None)
      .__init__(self, name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] OperationType(self, /, *args, **kwargs)
  [Class] PGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RCCXGate(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .__init__(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RXGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RXXGate(self, qubit1: int, qubit2: int, theta: float)
      .__init__(self, qubit1: int, qubit2: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RYGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RYYGate(self, qubit1: int, qubit2: int, theta: float)
      .__init__(self, qubit1: int, qubit2: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RZGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] RZZGate(self, qubit1: int, qubit2: int, theta: float)
      .__init__(self, qubit1: int, qubit2: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ResetOperation(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SDGGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SXDGGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SXGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] SwapGate(self, qubit1: int, qubit2: int)
      .__init__(self, qubit1: int, qubit2: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] TDGGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] TGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] U2Gate(self, qubit: int, phi: float, lam: float)
      .__init__(self, qubit: int, phi: float, lam: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] UGate(self, qubit: int, theta: float, phi: float, lam: float)
      .__init__(self, qubit: int, theta: float, phi: float, lam: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] XGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] YGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ZGate(self, qubit: int)
      .__init__(self, qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Func]  validate_index(value: int) -> int
  [Func]  validate_parameter(value: float) -> float

--- Module: qpiai_quantum.icr.decomposition ---
  Doc: Shared exact definitions for gates expressed as smaller operations. |  | Definitions preserve the full unitary, including scalar phase. Simulation,
  [Class] CXGate(self, control_qubit: int, target_qubit: int)
      .__init__(self, control_qubit: int, target_qubit: int)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] PGate(self, qubit: int, theta: float)
      .__init__(self, qubit: int, theta: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] U2Gate(self, qubit: int, phi: float, lam: float)
      .__init__(self, qubit: int, phi: float, lam: float)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Func]  gate_decomposition(name: str, qubits: list[int], params: list[float] | None = None) -> list[qpiai_quantum.icr.circuitoperation.CircuitOperation] | None

--- Module: qpiai_quantum.icr.icr ---
  [Class] CircuitEvolutionList(self)
      .__init__(self)
      .append(self, operation)
      .append_to_head(self, operation)
      .append_to_tail(self, operation)
      .pop(self)
      .pop_head(self)
      .pop_tail(self)
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] ClassicalRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)
  [Class] IntermediateCircuitRepresentation(self, *registers, name, metadata)
      .__init__(self, *registers, name, metadata)
      .to_json(self)
  [Class] QuantumRegister(self, size: int, name: str = None)
      .__init__(self, size: int, name: str = None)
      .to_json(self)

--- Module: qpiai_quantum.icr.operationmodifiers ---
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] CustomControlOperation(self, *control: int, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .__init__(self, *control: int, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Class] OperationType(self, /, *args, **kwargs)
  [Func]  validate_index(value: int) -> int

--- Module: qpiai_quantum.icr.validation ---
  Doc: Shared validation for circuit operations and numerical execution.
  [Func]  validate_index(value: int) -> int
  [Func]  validate_parameter(value: float) -> float

--- Module: qpiai_quantum.iem ---
  [Class] QASM2(self, /, *args, **kwargs)
      .generate(circuit: qpiai_quantum.circuit.circuit.Circuit) -> str

--- Module: qpiai_quantum.iem.qasm ---
  [Class] QASM2(self, /, *args, **kwargs)
      .generate(circuit: qpiai_quantum.circuit.circuit.Circuit) -> str

--- Module: qpiai_quantum.iem.qasm.primitives ---
  Doc: Exact, ancilla-free lowering to the portable U3/CX gate basis. |  | Every emitted phase is retained, including phases that become relative phases
  [Func]  gate_decomposition(name: str, qubits: list[int], params: list[float] | None = None) -> list[qpiai_quantum.icr.circuitoperation.CircuitOperation] | None
  [Func]  lower_operation(operation: Any) -> list[tuple[str, list[float], list[int]]]
  [Func]  validate_parameter(value: float) -> float

--- Module: qpiai_quantum.iem.qasm.v2 ---
  [Class] QASM2(self, /, *args, **kwargs)
      .generate(circuit: qpiai_quantum.circuit.circuit.Circuit) -> str

--- Module: qpiai_quantum.iem.qasm.v2.exceptions ---
  [Class] BaseError(self, *message)
      .__init__(self, *message)
  [Class] Qasm2Error(self, *message)
      .__init__(self, *message)

--- Module: qpiai_quantum.iem.qasm.v2.exporter ---
  Doc: Self-contained OpenQASM 2 export in the portable U3/CX basis.
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] QASM2(self, /, *args, **kwargs)
      .generate(circuit: qpiai_quantum.circuit.circuit.Circuit) -> str
  [Func]  lower_operation(operation: Any) -> list[tuple[str, list[float], list[int]]]

--- Module: qpiai_quantum.jobmanager ---
  Doc: QPIAI Quantum SDK Job Manager |  | This module provides job lifecycle management functionality for quantum circuit execution,
  [Class] Backend(self, /, *args, **kwargs)
  [Class] ExecutionEngine(self, /, *args, **kwargs)
      .execute_circuit(circuit: 'Circuit', shots: int = 1024, need_statevector: bool = False, need_density_matrix: bool = False, experiment_name: str | None = None, circuit_name: str | None = None, access_token: str | None = None, overwrite: bool = True, timeout: int = 300, method: str = 'statevector', device_name: str = 'QpiAI-QSV-Local', **kwargs) -> 'JobResult'
  [Class] JobManager(self, /, *args, **kwargs)
      .cancel_job(self, job_id: str) -> dict[str, typing.Any]
      .clear_resource_cache()
      .delete_job(self, job_id: str) -> dict[str, typing.Any]
      .get_current_job(self) -> dict[str, Any] | None
      .get_experiment_id_by_name(self, experiment_name: str) -> str
      .get_job_history(self, period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(self, job_id: str, device_name: str | None = None) -> 'JobResult'
      .get_job_status(self, job_id: str) -> dict[str, Any] | None
      .list_compute_resources(self) -> list[dict[str, typing.Any]]
      .submit_and_wait_for_results_qasm(self, qasm_string_or_circuit: str | qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False, use_events: bool = True, timeout: int = 300) -> qpiai_quantum.jobmanager.job_result.JobResult
      .submit_circuit_job(self, circuit: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str | None = None, compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .submit_qasm_job(self, qasm_string: str, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .track_job(func, job_name: str)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] ResolvedBackend(self, ID: str, backend_name: str, address: str, health_check: str, run: str) -> None
      .__init__(self, ID: str, backend_name: str, address: str, health_check: str, run: str) -> None
  [Class] SSEResultHandler(self, device_name: str | None = None, timeout: int = 300)
      .__init__(self, device_name: str | None = None, timeout: int = 300)
      .get_error(self) -> str | None
      .get_result(self) -> dict | None
      .wait_for_events(self, url: str, headers: dict) -> bool

--- Module: qpiai_quantum.jobmanager.backend ---
  [Class] Backend(self, /, *args, **kwargs)
  [Class] ResolvedBackend(self, ID: str, backend_name: str, address: str, health_check: str, run: str) -> None
      .__init__(self, ID: str, backend_name: str, address: str, health_check: str, run: str) -> None

--- Module: qpiai_quantum.jobmanager.exceptions ---
  [Class] AuthenticationError(self, message: str = 'No API key found in the current user context. Please login using QpiAIQuantumAuth.login(...).')
      .__init__(self, message: str = 'No API key found in the current user context. Please login using QpiAIQuantumAuth.login(...).')
  [Class] BaseError(self, *message)
      .__init__(self, *message)
  [Class] CircuitError(self, *message)
      .__init__(self, *message)
  [Class] CircuitNotFoundError(self, circuit_name: str)
      .__init__(self, circuit_name: str)
  [Class] CircuitUpdateError(self, error: Exception)
      .__init__(self, error: Exception)
  [Class] ExperimentError(self, *message)
      .__init__(self, *message)
  [Class] ExperimentNotFoundError(self, experiment_name: str)
      .__init__(self, experiment_name: str)
  [Class] InvalidExperimentResponseError(self, message: str = 'Invalid response from experiments API: missing experiment_id')
      .__init__(self, message: str = 'Invalid response from experiments API: missing experiment_id')
  [Class] InvalidResponseError(self, *message)
      .__init__(self, *message)
  [Class] JobManagerError(self, *message)
      .__init__(self, *message)
  [Class] JobStatusError(self, job_id: str, error: Exception)
      .__init__(self, job_id: str, error: Exception)
  [Class] JobSubmissionError(self, message: str = 'Job submission failed: no job ID found in response')
      .__init__(self, message: str = 'Job submission failed: no job ID found in response')

--- Module: qpiai_quantum.jobmanager.execution_engine ---
  [Class] ExecutionEngine(self, /, *args, **kwargs)
      .execute_circuit(circuit: 'Circuit', shots: int = 1024, need_statevector: bool = False, need_density_matrix: bool = False, experiment_name: str | None = None, circuit_name: str | None = None, access_token: str | None = None, overwrite: bool = True, timeout: int = 300, method: str = 'statevector', device_name: str = 'QpiAI-QSV-Local', **kwargs) -> 'JobResult'

--- Module: qpiai_quantum.jobmanager.job_result ---
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] JobExecutionResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)

--- Module: qpiai_quantum.jobmanager.jobmanager ---
  [Class] AuthenticationError(self, message: str = 'No API key found in the current user context. Please login using QpiAIQuantumAuth.login(...).')
      .__init__(self, message: str = 'No API key found in the current user context. Please login using QpiAIQuantumAuth.login(...).')
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] CircuitNotFoundError(self, circuit_name: str)
      .__init__(self, circuit_name: str)
  [Class] CircuitUpdateError(self, error: Exception)
      .__init__(self, error: Exception)
  [Class] ContractValidationError(self, /, *args, **kwargs)
  [Class] ExperimentNotFoundError(self, experiment_name: str)
      .__init__(self, experiment_name: str)
  [Class] IntermediateCircuitRepresentation(self, *registers, name, metadata)
      .__init__(self, *registers, name, metadata)
      .to_json(self)
  [Class] InvalidExperimentResponseError(self, message: str = 'Invalid response from experiments API: missing experiment_id')
      .__init__(self, message: str = 'Invalid response from experiments API: missing experiment_id')
  [Class] InvalidResponseError(self, *message)
      .__init__(self, *message)
  [Class] JobManager(self, /, *args, **kwargs)
      .cancel_job(self, job_id: str) -> dict[str, typing.Any]
      .clear_resource_cache()
      .delete_job(self, job_id: str) -> dict[str, typing.Any]
      .get_current_job(self) -> dict[str, Any] | None
      .get_experiment_id_by_name(self, experiment_name: str) -> str
      .get_job_history(self, period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(self, job_id: str, device_name: str | None = None) -> 'JobResult'
      .get_job_status(self, job_id: str) -> dict[str, Any] | None
      .list_compute_resources(self) -> list[dict[str, typing.Any]]
      .submit_and_wait_for_results_qasm(self, qasm_string_or_circuit: str | qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False, use_events: bool = True, timeout: int = 300) -> qpiai_quantum.jobmanager.job_result.JobResult
      .submit_circuit_job(self, circuit: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str | None = None, compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .submit_qasm_job(self, qasm_string: str, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .track_job(func, job_name: str)
  [Class] JobManagerError(self, *message)
      .__init__(self, *message)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] JobStatusError(self, job_id: str, error: Exception)
      .__init__(self, job_id: str, error: Exception)
  [Class] JobSubmissionError(self, message: str = 'Job submission failed: no job ID found in response')
      .__init__(self, message: str = 'Job submission failed: no job ID found in response')
  [Class] SSEResultHandler(self, device_name: str | None = None, timeout: int = 300)
      .__init__(self, device_name: str | None = None, timeout: int = 300)
      .get_error(self) -> str | None
      .get_result(self) -> dict | None
      .wait_for_events(self, url: str, headers: dict) -> bool
  [Func]  decode_density_matrix(density_matrix: object) -> list[list[complex]] | None
  [Func]  decode_statevector(statevector: object) -> list[list[complex]] | None
  [Func]  get_active_auth_header() -> dict[str, str] | None
  [Func]  get_api_url(endpoint: str) -> str
  [Func]  get_sse_url(job_id: str) -> str
  [Func]  validate_binary_manifest(raw_size: 'int', manifest: 'object') -> 'tuple[dict[str, int] | None, float, tuple[BinaryArtifactDescriptor, ...]]'

--- Module: qpiai_quantum.jobmanager.result_contract ---
  Doc: Dependency-free validation for simulator result transport contracts.
  [Class] BinaryArtifactDescriptor(self, result_type: 'str', shape: 'tuple[int, ...]', offset_bytes: 'int', size_bytes: 'int') -> None
      .__init__(self, result_type: 'str', shape: 'tuple[int, ...]', offset_bytes: 'int', size_bytes: 'int') -> None
  [Class] ContractValidationError(self, /, *args, **kwargs)
  [Class] JSONComplex(self, /, *args, **kwargs)
  [Func]  decode_density_matrix_contract(density_matrix: 'object') -> 'DensityMatrixData | None'
  [Func]  decode_statevector_contract(statevector: 'object') -> 'StatevectorData | None'
  [Func]  extract_json_result_data(response: 'object') -> 'dict[str, object]'
  [Func]  validate_binary_manifest(raw_size: 'int', manifest: 'object') -> 'tuple[dict[str, int] | None, float, tuple[BinaryArtifactDescriptor, ...]]'
  [Func]  validate_binary_response(raw_bytes: 'bytes', manifest: 'object', required_artifacts: 'set[str]') -> 'tuple[BinaryArtifactDescriptor, ...]'
  [Func]  validate_json_response(response: 'object', required_artifacts: 'set[str]') -> 'dict[str, object]'

--- Module: qpiai_quantum.jobmanager.result_decoding ---
  Doc: Decode JSON-safe quantum result artifacts into typed numeric values.
  [Class] ContractValidationError(self, /, *args, **kwargs)
  [Class] InvalidResponseError(self, *message)
      .__init__(self, *message)
  [Func]  decode_density_matrix(density_matrix: object) -> list[list[complex]] | None
  [Func]  decode_density_matrix_contract(density_matrix: 'object') -> 'DensityMatrixData | None'
  [Func]  decode_statevector(statevector: object) -> list[list[complex]] | None
  [Func]  decode_statevector_contract(statevector: 'object') -> 'StatevectorData | None'

--- Module: qpiai_quantum.jobmanager.sse_handler ---
  [Class] SSEResultHandler(self, device_name: str | None = None, timeout: int = 300)
      .__init__(self, device_name: str | None = None, timeout: int = 300)
      .get_error(self) -> str | None
      .get_result(self) -> dict | None
      .wait_for_events(self, url: str, headers: dict) -> bool
  [Func]  decode_statevector(statevector: object) -> list[list[complex]] | None

--- Module: qpiai_quantum.quantum_info ---
  Doc: Quantum information module for state representation and manipulation.
  [Class] DensityMatrix(self, data: list | numpy.ndarray | qpiai_quantum.circuit.circuit.Circuit | ForwardRef('DensityMatrix'), dims: list[int] | None = None, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local')
      .__init__(self, data: list | numpy.ndarray | qpiai_quantum.circuit.circuit.Circuit | ForwardRef('DensityMatrix'), dims: list[int] | None = None, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local')
      .copy(self) -> 'DensityMatrix'
      .entropy(self) -> float
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .from_circuit_object(circuit: qpiai_quantum.circuit.circuit.Circuit, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local') -> 'DensityMatrix'
      .from_formalism(formalism_dm) -> 'DensityMatrix'
      .from_label(label: str) -> 'DensityMatrix'
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .partial_trace(self, qubits_to_keep: list, dims: list | None = None) -> numpy.ndarray
      .probabilities(self) -> numpy.ndarray
      .probabilities_dict(self, decimals: int | None = None) -> dict
      .purity(self) -> float
      .to_formalism(self)
      .to_statevector(self)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] Statevector(self, data: 'list | np.ndarray | Circuit | Statevector', dims: 'list[int] | None' = None, experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local')
      .__init__(self, data: 'list | np.ndarray | Circuit | Statevector', dims: 'list[int] | None' = None, experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local')
      .copy(self) -> 'Statevector'
      .evolve(self, other: 'Circuit | np.ndarray') -> 'Statevector'
      .from_circuit_object(circuit: 'Circuit', experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local') -> 'Statevector'
      .from_label(label: 'str') -> 'Statevector'
      .is_valid(self, atol: 'float' = 1e-08) -> 'bool'
      .probabilities(self) -> 'np.ndarray'
      .probabilities_dict(self, decimals: 'int | None' = None) -> 'dict'
      .purity(self) -> 'float'
      .to_density_matrix(self)
      .to_dict(self, decimals: 'int' = 8) -> 'dict'

--- Module: qpiai_quantum.quantum_info.density_matrix ---
  Doc: DensityMatrix class for quantum state representation.
  [Class] BaseDensityMatrix(self, /, *args, **kwargs)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .partial_trace(self, qubits_to_keep: list, dims: list | None = None) -> numpy.ndarray
      .purity(self) -> float
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] DensityMatrix(self, data: list | numpy.ndarray | qpiai_quantum.circuit.circuit.Circuit | ForwardRef('DensityMatrix'), dims: list[int] | None = None, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local')
      .__init__(self, data: list | numpy.ndarray | qpiai_quantum.circuit.circuit.Circuit | ForwardRef('DensityMatrix'), dims: list[int] | None = None, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local')
      .copy(self) -> 'DensityMatrix'
      .entropy(self) -> float
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .from_circuit_object(circuit: qpiai_quantum.circuit.circuit.Circuit, experiment_name: str = 'Default Experiment', device_name: str = 'QpiAI-QSV-Local') -> 'DensityMatrix'
      .from_formalism(formalism_dm) -> 'DensityMatrix'
      .from_label(label: str) -> 'DensityMatrix'
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .partial_trace(self, qubits_to_keep: list, dims: list | None = None) -> numpy.ndarray
      .probabilities(self) -> numpy.ndarray
      .probabilities_dict(self, decimals: int | None = None) -> dict
      .purity(self) -> float
      .to_formalism(self)
      .to_statevector(self)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] FormalismDensityMatrix(self, state: list[list[complex]] | numpy.ndarray)
      .ADC(self, param: float)
      .__init__(self, state: list[list[complex]] | numpy.ndarray)
      .basis_operators(argument: int)
      .check(density_matrix: 'DensityMatrix', verbose: bool = False) -> bool
      .check_MUB(a: list[numpy.ndarray], b: list[numpy.ndarray], verbose: bool = False) -> bool
      .concurrence(self) -> float
      .correlation_points(self, state: numpy.ndarray)
      .depol(self, param: float)
      .distinguishability(self, X, *varargin)
      .entangling_power_2q(U: numpy.ndarray)
      .eof(self)
      .fidelity(self, other: 'BaseDensityMatrix', validate: bool = True) -> float
      .gate_expand_2_to_n(U, N, control=None, target=None, targets=None)
      .get_state(self) -> numpy.ndarray
      .has_symmetric_extension(self)
      .is_pure(self, atol: float = 1e-08) -> bool
      .is_valid(self, atol: float = 1e-08) -> bool
      .kraus(self, operator: list[numpy.ndarray])
      .l1_norm(self) -> float
      .max_bell_value(self)
      .partial_trace(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .partial_transpose(self, dims: list[int], axis: int) -> 'DensityMatrix'
      .plot_correlation_space_2q(self, p_adc=False, p_depol=False)
      .purity(self) -> float
      .relative_entropy_coherence(self) -> float
      .reyni(self, base: float = 2, alpha: float = 1)
      .schmidt_rank(self)
      .show(self)
      .swap(N=None, targets=[0, 1])
      .teleportation_fidelity(self)
      .tensor_product(*args)
      .trace(self) -> complex
      .von_neumann_entropy(self) -> float
  [Class] JobManager(self, /, *args, **kwargs)
      .cancel_job(self, job_id: str) -> dict[str, typing.Any]
      .clear_resource_cache()
      .delete_job(self, job_id: str) -> dict[str, typing.Any]
      .get_current_job(self) -> dict[str, Any] | None
      .get_experiment_id_by_name(self, experiment_name: str) -> str
      .get_job_history(self, period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(self, job_id: str, device_name: str | None = None) -> 'JobResult'
      .get_job_status(self, job_id: str) -> dict[str, Any] | None
      .list_compute_resources(self) -> list[dict[str, typing.Any]]
      .submit_and_wait_for_results_qasm(self, qasm_string_or_circuit: str | qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False, use_events: bool = True, timeout: int = 300) -> qpiai_quantum.jobmanager.job_result.JobResult
      .submit_circuit_job(self, circuit: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str | None = None, compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .submit_qasm_job(self, qasm_string: str, experiment_name: str = 'Default Experiment', shots: int = 1024, method: str = 'statevector', need_statevector: bool = False, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Simulator', circuit_name: str = 'circuit', compute_resource_id: str | None = None, overwrite: bool = False) -> dict[str, typing.Any]
      .track_job(func, job_name: str)

--- Module: qpiai_quantum.quantum_info.statevector ---
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] Statevector(self, data: 'list | np.ndarray | Circuit | Statevector', dims: 'list[int] | None' = None, experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local')
      .__init__(self, data: 'list | np.ndarray | Circuit | Statevector', dims: 'list[int] | None' = None, experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local')
      .copy(self) -> 'Statevector'
      .evolve(self, other: 'Circuit | np.ndarray') -> 'Statevector'
      .from_circuit_object(circuit: 'Circuit', experiment_name: 'str' = 'Default Experiment', device_name: 'str' = 'QpiAI-QSV-Local') -> 'Statevector'
      .from_label(label: 'str') -> 'Statevector'
      .is_valid(self, atol: 'float' = 1e-08) -> 'bool'
      .probabilities(self) -> 'np.ndarray'
      .probabilities_dict(self, decimals: 'int | None' = None) -> 'dict'
      .purity(self) -> 'float'
      .to_density_matrix(self)
      .to_dict(self, decimals: 'int' = 8) -> 'dict'

--- Module: qpiai_quantum.results ---
  Doc: Results Module |  | Provides base classes and interfaces for quantum execution results.
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)

--- Module: qpiai_quantum.results.base_result ---
  Doc: Base Result Class |  | Provides an abstract base class for all quantum execution result types.
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)

--- Module: qpiai_quantum.simulator ---
  Doc: QpiAI Quantum Simulator | ======================= | Local simulation tools for QpiAI Quantum circuits.
  [Class] BaseSimulator(self, /, *args, **kwargs)
      .run(self, circuit: 'Circuit', shots: int = 1024, seed: int | None = None, name: str | None = None) -> qpiai_quantum.results.base_result.BaseQuantumResult
  [Class] QasmSimulatorResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list | None = None, probabilities: dict[str, float] | None = None, density_matrix=None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = 'qasm_simulator', credits_used: int = 0, job_metadata: dict[str, Any] | None = None, n_qubits: int | None = None, n_cbits: int | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list | None = None, probabilities: dict[str, float] | None = None, density_matrix=None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = 'qasm_simulator', credits_used: int = 0, job_metadata: dict[str, Any] | None = None, n_qubits: int | None = None, n_cbits: int | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent: int = 2) -> str
  [Class] StatevectorSimulator(self, /, *args, **kwargs)
      .run(self, circuit: 'Circuit', shots: int = 1024, seed: int | None = None, name: str | None = None, initial_state: numpy.ndarray | None = None) -> qpiai_quantum.simulator.result.QasmSimulatorResult

--- Module: qpiai_quantum.simulator.base_simulator ---
  Doc: Abstract Base Simulator | ======================= | Defines the standard interface for all local quantum simulators
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] BaseSimulator(self, /, *args, **kwargs)
      .run(self, circuit: 'Circuit', shots: int = 1024, seed: int | None = None, name: str | None = None) -> qpiai_quantum.results.base_result.BaseQuantumResult

--- Module: qpiai_quantum.simulator.gates ---
  Doc: Gate Matrices and Specifications | ================================= | Pure-math module containing single/multi-qubit gate matrices,
  [Func]  controlled(U: numpy.ndarray, n_ctrl: int = 1) -> numpy.ndarray
  [Func]  decompose(name: str, qubits: list[int]) -> list[tuple[str, list[float], list[int]]]
  [Func]  gate_decomposition(name: str, qubits: list[int], params: list[float] | None = None) -> list[qpiai_quantum.icr.circuitoperation.CircuitOperation] | None
  [Func]  gate_spec(name: str, params: list[float], num_qubits: int | None = None) -> tuple[int, numpy.ndarray]
  [Func]  rx_matrix(theta: float) -> numpy.ndarray
  [Func]  rxx_matrix(theta: float) -> numpy.ndarray
  [Func]  ry_matrix(theta: float) -> numpy.ndarray
  [Func]  ryy_matrix(theta: float) -> numpy.ndarray
  [Func]  rz_matrix(theta: float) -> numpy.ndarray
  [Func]  rzz_matrix(theta: float) -> numpy.ndarray
  [Func]  u3_matrix(theta: float, phi: float, lam: float) -> numpy.ndarray
  [Func]  validate_parameter(value: float) -> float

--- Module: qpiai_quantum.simulator.operation_execution ---
  Doc: Quantum operations with explicit controls and probability-weighted branches.
  [Class] CircuitOperation(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .__init__(self, operation_type: qpiai_quantum.icr.circuitoperation.OperationType, gate_name: str, qubits: list[int], params: list[float] | None = None, clbits: list[int] | None = None, parameter_index: int | None = None, parameter_scale: float = 1.0)
      .decompose(self) -> list['CircuitOperation'] | None
      .get_gate(name: str)
      .list_gates()
      .to_json(self) -> dict[str, typing.Any]
  [Func]  apply_operation(state: numpy.ndarray, n: int, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation, apply_unitary: collections.abc.Callable, check_budget: collections.abc.Callable[[], None], controls: tuple[int, ...] = ()) -> numpy.ndarray
  [Func]  execute(operations: collections.abc.Iterable[qpiai_quantum.icr.circuitoperation.CircuitOperation], state: numpy.ndarray, n: int, n_cbits: int, shots: int, seed: int | None, apply_unitary: collections.abc.Callable, check_budget: collections.abc.Callable[[], None]) -> tuple[list | None, list | None, dict[str, int], dict]
  [Func]  flatten(operations: collections.abc.Iterable[qpiai_quantum.icr.circuitoperation.CircuitOperation]) -> collections.abc.Iterator[qpiai_quantum.icr.circuitoperation.CircuitOperation]
  [Func]  gate_spec(name: str, params: list[float], num_qubits: int | None = None) -> tuple[int, numpy.ndarray]
  [Func]  project(state: numpy.ndarray, qubit: int, outcome: int) -> tuple[float, numpy.ndarray | None]
  [Func]  validate_index(value: int) -> int

--- Module: qpiai_quantum.simulator.result ---
  Doc: QASM Simulator Result | ====================== | Concrete :class:`~qpiai_quantum.results.base_result.BaseQuantumResult`
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] QasmSimulatorResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list | None = None, probabilities: dict[str, float] | None = None, density_matrix=None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = 'qasm_simulator', credits_used: int = 0, job_metadata: dict[str, Any] | None = None, n_qubits: int | None = None, n_cbits: int | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list | None = None, probabilities: dict[str, float] | None = None, density_matrix=None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = 'qasm_simulator', credits_used: int = 0, job_metadata: dict[str, Any] | None = None, n_qubits: int | None = None, n_cbits: int | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent: int = 2) -> str

--- Module: qpiai_quantum.simulator.statevector ---
  Doc: Statevector Simulator | ===================== | A self-contained statevector simulator that executes QpiAI Quantum
  [Class] BaseSimulator(self, /, *args, **kwargs)
      .run(self, circuit: 'Circuit', shots: int = 1024, seed: int | None = None, name: str | None = None) -> qpiai_quantum.results.base_result.BaseQuantumResult
  [Class] OperationType(self, /, *args, **kwargs)
  [Class] QasmSimulatorResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list | None = None, probabilities: dict[str, float] | None = None, density_matrix=None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = 'qasm_simulator', credits_used: int = 0, job_metadata: dict[str, Any] | None = None, n_qubits: int | None = None, n_cbits: int | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list | None = None, probabilities: dict[str, float] | None = None, density_matrix=None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = 'qasm_simulator', credits_used: int = 0, job_metadata: dict[str, Any] | None = None, n_qubits: int | None = None, n_cbits: int | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent: int = 2) -> str
  [Class] StatevectorSimulator(self, /, *args, **kwargs)
      .run(self, circuit: 'Circuit', shots: int = 1024, seed: int | None = None, name: str | None = None, initial_state: numpy.ndarray | None = None) -> qpiai_quantum.simulator.result.QasmSimulatorResult
  [Func]  gate_spec(name: str, params: list[float], num_qubits: int | None = None) -> tuple[int, numpy.ndarray]

--- Module: qpiai_quantum.state_preparation ---
  [Class] BellStateGenerator(self, state_type: str = '|Ψ+>')
      .__init__(self, state_type: str = '|Ψ+>')
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .compare_all_bell_states(shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None)
      .get_all_bell_states() -> dict[str, 'BellStateGenerator']
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.4) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] ClusterStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .compare_different_sizes(qubit_range: list[int] = [2, 3, 4], shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None) -> dict[int, qpiai_quantum.results.base_result.BaseQuantumResult]
      .get_circuit_depth(self) -> int
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.5) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] GHZStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .calculate_entanglement_depth(self) -> int
      .compare_different_sizes(qubit_range: list[int] = [3, 4, 5], shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None) -> dict[int, qpiai_quantum.results.base_result.BaseQuantumResult]
      .compare_with_product_state(self, result: qpiai_quantum.results.base_result.BaseQuantumResult) -> dict[str, float]
      .create_multiple_sizes(min_qubits: int = 3, max_qubits: int = 6) -> dict[int, 'GHZStateGenerator']
      .get_circuit_depth(self) -> int
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.4) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] WStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .calculate_robustness(self, particle_loss_count: int = 1) -> float
      .compare_with_ghz_robustness(self, particle_loss_count: int = 1) -> dict[str, float]
      .count_excitations(self, result: qpiai_quantum.results.base_result.BaseQuantumResult) -> dict[int, int]
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.2) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)

--- Module: qpiai_quantum.state_preparation.bell_state ---
  [Class] Backend(self, /, *args, **kwargs)
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] BellStateGenerator(self, state_type: str = '|Ψ+>')
      .__init__(self, state_type: str = '|Ψ+>')
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .compare_all_bell_states(shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None)
      .get_all_bell_states() -> dict[str, 'BellStateGenerator']
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.4) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Func]  create_bell_state(state_type: str = '|Ψ+>') -> qpiai_quantum.state_preparation.bell_state.BellStateGenerator
  [Func]  get_all_bell_state_circuits(measure: bool = True) -> dict[str, qpiai_quantum.circuit.circuit.Circuit]
  [Func]  get_bell_state_circuit(state_type: str = '|Ψ+>', measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.state_preparation.cluster_state ---
  [Class] Backend(self, /, *args, **kwargs)
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] ClusterStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .compare_different_sizes(qubit_range: list[int] = [2, 3, 4], shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None) -> dict[int, qpiai_quantum.results.base_result.BaseQuantumResult]
      .get_circuit_depth(self) -> int
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.5) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Func]  create_cluster_state(num_qubits: int = 3) -> qpiai_quantum.state_preparation.cluster_state.ClusterStateGenerator
  [Func]  get_cluster_state_circuit(num_qubits: int = 3, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.state_preparation.ghz_state ---
  [Class] Backend(self, /, *args, **kwargs)
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] GHZStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .calculate_entanglement_depth(self) -> int
      .compare_different_sizes(qubit_range: list[int] = [3, 4, 5], shots: int = 1024, backend: qpiai_quantum.jobmanager.backend.Backend | None = None) -> dict[int, qpiai_quantum.results.base_result.BaseQuantumResult]
      .compare_with_product_state(self, result: qpiai_quantum.results.base_result.BaseQuantumResult) -> dict[str, float]
      .create_multiple_sizes(min_qubits: int = 3, max_qubits: int = 6) -> dict[int, 'GHZStateGenerator']
      .get_circuit_depth(self) -> int
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.4) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Func]  create_ghz_state(num_qubits: int = 3) -> qpiai_quantum.state_preparation.ghz_state.GHZStateGenerator
  [Func]  get_ghz_circuit(num_qubits: int = 3, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.state_preparation.w_state ---
  [Class] Backend(self, /, *args, **kwargs)
  [Class] BaseQuantumResult(self, /, *args, **kwargs)
      .get(self, *params) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] JobResult(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .__init__(self, name: str | None = None, counts: dict[str, int] | None = None, statevector: list[list[complex]] | None = None, probabilities: dict[str, float] | None = None, density_matrix: list[list[complex]] | None = None, message: str | None = 'Job executed successfully', execution_time: float = 0.0, cpu_usage: float = 0.0, memory_usage: float = 0.0, gpu_memory_usage: float = 0.0, shots: int | None = 0, job_id: str | None = None, job_status: str | None = None, method: str | None = None, credits_used: int = 0, job_metadata: dict[str, Any] | None = None)
      .get(self, *param) -> dict[str, typing.Any]
      .get_counts(self) -> dict[str, int] | None
      .get_job_id(self) -> str | None
      .get_job_status(self) -> str | None
      .get_probabilities(self) -> dict[str, float] | None
      .get_statevector(self) -> list | None
      .plot(self, *other_results, **kwargs)
      .set_name(self, name: str)
      .to_json(self, indent=2)
  [Class] QuantumAlgorithm(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .__init__(self, num_qubits: int, name: str = 'QuantumAlgorithm')
      .build_circuit(self, *args, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Class] WStateGenerator(self, num_qubits: int = 3)
      .__init__(self, num_qubits: int = 3)
      .build_circuit(self, measure: bool = True, **kwargs) -> qpiai_quantum.circuit.circuit.Circuit
      .calculate_robustness(self, particle_loss_count: int = 1) -> float
      .compare_with_ghz_robustness(self, particle_loss_count: int = 1) -> dict[str, float]
      .count_excitations(self, result: qpiai_quantum.results.base_result.BaseQuantumResult) -> dict[int, int]
      .get_expected_outcomes(self) -> dict[str, float]
      .get_info(self) -> dict[str, typing.Any]
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool = True, need_density_matrix: bool = False, device_name: str = 'QpiAI-QSV-Local', reverse_bits: bool = False, **kwargs) -> 'BaseQuantumResult'
      .to_qasm(self)
      .verify_entanglement(self, result: qpiai_quantum.results.base_result.BaseQuantumResult, threshold: float = 0.2) -> bool
      .visualize(self, plot: str = 'circuit', result: qpiai_quantum.results.base_result.BaseQuantumResult | None = None, **kwargs)
  [Func]  create_w_state(num_qubits: int = 3) -> qpiai_quantum.state_preparation.w_state.WStateGenerator
  [Func]  get_w_circuit(num_qubits: int = 3, measure: bool = True) -> qpiai_quantum.circuit.circuit.Circuit

--- Module: qpiai_quantum.utils ---
  Doc: Module for QpiAI Quantum SDK.

--- Module: qpiai_quantum.utils.gate_matrices ---
  [Class] GateMatrices(self, /, *args, **kwargs)
      .RY(theta)
      .RZ(theta)

--- Module: qpiai_quantum.visualization ---
  [Class] MatplotlibVisualizer(self, /, *args, **kwargs)
      .plot_icr(icr: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True) -> None
  [Class] PlotlyBlochSphere(self)
      .__init__(self)
      .add_density_matrix(self, rho: numpy.ndarray, color: str = 'red', label: str | None = None)
      .add_state(self, state_vector: list[complex] | numpy.ndarray, color: str = 'red', label: str | None = None)
      .add_state_from_angles(self, theta: float, phi: float, color: str = 'red', label: str | None = None)
      .add_vector(self, vector: list[float] | numpy.ndarray, color: str = 'red', label: str | None = None)
      .clear(self)
      .save(self, filename: str, **kwargs)
      .show(self, title: str = 'Interactive Bloch Sphere', width: int = 800, height: int = 800)
  [Func]  create_interactive_bloch_sphere(states: list[numpy.ndarray] | None = None, colors: list[str] | None = None, labels: list[str] | None = None, title: str = 'Interactive Bloch Sphere') -> qpiai_quantum.visualization.q_sphere.bloch_sphere_plotly.PlotlyBlochSphere

--- Module: qpiai_quantum.visualization.latex_visualizer ---
  Doc: Module for QpiAI Quantum SDK.

--- Module: qpiai_quantum.visualization.matplotlib_visualizer ---
  [Class] MatplotlibVisualizer(self, /, *args, **kwargs)
      .plot_icr(icr: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True) -> None

--- Module: qpiai_quantum.visualization.matplotlib_visualizer.exceptions ---
  [Class] BaseError(self, *message)
      .__init__(self, *message)
  [Class] MatplotlibVisualizerException(self, *message)
      .__init__(self, *message)

--- Module: qpiai_quantum.visualization.matplotlib_visualizer.plotter ---
  [Class] Plotter(self, max_depth, num_qubits, break_point, num_broken_circuit, scale=1, use_mathtext: bool = True)
      .__init__(self, max_depth, num_qubits, break_point, num_broken_circuit, scale=1, use_mathtext: bool = True)
      .draw_barrier(self, x, y)
      .draw_clbit_wires(self, x_start, x_end, y_pos)
      .draw_controlled_swap(self, x, control_y, swap_y1, swap_y2)
      .draw_measure(self, x, qubit_y, clbit_y, target, basis='z')
      .draw_multi_qubit_gate(self, x, qubits, label)
      .draw_n_qubit_gate(self, x: float, qubits: list[int], label: str, params: list[float] | None = None)
      .draw_one_qubit_non_parametric(self, x, y, label)
      .draw_one_qubit_parametric(self, x, y, label, parameter)
      .draw_operation(self, x, y_start, y_end, label)
      .draw_qubit_wires(self, x_start, x_end, num_qubits)
      .draw_reset(self, x, y)
      .draw_swap(self, x, y1, y2)
      .draw_three_qubit_non_parametric(self, x, control1_y, control2_y, target_y, label)
      .draw_two_qubit_non_parametric(self, x, control_y, target_y, label)
      .draw_two_qubit_parametric(self, x, control_y, target_y, label, parameter)
      .operation_column_width(self, label: str) -> float
      .operation_column_width_for_label(label: str, use_mathtext: bool = True) -> float
      .operation_width(self, label: str) -> float
      .operation_width_for_label(label: str, use_mathtext: bool = True) -> float
      .set_theme(self, theme: str)

--- Module: qpiai_quantum.visualization.matplotlib_visualizer.visualizer ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] ICR(self, *registers, name, metadata)
      .__init__(self, *registers, name, metadata)
      .to_json(self)
  [Class] MatplotlibVisualizer(self, /, *args, **kwargs)
      .plot_icr(icr: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True) -> None
  [Class] OperationType(self, /, *args, **kwargs)
  [Class] Plotter(self, max_depth, num_qubits, break_point, num_broken_circuit, scale=1, use_mathtext: bool = True)
      .__init__(self, max_depth, num_qubits, break_point, num_broken_circuit, scale=1, use_mathtext: bool = True)
      .draw_barrier(self, x, y)
      .draw_clbit_wires(self, x_start, x_end, y_pos)
      .draw_controlled_swap(self, x, control_y, swap_y1, swap_y2)
      .draw_measure(self, x, qubit_y, clbit_y, target, basis='z')
      .draw_multi_qubit_gate(self, x, qubits, label)
      .draw_n_qubit_gate(self, x: float, qubits: list[int], label: str, params: list[float] | None = None)
      .draw_one_qubit_non_parametric(self, x, y, label)
      .draw_one_qubit_parametric(self, x, y, label, parameter)
      .draw_operation(self, x, y_start, y_end, label)
      .draw_qubit_wires(self, x_start, x_end, num_qubits)
      .draw_reset(self, x, y)
      .draw_swap(self, x, y1, y2)
      .draw_three_qubit_non_parametric(self, x, control1_y, control2_y, target_y, label)
      .draw_two_qubit_non_parametric(self, x, control_y, target_y, label)
      .draw_two_qubit_parametric(self, x, control_y, target_y, label, parameter)
      .operation_column_width(self, label: str) -> float
      .operation_column_width_for_label(label: str, use_mathtext: bool = True) -> float
      .operation_width(self, label: str) -> float
      .operation_width_for_label(label: str, use_mathtext: bool = True) -> float
      .set_theme(self, theme: str)

--- Module: qpiai_quantum.visualization.plotly_visualizer ---
  [Class] PlotlyVisualizer(self, /, *args, **kwargs)
      .plot_icr(icr: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, theme: str = 'dark') -> None

--- Module: qpiai_quantum.visualization.plotly_visualizer.exceptions ---
  [Class] BaseError(self, *message)
      .__init__(self, *message)
  [Class] PlotlyVisualizerException(self, *message)
      .__init__(self, *message)

--- Module: qpiai_quantum.visualization.plotly_visualizer.plotter ---
  [Class] Plotter(self, max_depth, num_qubits, theme='light', scale=1)
      .__init__(self, max_depth, num_qubits, theme='light', scale=1)
      .draw_barrier(self, x, y, y_offset=0)
      .draw_circuit(self, gates)
      .draw_clbit_wires(self, x_start, x_end, y_pos, y_offset=0)
      .draw_controlled_swap(self, x, control_y, swap_y1, swap_y2, y_offset=0)
      .draw_measure(self, x, qubit_y, clbit_y, target, basis='z', y_offset=0)
      .draw_multi_qubit_gate(self, x, qubits, label, y_offset=0)
      .draw_n_qubit_gate(self, x: float, qubits: list[int], label: str, params: list[float] | None = None, y_offset=0)
      .draw_one_qubit_non_parametric(self, x, y, label, y_offset=0)
      .draw_one_qubit_parametric(self, x, y, label, parameter, y_offset=0)
      .draw_operation(self, x, y_start, y_end, label, y_offset=0)
      .draw_qubit_wires(self, x_start, x_end, num_qubits, y_offset=0)
      .draw_reset(self, x, y, y_offset=0)
      .draw_swap(self, x, y1, y2, y_offset=0)
      .draw_three_qubit_non_parametric(self, x, control1_y, control2_y, target_y, label, y_offset=0)
      .draw_two_qubit_non_parametric(self, x, control_y, target_y, label, y_offset=0)
      .draw_two_qubit_parametric(self, x, control_y, target_y, label, parameter, y_offset=0)
      .set_theme(self, theme: str)
      .show(self)

--- Module: qpiai_quantum.visualization.plotly_visualizer.visualizer ---
  [Class] Circuit(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .__init__(self, *regs: int | qpiai_quantum.circuit.register.Register, name=None, metadata=None)
      .add_operation(self, operation: qpiai_quantum.icr.circuitoperation.CircuitOperation)
      .barrier(self, *qubits: int)
      .cancel_job(job_id: str) -> dict[str, typing.Any]
      .ccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int)
      .ch(self, control_qubit: int, target_qubit: int)
      .check_job_status(job_id: str) -> dict[str, Any] | None
      .compose(self, other: 'Circuit', qubits: list[int] | None = None)
      .cp(self, control_qubit: int, target_qubit: int, theta: float)
      .crx(self, control_qubit: int, target_qubit: int, theta: float)
      .cry(self, control_qubit: int, target_qubit: int, theta: float)
      .crz(self, control_qubit: int, target_qubit: int, theta: float)
      .cs(self, control_qubit: int, target_qubit: int)
      .csdg(self, control_qubit: int, target_qubit: int) -> None
      .cswap(self, control_qubit: int, target_qubit1: int, target_qubit2: int)
      .cu(self, control_qubit: int, target_qubit: int, theta: float, phi: float, lam: float, gamma: float) -> None
      .cx(self, control_qubit: int, target_qubit: int)
      .cy(self, control_qubit: int, target_qubit: int)
      .cz(self, control_qubit: int, target_qubit: int)
      .dcx(self, qubit1: int, qubit2: int) -> None
      .delete_job(job_id: str) -> dict[str, typing.Any]
      .depth(self) -> int
      .ecr(self, qubit1: int, qubit2: int)
      .get_current_job() -> dict[str, Any] | None
      .get_job_history(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .get_job_results(job_id: str) -> 'JobResult'
      .get_job_status(job_id: str) -> dict[str, Any] | None
      .h(self, qubit: int)
      .id(self, qubit: int)
      .inverse(self) -> 'Circuit'
      .iswap(self, qubit1: int, qubit2: int)
      .iswapdg(self, qubit1: int, qubit2: int)
      .list_gates(self) -> dict
      .list_jobs(period: str | None = None, status: str | None = None, page: int = 1, page_size: int = 20) -> dict[str, typing.Any]
      .mcx(self, control_qubits: list[int], target_qubit: int)
      .measure(self, qubit: int | list[int], clbit: int | list[int])
      .measure_all(self)
      .p(self, qubit: int, theta: float)
      .rccx(self, control_qubit1: int, control_qubit2: int, target_qubit: int) -> None
      .remove_operation(self, upto: int = 1)
      .reset(self, qubit: int) -> None
      .run(self, shots: int = 1024, experiment_name: str = 'Default Experiment', need_statevector: bool | None = None, need_density_matrix: bool | None = None, device_name: str = 'QpiAI-QSV-Simulator', reverse_bits: bool = False, **kwargs) -> ForwardRef('JobResult') | ForwardRef('BaseQuantumResult')
      .rx(self, qubit: int, theta: float)
      .rxx(self, qubit1: int, qubit2: int, theta: float)
      .ry(self, qubit: int, theta: float)
      .ryy(self, qubit1: int, qubit2: int, theta: float)
      .rz(self, qubit: int, theta: float)
      .rzz(self, qubit1: int, qubit2: int, theta: float)
      .s(self, qubit: int)
      .sdg(self, qubit: int)
      .show(self, theme: str = 'light', dpi: int = 200, use_mathtext: bool = True)
      .size(self) -> int
      .swap(self, qubit1: int, qubit2: int)
      .sx(self, qubit: int)
      .sxdg(self, qubit: int)
      .t(self, qubit: int)
      .tdg(self, qubit: int)
      .to_circuit_operation(self, name=None)
      .to_json(self) -> dict
      .to_qasm(self)
      .u(self, qubit: int, theta: float, phi: float, lam: float)
      .u2(self, qubit: int, phi: float, lam: float) -> None
      .x(self, qubit: int)
      .y(self, qubit: int)
      .z(self, qubit: int)
  [Class] ICR(self, *registers, name, metadata)
      .__init__(self, *registers, name, metadata)
      .to_json(self)
  [Class] OperationType(self, /, *args, **kwargs)
  [Class] PlotlyVisualizer(self, /, *args, **kwargs)
      .plot_icr(icr: qpiai_quantum.circuit.circuit.Circuit | qpiai_quantum.icr.icr.IntermediateCircuitRepresentation, theme: str = 'dark') -> None
  [Class] Plotter(self, max_depth, num_qubits, theme='light', scale=1)
      .__init__(self, max_depth, num_qubits, theme='light', scale=1)
      .draw_barrier(self, x, y, y_offset=0)
      .draw_circuit(self, gates)
      .draw_clbit_wires(self, x_start, x_end, y_pos, y_offset=0)
      .draw_controlled_swap(self, x, control_y, swap_y1, swap_y2, y_offset=0)
      .draw_measure(self, x, qubit_y, clbit_y, target, basis='z', y_offset=0)
      .draw_multi_qubit_gate(self, x, qubits, label, y_offset=0)
      .draw_n_qubit_gate(self, x: float, qubits: list[int], label: str, params: list[float] | None = None, y_offset=0)
      .draw_one_qubit_non_parametric(self, x, y, label, y_offset=0)
      .draw_one_qubit_parametric(self, x, y, label, parameter, y_offset=0)
      .draw_operation(self, x, y_start, y_end, label, y_offset=0)
      .draw_qubit_wires(self, x_start, x_end, num_qubits, y_offset=0)
      .draw_reset(self, x, y, y_offset=0)
      .draw_swap(self, x, y1, y2, y_offset=0)
      .draw_three_qubit_non_parametric(self, x, control1_y, control2_y, target_y, label, y_offset=0)
      .draw_two_qubit_non_parametric(self, x, control_y, target_y, label, y_offset=0)
      .draw_two_qubit_parametric(self, x, control_y, target_y, label, parameter, y_offset=0)
      .set_theme(self, theme: str)
      .show(self)

--- Module: qpiai_quantum.visualization.q_sphere ---
  [Class] PlotlyBlochSphere(self)
      .__init__(self)
      .add_density_matrix(self, rho: numpy.ndarray, color: str = 'red', label: str | None = None)
      .add_state(self, state_vector: list[complex] | numpy.ndarray, color: str = 'red', label: str | None = None)
      .add_state_from_angles(self, theta: float, phi: float, color: str = 'red', label: str | None = None)
      .add_vector(self, vector: list[float] | numpy.ndarray, color: str = 'red', label: str | None = None)
      .clear(self)
      .save(self, filename: str, **kwargs)
      .show(self, title: str = 'Interactive Bloch Sphere', width: int = 800, height: int = 800)
  [Func]  create_interactive_bloch_sphere(states: list[numpy.ndarray] | None = None, colors: list[str] | None = None, labels: list[str] | None = None, title: str = 'Interactive Bloch Sphere') -> qpiai_quantum.visualization.q_sphere.bloch_sphere_plotly.PlotlyBlochSphere

--- Module: qpiai_quantum.visualization.q_sphere.bloch_sphere_plotly ---
  Doc: Interactive Bloch Sphere visualization using Plotly.
  [Class] PlotlyBlochSphere(self)
      .__init__(self)
      .add_density_matrix(self, rho: numpy.ndarray, color: str = 'red', label: str | None = None)
      .add_state(self, state_vector: list[complex] | numpy.ndarray, color: str = 'red', label: str | None = None)
      .add_state_from_angles(self, theta: float, phi: float, color: str = 'red', label: str | None = None)
      .add_vector(self, vector: list[float] | numpy.ndarray, color: str = 'red', label: str | None = None)
      .clear(self)
      .save(self, filename: str, **kwargs)
      .show(self, title: str = 'Interactive Bloch Sphere', width: int = 800, height: int = 800)
  [Func]  create_interactive_bloch_sphere(states: list[numpy.ndarray] | None = None, colors: list[str] | None = None, labels: list[str] | None = None, title: str = 'Interactive Bloch Sphere') -> qpiai_quantum.visualization.q_sphere.bloch_sphere_plotly.PlotlyBlochSphere

[Environment variables referenced inside qpiai_quantum]: ['API_KEY', 'QPIAI_SERVER_URL']

================================================================================
PROBE COMPLETE.
================================================================================

`
