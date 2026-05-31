# Log Snippet: repo/coursework/new_datasets/alloy/mace_ablation_20260509/alloy_protocols_norm_3979635.out

Original size: 64897 bytes. Full raw log not copied.

6: 
7: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
8:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
13: 2026-05-10 03:36:04.379 INFO: CUDA version: 12.4, CUDA device: 0
14: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/cli/run_train.py:169: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
15:   model_foundation = torch.load(
16: 2026-05-10 03:36:05.570 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
17: 2026-05-10 03:36:05.572 INFO: ===========LOADING INPUT DATA===========
19: 2026-05-10 03:36:05.572 INFO: Using the key specifications to parse data:
20: 2026-05-10 03:36:05.572 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
21: 2026-05-10 03:36:05.573 INFO: =============    Processing head Default     ===========
22: 2026-05-10 03:36:06.204 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
23: 2026-05-10 03:36:06.394 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
24: 2026-05-10 03:36:06.638 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
25: 2026-05-10 03:36:06.645 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
26: 2026-05-10 03:36:06.792 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
27: 2026-05-10 03:36:06.826 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
28: 2026-05-10 03:36:06.870 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
29: 2026-05-10 03:36:06.871 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
30: 2026-05-10 03:36:06.872 INFO: Total number of configurations: train=1210, valid=213, tests=[],
31: 2026-05-10 03:36:06.872 INFO: Using atomic numbers from command line argument
37: 2026-05-10 03:36:11.173 INFO: Combining 1 list datasets for head 'Default'
38: 2026-05-10 03:36:11.858 INFO: Combining 1 list datasets for head 'Default_valid'
39: 2026-05-10 03:36:11.858 INFO: Combined validation datasets for Default
40: 2026-05-10 03:36:11.859 INFO: Head 'Default' training dataset size: 1210
42: 2026-05-10 03:36:12.733 INFO: Average number of neighbors: 56.52305706170927
43: 2026-05-10 03:36:12.733 INFO: During training the following quantities will be reported: energy, forces
44: 2026-05-10 03:36:12.733 INFO: ===========MODEL DETAILS===========
47: 2026-05-10 03:36:13.504 INFO: Model configuration extracted from foundation model
48: 2026-05-10 03:36:13.504 INFO: Using weighted loss function for fine-tuning
49: 2026-05-10 03:36:13.504 INFO: Message passing with hidden irreps 128x0e)
52: 2026-05-10 03:36:13.504 INFO: Distance transform for radial basis functions: None
53: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
54:   warnings.warn(
55: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
56:   warnings.warn(
57: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
58:   warnings.warn(
59: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
60:   warnings.warn(
61: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
62:   warnings.warn(
63: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
64:   warnings.warn(
65: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
66:   warnings.warn(
67: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
68:   warnings.warn(
69: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
70:   warnings.warn(
71: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
72:   warnings.warn(
73: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
74:   warnings.warn(
75: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
76:   warnings.warn(
77: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
78:   warnings.warn(
79: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
80:   warnings.warn(
81: 2026-05-10 03:36:15.722 INFO: ===========OPTIMIZER INFORMATION===========
85: 2026-05-10 03:36:15.722 INFO: Learning rate: 0.001, weight decay: 5e-07
86: 2026-05-10 03:36:15.722 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
87: 2026-05-10 03:36:15.723 INFO: === Layer's learning rates ===
92: 2026-05-10 03:36:15.724 INFO: Param group 4: lr = 0.001
93: 2026-05-10 03:36:15.724 INFO: Stage Two (after 150 epochs) with loss function: WeightedEnergyForcesLoss(energy_weight=1000.000, forces_weight=100.000), with energy weight : 1000.0, forces weight : 100.0 and learning rate : 0.0003
94: 2026-05-10 03:36:15.918 INFO: Using gradient clipping with tolerance=10.000
96: 2026-05-10 03:36:15.919 INFO: ===========TRAINING===========
97: 2026-05-10 03:36:15.919 INFO: Started training, reporting errors on validation set
98: 2026-05-10 03:36:15.919 INFO: Loss metrics on validation set
99: 2026-05-10 03:36:22.682 INFO: Initial: head: Default, loss=1.68970534, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
100: 2026-05-10 03:36:57.756 INFO: Epoch 0: head: Default, loss=0.37870810, RMSE_E_per_atom=  297.64 meV, RMSE_F=  193.78 meV / A
101: 2026-05-10 03:48:49.071 INFO: Epoch 25: head: Default, loss=0.16741145, RMSE_E_per_atom=   91.25 meV, RMSE_F=  124.21 meV / A
102: 2026-05-10 04:00:36.670 INFO: Epoch 50: head: Default, loss=0.15414372, RMSE_E_per_atom=   80.92 meV, RMSE_F=  117.96 meV / A
103: 2026-05-10 04:12:23.582 INFO: Epoch 75: head: Default, loss=0.14551337, RMSE_E_per_atom=   87.45 meV, RMSE_F=  117.58 meV / A
104: 2026-05-10 04:24:12.269 INFO: Epoch 100: head: Default, loss=0.14156904, RMSE_E_per_atom=   86.58 meV, RMSE_F=  115.58 meV / A
105: 2026-05-10 04:35:59.845 INFO: Epoch 125: head: Default, loss=0.13951513, RMSE_E_per_atom=   86.23 meV, RMSE_F=  114.00 meV / A
106: 2026-05-10 04:47:24.169 INFO: Changing loss based on Stage Two Weights
107: 2026-05-10 04:47:54.255 INFO: Epoch 150: head: Default, loss=0.53343411, RMSE_E_per_atom=   57.00 meV, RMSE_F=  117.02 meV / A
108: 2026-05-10 04:59:38.411 INFO: Epoch 175: head: Default, loss=0.29406887, RMSE_E_per_atom=   26.43 meV, RMSE_F=  114.63 meV / A
109: 2026-05-10 05:10:48.177 INFO: Training complete
111: 2026-05-10 05:10:48.178 INFO: ===========RESULTS===========
112: 2026-05-10 05:10:48.196 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-125.pt
113: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/tools/checkpoint.py:187: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
114:   torch.load(f=checkpoint_info.path, map_location=device),
115: 2026-05-10 05:10:48.301 INFO: Loaded Stage one model from epoch 125 for evaluation
116: 2026-05-10 05:10:48.301 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42.model
117: 2026-05-10 05:10:48.627 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/models/alloy_mace_stage2_normal_compiled.model
118: 2026-05-10 05:10:50.300 INFO: Computing metrics for training, validation, and test sets
119: 2026-05-10 05:10:50.301 INFO: Skipping evaluation for heads: ['pt_head']
120: 2026-05-10 05:10:50.301 INFO: Evaluating train_Default ...
121: 2026-05-10 05:11:00.355 INFO: Evaluating valid_Default ...
122: 2026-05-10 05:11:02.137 INFO: Error-table on TRAIN and VALID:
123: +---------------+---------------------+------------------+-------------------+
124: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
125: +---------------+---------------------+------------------+-------------------+
126: | train_Default |           88.0      |         85.9     |          9.55     |
127: | valid_Default |           86.2      |        114.0     |         12.85     |
128: +---------------+---------------------+------------------+-------------------+
129: 2026-05-10 05:11:21.157 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-175_swa.pt
130: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/tools/checkpoint.py:187: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
131:   torch.load(f=checkpoint_info.path, map_location=device),
132: 2026-05-10 05:11:21.242 INFO: Loaded Stage two model from epoch 175 for evaluation
133: 2026-05-10 05:11:21.242 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_stagetwo.model
134: 2026-05-10 05:11:21.474 INFO: Compiling model, saving metadata /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/models/alloy_mace_stage2_normal_stagetwo_compiled.model
135: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/torch/jit/_check.py:178: UserWarning: The TorchScript type system doesn't support instance-level annotations on empty non-base types in `__init__`. Instead, either 1) use a type annotation in the class body, or 2) wrap the type in `torch
136:   warnings.warn(
137: 2026-05-10 05:11:22.510 INFO: Computing metrics for training, validation, and test sets
138: 2026-05-10 05:11:22.511 INFO: Skipping evaluation for heads: ['pt_head']
139: 2026-05-10 05:11:22.511 INFO: Evaluating train_Default ...
140: 2026-05-10 05:11:32.486 INFO: Evaluating valid_Default ...
141: 2026-05-10 05:11:34.089 INFO: Error-table on TRAIN and VALID:
142: +---------------+---------------------+------------------+-------------------+
143: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
144: +---------------+---------------------+------------------+-------------------+
145: | train_Default |           38.8      |         88.2     |          9.80     |
146: | valid_Default |           26.4      |        114.6     |         12.92     |
147: +---------------+---------------------+------------------+-------------------+
158: 
159: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
160:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
161: cuequivariance or cuequivariance_torch is not available. Cuequivariance acceleration will be disabled.
162: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/calculators/mace.py:199: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
163:   torch.load(f=model_path, map_location=device)
164: WARNING:root:No dtype selected, switching to float64 to match model dtype.
165: {
