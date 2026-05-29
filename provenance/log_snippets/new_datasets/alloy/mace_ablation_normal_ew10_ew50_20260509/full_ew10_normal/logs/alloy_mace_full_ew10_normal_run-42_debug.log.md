# Log Snippet: repo/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/logs/alloy_mace_full_ew10_normal_run-42_debug.log

Original size: 16500 bytes. Full raw log not copied.

2: 2026-05-10 02:59:55.395 INFO: MACE version: 0.3.15
3: 2026-05-10 02:59:55.395 DEBUG: Configuration: Namespace(config=None, name='alloy_mace_full_ew10_normal', seed=42, work_dir='.', log_dir='/home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/logs', model_dir='/home/brmannanov/coursework/new_datasets/
4: 2026-05-10 02:59:55.465 INFO: CUDA version: 12.4, CUDA device: 0
7: 2026-05-10 02:59:57.566 DEBUG: sys.platform='linux', git_executable='git'
8: 2026-05-10 02:59:57.578 DEBUG: Error accessing Git repository: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal
9: 2026-05-10 02:59:59.285 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
10: 2026-05-10 02:59:59.294 INFO: ===========LOADING INPUT DATA===========
12: 2026-05-10 02:59:59.294 INFO: Using the key specifications to parse data:
13: 2026-05-10 02:59:59.294 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
14: 2026-05-10 02:59:59.294 INFO: =============    Processing head Default     ===========
15: 2026-05-10 02:59:59.296 DEBUG: Loading training file: /home/brmannanov/coursework/new_datasets/alloy/convert/train_alloy.xyz
16: 2026-05-10 03:00:00.155 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
17: 2026-05-10 03:00:00.361 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
18: 2026-05-10 03:00:00.645 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
19: 2026-05-10 03:00:00.657 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
20: 2026-05-10 03:00:00.823 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
21: 2026-05-10 03:00:00.860 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
22: 2026-05-10 03:00:00.909 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
23: 2026-05-10 03:00:00.911 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
24: 2026-05-10 03:00:00.911 INFO: Total number of configurations: train=1210, valid=213, tests=[],
25: 2026-05-10 03:00:00.912 INFO: Using atomic numbers from command line argument
32: 2026-05-10 03:00:08.013 INFO: Combining 1 list datasets for head 'Default'
33: 2026-05-10 03:00:08.829 DEBUG: Successfully loaded validation dataset from ASE files: ['/home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.xyz']
34: 2026-05-10 03:00:08.829 INFO: Combining 1 list datasets for head 'Default_valid'
35: 2026-05-10 03:00:08.829 INFO: Combined validation datasets for Default
36: 2026-05-10 03:00:08.829 INFO: Head 'Default' training dataset size: 1210
38: 2026-05-10 03:00:11.011 INFO: Average number of neighbors: 56.52305706170927
39: 2026-05-10 03:00:11.012 INFO: During training the following quantities will be reported: energy, forces
40: 2026-05-10 03:00:11.012 INFO: ===========MODEL DETAILS===========
43: 2026-05-10 03:00:12.704 INFO: Model configuration extracted from foundation model
44: 2026-05-10 03:00:12.704 INFO: Using weighted loss function for fine-tuning
45: 2026-05-10 03:00:12.704 INFO: Message passing with hidden irreps 128x0e)
53: 2026-05-10 03:00:27.117 INFO: Learning rate: 0.001, weight decay: 5e-07
54: 2026-05-10 03:00:27.117 INFO: WeightedEnergyForcesLoss(energy_weight=10.000, forces_weight=100.000)
55: 2026-05-10 03:00:27.119 INFO: === Layer's learning rates ===
63: 2026-05-10 03:00:27.122 INFO: ===========TRAINING===========
64: 2026-05-10 03:00:27.122 INFO: Started training, reporting errors on validation set
65: 2026-05-10 03:00:27.122 INFO: Loss metrics on validation set
66: 2026-05-10 03:00:41.928 INFO: Initial: head: Default, loss=3.47115944, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
67: 2026-05-10 03:01:19.587 INFO: Epoch 0: head: Default, loss=0.38565270, RMSE_E_per_atom=   78.91 meV, RMSE_F=  195.43 meV / A
68: 2026-05-10 03:01:19.590 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-0.pt
69: 2026-05-10 03:14:16.865 INFO: Epoch 25: head: Default, loss=0.22845447, RMSE_E_per_atom=   54.87 meV, RMSE_F=  124.30 meV / A
70: 2026-05-10 03:14:16.866 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-25.pt
71: 2026-05-10 03:27:23.468 INFO: Epoch 50: head: Default, loss=0.22796134, RMSE_E_per_atom=   32.62 meV, RMSE_F=  119.89 meV / A
72: 2026-05-10 03:27:23.469 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-50.pt
73: 2026-05-10 03:40:47.194 INFO: Epoch 75: head: Default, loss=0.23127289, RMSE_E_per_atom=   43.38 meV, RMSE_F=  119.32 meV / A
74: 2026-05-10 03:40:47.195 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-75.pt
75: 2026-05-10 03:54:00.330 INFO: Epoch 100: head: Default, loss=0.24034409, RMSE_E_per_atom=   43.48 meV, RMSE_F=  117.18 meV / A
76: 2026-05-10 03:54:00.332 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-100.pt
77: 2026-05-10 04:07:26.363 INFO: Epoch 125: head: Default, loss=0.23788896, RMSE_E_per_atom=   29.00 meV, RMSE_F=  115.09 meV / A
78: 2026-05-10 04:07:26.398 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-125.pt
79: 2026-05-10 04:20:55.886 INFO: Epoch 150: head: Default, loss=0.23717604, RMSE_E_per_atom=   37.53 meV, RMSE_F=  115.53 meV / A
80: 2026-05-10 04:20:55.889 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-150.pt
81: 2026-05-10 04:34:22.767 INFO: Epoch 175: head: Default, loss=0.23794774, RMSE_E_per_atom=   39.34 meV, RMSE_F=  113.79 meV / A
82: 2026-05-10 04:34:22.768 DEBUG: Saving checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-175.pt
83: 2026-05-10 04:47:25.584 INFO: Training complete
85: 2026-05-10 04:47:25.585 INFO: ===========RESULTS===========
86: 2026-05-10 04:47:25.626 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-175.pt
87: 2026-05-10 04:47:27.782 INFO: Loaded Stage one model from epoch 175 for evaluation
88: 2026-05-10 04:47:27.782 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42.model
89: 2026-05-10 04:47:31.326 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/models/alloy_mace_full_ew10_normal_compiled.model
90: 2026-05-10 04:47:38.395 INFO: Computing metrics for training, validation, and test sets
91: 2026-05-10 04:47:38.396 INFO: Skipping evaluation for heads: ['pt_head']
92: 2026-05-10 04:47:38.396 INFO: Evaluating train_Default ...
93: 2026-05-10 04:47:56.409 INFO: Evaluating valid_Default ...
94: 2026-05-10 04:47:58.570 INFO: Error-table on TRAIN and VALID:
95: +---------------+---------------------+------------------+-------------------+
96: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
97: +---------------+---------------------+------------------+-------------------+
98: | train_Default |           36.5      |         82.3     |          9.14     |
99: | valid_Default |           39.3      |        113.8     |         12.82     |
100: +---------------+---------------------+------------------+-------------------+
101: 2026-05-10 04:47:58.571 DEBUG: Running inference on train_Default dataset
102: 2026-05-10 04:48:18.842 DEBUG: Running inference on valid_Default dataset
103: 2026-05-10 04:48:34.402 INFO: Done
