# Log Snippet: repo/coursework/new_datasets/alloy/mace_ablation_20260509/freeze1_ew10_normal/logs/alloy_mace_freeze1_ew10_normal_run-42_debug.log

Original size: 16642 bytes. Full raw log not copied.

2: 2026-05-10 07:01:59.448 INFO: MACE version: 0.3.15
3: 2026-05-10 07:01:59.449 DEBUG: Configuration: Namespace(config=None, name='alloy_mace_freeze1_ew10_normal', seed=42, work_dir='.', log_dir='/home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/logs', model_dir='/home/brmannanov/coursework/new_dat
4: 2026-05-10 07:01:59.488 INFO: CUDA version: 12.4, CUDA device: 0
7: 2026-05-10 07:02:00.625 DEBUG: sys.platform='linux', git_executable='git'
8: 2026-05-10 07:02:00.636 DEBUG: Error accessing Git repository: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal
9: 2026-05-10 07:02:01.026 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
10: 2026-05-10 07:02:01.028 INFO: ===========LOADING INPUT DATA===========
12: 2026-05-10 07:02:01.028 INFO: Using the key specifications to parse data:
13: 2026-05-10 07:02:01.028 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
14: 2026-05-10 07:02:01.028 INFO: =============    Processing head Default     ===========
15: 2026-05-10 07:02:01.030 DEBUG: Loading training file: /home/brmannanov/coursework/new_datasets/alloy/convert/train_alloy.xyz
16: 2026-05-10 07:02:01.569 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
17: 2026-05-10 07:02:01.740 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
18: 2026-05-10 07:02:01.957 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
19: 2026-05-10 07:02:01.963 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
20: 2026-05-10 07:02:02.072 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
21: 2026-05-10 07:02:02.103 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
22: 2026-05-10 07:02:02.146 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
23: 2026-05-10 07:02:02.147 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
24: 2026-05-10 07:02:02.148 INFO: Total number of configurations: train=1210, valid=213, tests=[],
25: 2026-05-10 07:02:02.148 INFO: Using atomic numbers from command line argument
32: 2026-05-10 07:02:06.724 INFO: Combining 1 list datasets for head 'Default'
33: 2026-05-10 07:02:07.379 DEBUG: Successfully loaded validation dataset from ASE files: ['/home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.xyz']
34: 2026-05-10 07:02:07.379 INFO: Combining 1 list datasets for head 'Default_valid'
35: 2026-05-10 07:02:07.379 INFO: Combined validation datasets for Default
36: 2026-05-10 07:02:07.380 INFO: Head 'Default' training dataset size: 1210
38: 2026-05-10 07:02:08.606 INFO: Average number of neighbors: 56.52305706170927
39: 2026-05-10 07:02:08.607 INFO: During training the following quantities will be reported: energy, forces
40: 2026-05-10 07:02:08.607 INFO: ===========MODEL DETAILS===========
43: 2026-05-10 07:02:09.772 INFO: Model configuration extracted from foundation model
44: 2026-05-10 07:02:09.772 INFO: Using weighted loss function for fine-tuning
45: 2026-05-10 07:02:09.772 INFO: Message passing with hidden irreps 128x0e)
53: 2026-05-10 07:02:12.562 INFO: Learning rate: 0.001, weight decay: 5e-07
54: 2026-05-10 07:02:12.563 INFO: WeightedEnergyForcesLoss(energy_weight=10.000, forces_weight=100.000)
55: 2026-05-10 07:02:12.564 INFO: Freezing embedding weights
64: 2026-05-10 07:02:12.568 INFO: ===========TRAINING===========
65: 2026-05-10 07:02:12.569 INFO: Started training, reporting errors on validation set
66: 2026-05-10 07:02:12.569 INFO: Loss metrics on validation set
67: 2026-05-10 07:02:18.996 INFO: Initial: head: Default, loss=3.47115944, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
68: 2026-05-10 07:02:54.757 INFO: Epoch 0: head: Default, loss=0.39031749, RMSE_E_per_atom=   86.36 meV, RMSE_F=  195.79 meV / A
69: 2026-05-10 07:02:54.759 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-0.pt
70: 2026-05-10 07:14:41.572 INFO: Epoch 25: head: Default, loss=0.22876924, RMSE_E_per_atom=   54.50 meV, RMSE_F=  124.20 meV / A
71: 2026-05-10 07:14:41.575 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-25.pt
72: 2026-05-10 07:26:28.997 INFO: Epoch 50: head: Default, loss=0.22627333, RMSE_E_per_atom=   31.01 meV, RMSE_F=  119.78 meV / A
73: 2026-05-10 07:26:28.999 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-50.pt
74: 2026-05-10 07:38:14.968 INFO: Epoch 75: head: Default, loss=0.23178888, RMSE_E_per_atom=   41.25 meV, RMSE_F=  119.61 meV / A
75: 2026-05-10 07:38:14.971 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-75.pt
76: 2026-05-10 07:50:00.908 INFO: Epoch 100: head: Default, loss=0.24055243, RMSE_E_per_atom=   40.94 meV, RMSE_F=  117.15 meV / A
77: 2026-05-10 07:50:00.910 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-100.pt
78: 2026-05-10 08:01:48.492 INFO: Epoch 125: head: Default, loss=0.23875017, RMSE_E_per_atom=   27.93 meV, RMSE_F=  115.31 meV / A
79: 2026-05-10 08:01:48.494 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-125.pt
80: 2026-05-10 08:13:41.134 INFO: Epoch 150: head: Default, loss=0.23532471, RMSE_E_per_atom=   37.92 meV, RMSE_F=  115.52 meV / A
81: 2026-05-10 08:13:41.178 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-150.pt
82: 2026-05-10 08:25:26.933 INFO: Epoch 175: head: Default, loss=0.23741250, RMSE_E_per_atom=   38.47 meV, RMSE_F=  114.11 meV / A
83: 2026-05-10 08:25:26.936 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-175.pt
84: 2026-05-10 08:36:38.720 INFO: Training complete
86: 2026-05-10 08:36:38.724 INFO: ===========RESULTS===========
87: 2026-05-10 08:36:38.736 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42_epoch-175.pt
88: 2026-05-10 08:36:39.084 INFO: Loaded Stage one model from epoch 175 for evaluation
89: 2026-05-10 08:36:39.084 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/checkpoints/alloy_mace_freeze1_ew10_normal_run-42.model
90: 2026-05-10 08:36:40.233 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/models/alloy_mace_freeze1_ew10_normal_compiled.model
91: 2026-05-10 08:36:42.657 INFO: Computing metrics for training, validation, and test sets
92: 2026-05-10 08:36:42.658 INFO: Skipping evaluation for heads: ['pt_head']
93: 2026-05-10 08:36:42.659 INFO: Evaluating train_Default ...
94: 2026-05-10 08:36:52.680 INFO: Evaluating valid_Default ...
95: 2026-05-10 08:36:54.392 INFO: Error-table on TRAIN and VALID:
96: +---------------+---------------------+------------------+-------------------+
97: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
98: +---------------+---------------------+------------------+-------------------+
99: | train_Default |           36.2      |         82.4     |          9.15     |
100: | valid_Default |           38.5      |        114.1     |         12.86     |
101: +---------------+---------------------+------------------+-------------------+
102: 2026-05-10 08:36:54.393 DEBUG: Running inference on train_Default dataset
103: 2026-05-10 08:37:05.620 DEBUG: Running inference on valid_Default dataset
104: 2026-05-10 08:37:15.328 INFO: Done
