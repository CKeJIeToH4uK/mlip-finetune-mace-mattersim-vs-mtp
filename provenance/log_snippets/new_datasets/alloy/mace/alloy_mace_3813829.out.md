# Log Snippet: repo/coursework/new_datasets/alloy/mace/alloy_mace_3813829.out

Original size: 48742 bytes. Full raw log not copied.

1: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
2:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
6: 2026-04-02 00:17:32.278 INFO: CUDA version: 12.4, CUDA device: 0
7: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/cli/run_train.py:169: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
8:   model_foundation = torch.load(
9: 2026-04-02 00:17:32.957 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
10: 2026-04-02 00:17:32.961 INFO: ===========LOADING INPUT DATA===========
12: 2026-04-02 00:17:32.962 INFO: Using the key specifications to parse data:
13: 2026-04-02 00:17:32.962 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
14: 2026-04-02 00:17:32.962 INFO: =============    Processing head Default     ===========
15: 2026-04-02 00:17:33.689 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
16: 2026-04-02 00:17:33.865 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
17: 2026-04-02 00:17:34.089 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
18: 2026-04-02 00:17:34.096 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
19: 2026-04-02 00:17:34.208 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
20: 2026-04-02 00:17:34.239 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
21: 2026-04-02 00:17:34.279 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
22: 2026-04-02 00:17:34.281 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
23: 2026-04-02 00:17:34.281 INFO: Total number of configurations: train=1210, valid=213, tests=[],
24: 2026-04-02 00:17:34.282 INFO: Using atomic numbers from command line argument
30: 2026-04-02 00:17:39.765 INFO: Combining 1 list datasets for head 'Default'
31: 2026-04-02 00:17:40.457 INFO: Combining 1 list datasets for head 'Default_valid'
32: 2026-04-02 00:17:40.457 INFO: Combined validation datasets for Default
33: 2026-04-02 00:17:40.457 INFO: Head 'Default' training dataset size: 1210
35: 2026-04-02 00:17:41.435 INFO: Average number of neighbors: 56.52305706170927
36: 2026-04-02 00:17:41.435 INFO: During training the following quantities will be reported: energy, forces
37: 2026-04-02 00:17:41.435 INFO: ===========MODEL DETAILS===========
40: 2026-04-02 00:17:42.154 INFO: Model configuration extracted from foundation model
41: 2026-04-02 00:17:42.154 INFO: Using weighted loss function for fine-tuning
42: 2026-04-02 00:17:42.154 INFO: Message passing with hidden irreps 128x0e)
45: 2026-04-02 00:17:42.154 INFO: Distance transform for radial basis functions: None
46: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
47:   warnings.warn(
48: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
49:   warnings.warn(
50: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
51:   warnings.warn(
52: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
53:   warnings.warn(
54: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
55:   warnings.warn(
56: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
57:   warnings.warn(
58: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
59:   warnings.warn(
60: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
61:   warnings.warn(
62: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
63:   warnings.warn(
64: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
65:   warnings.warn(
66: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
67:   warnings.warn(
68: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
69:   warnings.warn(
70: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
71:   warnings.warn(
72: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
73:   warnings.warn(
74: 2026-04-02 00:17:53.867 INFO: ===========OPTIMIZER INFORMATION===========
78: 2026-04-02 00:17:53.868 INFO: Learning rate: 0.01, weight decay: 5e-07
79: 2026-04-02 00:17:53.869 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
80: 2026-04-02 00:17:53.870 INFO: === Layer's learning rates ===
88: 2026-04-02 00:17:53.871 INFO: ===========TRAINING===========
89: 2026-04-02 00:17:53.871 INFO: Started training, reporting errors on validation set
90: 2026-04-02 00:17:53.872 INFO: Loss metrics on validation set
91: 2026-04-02 00:18:00.916 INFO: Initial: head: Default, loss=1.68970534, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
92: 2026-04-02 00:18:36.335 INFO: Epoch 0: head: Default, loss=0.45322180, RMSE_E_per_atom=  261.34 meV, RMSE_F=  198.58 meV / A
93: 2026-04-02 00:19:06.649 INFO: Epoch 1: head: Default, loss=0.33404976, RMSE_E_per_atom=  250.01 meV, RMSE_F=  173.56 meV / A
94: 2026-04-02 00:19:40.368 INFO: Epoch 2: head: Default, loss=0.29574253, RMSE_E_per_atom=  223.76 meV, RMSE_F=  170.27 meV / A
95: 2026-04-02 00:20:14.838 INFO: Epoch 3: head: Default, loss=0.32008296, RMSE_E_per_atom=  217.53 meV, RMSE_F=  159.48 meV / A
96: 2026-04-02 00:20:44.634 INFO: Epoch 4: head: Default, loss=0.27322507, RMSE_E_per_atom=  163.74 meV, RMSE_F=  153.25 meV / A
97: 2026-04-02 00:21:14.753 INFO: Epoch 5: head: Default, loss=0.23516969, RMSE_E_per_atom=  112.35 meV, RMSE_F=  150.26 meV / A
98: 2026-04-02 00:21:46.093 INFO: Epoch 6: head: Default, loss=0.27835247, RMSE_E_per_atom=  122.88 meV, RMSE_F=  168.29 meV / A
99: 2026-04-02 00:22:20.678 INFO: Epoch 7: head: Default, loss=0.29990528, RMSE_E_per_atom=  239.59 meV, RMSE_F=  154.96 meV / A
100: 2026-04-02 00:22:50.357 INFO: Epoch 8: head: Default, loss=0.19944971, RMSE_E_per_atom=  169.61 meV, RMSE_F=  136.55 meV / A
101: 2026-04-02 00:23:20.467 INFO: Epoch 9: head: Default, loss=0.24336029, RMSE_E_per_atom=  270.54 meV, RMSE_F=  146.10 meV / A
102: 2026-04-02 00:23:53.075 INFO: Epoch 10: head: Default, loss=0.23268202, RMSE_E_per_atom=  146.05 meV, RMSE_F=  148.51 meV / A
103: 2026-04-02 00:24:23.572 INFO: Epoch 11: head: Default, loss=0.21755363, RMSE_E_per_atom=  208.46 meV, RMSE_F=  148.12 meV / A
104: 2026-04-02 00:25:01.354 INFO: Epoch 12: head: Default, loss=0.24548369, RMSE_E_per_atom=  131.23 meV, RMSE_F=  148.83 meV / A
105: 2026-04-02 00:25:32.166 INFO: Epoch 13: head: Default, loss=0.19131407, RMSE_E_per_atom=   68.63 meV, RMSE_F=  130.37 meV / A
106: 2026-04-02 00:26:06.528 INFO: Epoch 14: head: Default, loss=0.21515118, RMSE_E_per_atom=  187.64 meV, RMSE_F=  148.60 meV / A
107: 2026-04-02 00:26:41.762 INFO: Epoch 15: head: Default, loss=0.21855052, RMSE_E_per_atom=   91.96 meV, RMSE_F=  135.77 meV / A
108: 2026-04-02 00:27:12.046 INFO: Epoch 16: head: Default, loss=0.23089392, RMSE_E_per_atom=  113.67 meV, RMSE_F=  141.20 meV / A
109: 2026-04-02 00:27:44.161 INFO: Epoch 17: head: Default, loss=0.30370984, RMSE_E_per_atom=  222.54 meV, RMSE_F=  166.28 meV / A
110: 2026-04-02 00:28:18.350 INFO: Epoch 18: head: Default, loss=0.18865864, RMSE_E_per_atom=  148.62 meV, RMSE_F=  134.44 meV / A
111: 2026-04-02 00:28:50.750 INFO: Epoch 19: head: Default, loss=0.19972458, RMSE_E_per_atom=  124.35 meV, RMSE_F=  135.15 meV / A
112: 2026-04-02 00:29:20.258 INFO: Epoch 20: head: Default, loss=0.17863202, RMSE_E_per_atom=  118.95 meV, RMSE_F=  128.95 meV / A
113: 2026-04-02 00:29:52.673 INFO: Epoch 21: head: Default, loss=0.22148440, RMSE_E_per_atom=  121.62 meV, RMSE_F=  145.53 meV / A
114: 2026-04-02 00:30:24.456 INFO: Epoch 22: head: Default, loss=0.18441888, RMSE_E_per_atom=   85.04 meV, RMSE_F=  131.25 meV / A
115: 2026-04-02 00:30:57.392 INFO: Epoch 23: head: Default, loss=0.20348597, RMSE_E_per_atom=  146.90 meV, RMSE_F=  144.25 meV / A
116: 2026-04-02 00:31:26.830 INFO: Epoch 24: head: Default, loss=0.18502910, RMSE_E_per_atom=  167.87 meV, RMSE_F=  134.48 meV / A
117: 2026-04-02 00:31:56.620 INFO: Epoch 25: head: Default, loss=0.18866166, RMSE_E_per_atom=   85.69 meV, RMSE_F=  131.15 meV / A
118: 2026-04-02 00:32:27.185 INFO: Epoch 26: head: Default, loss=0.18488951, RMSE_E_per_atom=   67.04 meV, RMSE_F=  132.65 meV / A
119: 2026-04-02 00:32:59.325 INFO: Epoch 27: head: Default, loss=0.16543825, RMSE_E_per_atom=  153.29 meV, RMSE_F=  132.71 meV / A
120: 2026-04-02 00:33:35.378 INFO: Epoch 28: head: Default, loss=0.15429333, RMSE_E_per_atom=  119.99 meV, RMSE_F=  126.04 meV / A
121: 2026-04-02 00:34:10.046 INFO: Epoch 29: head: Default, loss=0.16103959, RMSE_E_per_atom=  100.93 meV, RMSE_F=  130.65 meV / A
122: 2026-04-02 00:34:42.150 INFO: Epoch 30: head: Default, loss=0.15702184, RMSE_E_per_atom=  121.26 meV, RMSE_F=  122.08 meV / A
123: 2026-04-02 00:35:15.282 INFO: Epoch 31: head: Default, loss=0.19523196, RMSE_E_per_atom=   63.19 meV, RMSE_F=  130.63 meV / A
