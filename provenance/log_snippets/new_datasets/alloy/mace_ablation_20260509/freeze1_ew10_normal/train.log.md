# Log Snippet: repo/coursework/new_datasets/alloy/mace_ablation_20260509/freeze1_ew10_normal/train.log

Original size: 14821 bytes. Full raw log not copied.

1: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
2:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
6: 2026-05-10 07:01:59.488 INFO: CUDA version: 12.4, CUDA device: 0
7: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/cli/run_train.py:169: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
8:   model_foundation = torch.load(
9: 2026-05-10 07:02:01.026 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
10: 2026-05-10 07:02:01.028 INFO: ===========LOADING INPUT DATA===========
12: 2026-05-10 07:02:01.028 INFO: Using the key specifications to parse data:
13: 2026-05-10 07:02:01.028 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
14: 2026-05-10 07:02:01.028 INFO: =============    Processing head Default     ===========
15: 2026-05-10 07:02:01.569 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
16: 2026-05-10 07:02:01.740 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
17: 2026-05-10 07:02:01.957 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
18: 2026-05-10 07:02:01.963 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
19: 2026-05-10 07:02:02.072 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
20: 2026-05-10 07:02:02.103 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
21: 2026-05-10 07:02:02.146 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
22: 2026-05-10 07:02:02.147 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
23: 2026-05-10 07:02:02.148 INFO: Total number of configurations: train=1210, valid=213, tests=[],
24: 2026-05-10 07:02:02.148 INFO: Using atomic numbers from command line argument
30: 2026-05-10 07:02:06.724 INFO: Combining 1 list datasets for head 'Default'
31: 2026-05-10 07:02:07.379 INFO: Combining 1 list datasets for head 'Default_valid'
32: 2026-05-10 07:02:07.379 INFO: Combined validation datasets for Default
33: 2026-05-10 07:02:07.380 INFO: Head 'Default' training dataset size: 1210
35: 2026-05-10 07:02:08.606 INFO: Average number of neighbors: 56.52305706170927
36: 2026-05-10 07:02:08.607 INFO: During training the following quantities will be reported: energy, forces
37: 2026-05-10 07:02:08.607 INFO: ===========MODEL DETAILS===========
40: 2026-05-10 07:02:09.772 INFO: Model configuration extracted from foundation model
41: 2026-05-10 07:02:09.772 INFO: Using weighted loss function for fine-tuning
42: 2026-05-10 07:02:09.772 INFO: Message passing with hidden irreps 128x0e)
45: 2026-05-10 07:02:09.773 INFO: Distance transform for radial basis functions: None
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
74: 2026-05-10 07:02:12.561 INFO: ===========OPTIMIZER INFORMATION===========
78: 2026-05-10 07:02:12.562 INFO: Learning rate: 0.001, weight decay: 5e-07
79: 2026-05-10 07:02:12.563 INFO: WeightedEnergyForcesLoss(energy_weight=10.000, forces_weight=100.000)
80: 2026-05-10 07:02:12.564 INFO: Freezing embedding weights
89: 2026-05-10 07:02:12.568 INFO: ===========TRAINING===========
90: 2026-05-10 07:02:12.569 INFO: Started training, reporting errors on validation set
91: 2026-05-10 07:02:12.569 INFO: Loss metrics on validation set
92: 2026-05-10 07:02:18.996 INFO: Initial: head: Default, loss=3.47115944, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
93: 2026-05-10 07:02:54.757 INFO: Epoch 0: head: Default, loss=0.39031749, RMSE_E_per_atom=   86.36 meV, RMSE_F=  195.79 meV / A
94: 2026-05-10 07:14:41.572 INFO: Epoch 25: head: Default, loss=0.22876924, RMSE_E_per_atom=   54.50 meV, RMSE_F=  124.20 meV / A
95: 2026-05-10 07:26:28.997 INFO: Epoch 50: head: Default, loss=0.22627333, RMSE_E_per_atom=   31.01 meV, RMSE_F=  119.78 meV / A
96: 2026-05-10 07:38:14.968 INFO: Epoch 75: head: Default, loss=0.23178888, RMSE_E_per_atom=   41.25 meV, RMSE_F=  119.61 meV / A
97: 2026-05-10 07:50:00.908 INFO: Epoch 100: head: Default, loss=0.24055243, RMSE_E_per_atom=   40.94 meV, RMSE_F=  117.15 meV / A
98: 2026-05-10 08:01:48.492 INFO: Epoch 125: head: Default, loss=0.23875017, RMSE_E_per_atom=   27.93 meV, RMSE_F=  115.31 meV / A
99: 2026-05-10 08:13:41.134 INFO: Epoch 150: head: Default, loss=0.23532471, RMSE_E_per_atom=   37.92 meV, RMSE_F=  115.52 meV / A
100: 2026-05-10 08:25:26.933 INFO: Epoch 175: head: Default, loss=0.23741250, RMSE_E_per_atom=   38.47 meV, RMSE_F=  114.11 meV / A
101: 2026-05-10 08:36:38.720 INFO: Training complete
103: 2026-05-10 08:36:38.724 INFO: ===========RESULTS===========
104: 2026-05-10 08:36:38.736 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-175.pt
105: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/tools/checkpoint.py:187: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
106:   torch.load(f=checkpoint_info.path, map_location=device),
107: 2026-05-10 08:36:39.084 INFO: Loaded Stage one model from epoch 175 for evaluation
108: 2026-05-10 08:36:39.084 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42.model
109: 2026-05-10 08:36:40.233 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/models/alloy_mace_freeze1_ew10_normal_compiled.model
110: 2026-05-10 08:36:42.657 INFO: Computing metrics for training, validation, and test sets
111: 2026-05-10 08:36:42.658 INFO: Skipping evaluation for heads: ['pt_head']
112: 2026-05-10 08:36:42.659 INFO: Evaluating train_Default ...
113: 2026-05-10 08:36:52.680 INFO: Evaluating valid_Default ...
114: 2026-05-10 08:36:54.392 INFO: Error-table on TRAIN and VALID:
115: +---------------+---------------------+------------------+-------------------+
116: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
117: +---------------+---------------------+------------------+-------------------+
118: | train_Default |           36.2      |         82.4     |          9.15     |
119: | valid_Default |           38.5      |        114.1     |         12.86     |
120: +---------------+---------------------+------------------+-------------------+
