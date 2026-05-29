# Log Snippet: repo/coursework/new_datasets/alloy/mace_ablation_20260509/stage2_normal/logs/alloy_mace_stage2_normal_run-42_debug.log

Original size: 18484 bytes. Full raw log not copied.

3: 2026-05-10 03:36:04.340 INFO: MACE version: 0.3.15
4: 2026-05-10 03:36:04.341 DEBUG: Configuration: Namespace(config=None, name='alloy_mace_stage2_normal', seed=42, work_dir='.', log_dir='/home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/logs', model_dir='/home/brmannanov/coursework/new_datasets/alloy/
5: 2026-05-10 03:36:04.379 INFO: CUDA version: 12.4, CUDA device: 0
8: 2026-05-10 03:36:05.038 DEBUG: sys.platform='linux', git_executable='git'
9: 2026-05-10 03:36:05.049 DEBUG: Error accessing Git repository: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal
10: 2026-05-10 03:36:05.570 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
11: 2026-05-10 03:36:05.572 INFO: ===========LOADING INPUT DATA===========
13: 2026-05-10 03:36:05.572 INFO: Using the key specifications to parse data:
14: 2026-05-10 03:36:05.572 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
15: 2026-05-10 03:36:05.573 INFO: =============    Processing head Default     ===========
16: 2026-05-10 03:36:05.573 DEBUG: Loading training file: /home/brmannanov/coursework/new_datasets/alloy/convert/train_alloy.xyz
17: 2026-05-10 03:36:06.204 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
18: 2026-05-10 03:36:06.394 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
19: 2026-05-10 03:36:06.638 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
20: 2026-05-10 03:36:06.645 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
21: 2026-05-10 03:36:06.792 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
22: 2026-05-10 03:36:06.826 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
23: 2026-05-10 03:36:06.870 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
24: 2026-05-10 03:36:06.871 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
25: 2026-05-10 03:36:06.872 INFO: Total number of configurations: train=1210, valid=213, tests=[],
26: 2026-05-10 03:36:06.872 INFO: Using atomic numbers from command line argument
33: 2026-05-10 03:36:11.173 INFO: Combining 1 list datasets for head 'Default'
34: 2026-05-10 03:36:11.858 DEBUG: Successfully loaded validation dataset from ASE files: ['/home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.xyz']
35: 2026-05-10 03:36:11.858 INFO: Combining 1 list datasets for head 'Default_valid'
36: 2026-05-10 03:36:11.858 INFO: Combined validation datasets for Default
37: 2026-05-10 03:36:11.859 INFO: Head 'Default' training dataset size: 1210
39: 2026-05-10 03:36:12.733 INFO: Average number of neighbors: 56.52305706170927
40: 2026-05-10 03:36:12.733 INFO: During training the following quantities will be reported: energy, forces
41: 2026-05-10 03:36:12.733 INFO: ===========MODEL DETAILS===========
44: 2026-05-10 03:36:13.504 INFO: Model configuration extracted from foundation model
45: 2026-05-10 03:36:13.504 INFO: Using weighted loss function for fine-tuning
46: 2026-05-10 03:36:13.504 INFO: Message passing with hidden irreps 128x0e)
54: 2026-05-10 03:36:15.722 INFO: Learning rate: 0.001, weight decay: 5e-07
55: 2026-05-10 03:36:15.722 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
56: 2026-05-10 03:36:15.723 INFO: === Layer's learning rates ===
61: 2026-05-10 03:36:15.724 INFO: Param group 4: lr = 0.001
62: 2026-05-10 03:36:15.724 INFO: Stage Two (after 150 epochs) with loss function: WeightedEnergyForcesLoss(energy_weight=1000.000, forces_weight=100.000), with energy weight : 1000.0, forces weight : 100.0 and learning rate : 0.0003
63: 2026-05-10 03:36:15.918 INFO: Using gradient clipping with tolerance=10.000
65: 2026-05-10 03:36:15.919 INFO: ===========TRAINING===========
66: 2026-05-10 03:36:15.919 INFO: Started training, reporting errors on validation set
67: 2026-05-10 03:36:15.919 INFO: Loss metrics on validation set
68: 2026-05-10 03:36:22.682 INFO: Initial: head: Default, loss=1.68970534, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
69: 2026-05-10 03:36:57.756 INFO: Epoch 0: head: Default, loss=0.37870810, RMSE_E_per_atom=  297.64 meV, RMSE_F=  193.78 meV / A
70: 2026-05-10 03:36:57.758 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-0.pt
71: 2026-05-10 03:48:49.071 INFO: Epoch 25: head: Default, loss=0.16741145, RMSE_E_per_atom=   91.25 meV, RMSE_F=  124.21 meV / A
72: 2026-05-10 03:48:49.073 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-25.pt
73: 2026-05-10 04:00:36.670 INFO: Epoch 50: head: Default, loss=0.15414372, RMSE_E_per_atom=   80.92 meV, RMSE_F=  117.96 meV / A
74: 2026-05-10 04:00:36.674 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-50.pt
75: 2026-05-10 04:12:23.582 INFO: Epoch 75: head: Default, loss=0.14551337, RMSE_E_per_atom=   87.45 meV, RMSE_F=  117.58 meV / A
76: 2026-05-10 04:12:23.585 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-75.pt
77: 2026-05-10 04:24:12.269 INFO: Epoch 100: head: Default, loss=0.14156904, RMSE_E_per_atom=   86.58 meV, RMSE_F=  115.58 meV / A
78: 2026-05-10 04:24:12.271 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-100.pt
79: 2026-05-10 04:35:59.845 INFO: Epoch 125: head: Default, loss=0.13951513, RMSE_E_per_atom=   86.23 meV, RMSE_F=  114.00 meV / A
80: 2026-05-10 04:35:59.847 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-125.pt
81: 2026-05-10 04:47:24.169 INFO: Changing loss based on Stage Two Weights
82: 2026-05-10 04:47:54.255 INFO: Epoch 150: head: Default, loss=0.53343411, RMSE_E_per_atom=   57.00 meV, RMSE_F=  117.02 meV / A
83: 2026-05-10 04:47:54.258 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-150_swa.pt
84: 2026-05-10 04:59:38.411 INFO: Epoch 175: head: Default, loss=0.29406887, RMSE_E_per_atom=   26.43 meV, RMSE_F=  114.63 meV / A
85: 2026-05-10 04:59:38.414 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-175_swa.pt
86: 2026-05-10 05:10:48.177 INFO: Training complete
88: 2026-05-10 05:10:48.178 INFO: ===========RESULTS===========
89: 2026-05-10 05:10:48.196 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-125.pt
90: 2026-05-10 05:10:48.301 INFO: Loaded Stage one model from epoch 125 for evaluation
91: 2026-05-10 05:10:48.301 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42.model
92: 2026-05-10 05:10:48.627 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/models/alloy_mace_stage2_normal_compiled.model
93: 2026-05-10 05:10:50.300 INFO: Computing metrics for training, validation, and test sets
94: 2026-05-10 05:10:50.301 INFO: Skipping evaluation for heads: ['pt_head']
95: 2026-05-10 05:10:50.301 INFO: Evaluating train_Default ...
96: 2026-05-10 05:11:00.355 INFO: Evaluating valid_Default ...
97: 2026-05-10 05:11:02.137 INFO: Error-table on TRAIN and VALID:
98: +---------------+---------------------+------------------+-------------------+
99: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
100: +---------------+---------------------+------------------+-------------------+
101: | train_Default |           88.0      |         85.9     |          9.55     |
102: | valid_Default |           86.2      |        114.0     |         12.85     |
103: +---------------+---------------------+------------------+-------------------+
104: 2026-05-10 05:11:02.138 DEBUG: Running inference on train_Default dataset
105: 2026-05-10 05:11:13.574 DEBUG: Running inference on valid_Default dataset
106: 2026-05-10 05:11:21.157 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_epoch-175_swa.pt
107: 2026-05-10 05:11:21.242 INFO: Loaded Stage two model from epoch 175 for evaluation
108: 2026-05-10 05:11:21.242 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/checkpoints/alloy_mace_stage2_normal_run-42_stagetwo.model
109: 2026-05-10 05:11:21.474 INFO: Compiling model, saving metadata /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/stage2_normal/models/alloy_mace_stage2_normal_stagetwo_compiled.model
110: 2026-05-10 05:11:22.510 INFO: Computing metrics for training, validation, and test sets
111: 2026-05-10 05:11:22.511 INFO: Skipping evaluation for heads: ['pt_head']
112: 2026-05-10 05:11:22.511 INFO: Evaluating train_Default ...
113: 2026-05-10 05:11:32.486 INFO: Evaluating valid_Default ...
114: 2026-05-10 05:11:34.089 INFO: Error-table on TRAIN and VALID:
115: +---------------+---------------------+------------------+-------------------+
116: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
117: +---------------+---------------------+------------------+-------------------+
118: | train_Default |           38.8      |         88.2     |          9.80     |
119: | valid_Default |           26.4      |        114.6     |         12.92     |
120: +---------------+---------------------+------------------+-------------------+
121: 2026-05-10 05:11:34.090 DEBUG: Running inference on train_Default dataset
122: 2026-05-10 05:11:45.293 DEBUG: Running inference on valid_Default dataset
123: 2026-05-10 05:11:51.310 INFO: Done
