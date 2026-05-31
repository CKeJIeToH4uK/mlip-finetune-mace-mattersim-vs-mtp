# Log Snippet: repo/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/logs/alloy_mace_full_ew10_normal_run-42.log

Original size: 8916 bytes. Full raw log not copied.

3: 2026-05-10 02:59:55.465 INFO: CUDA version: 12.4, CUDA device: 0
4: 2026-05-10 02:59:59.285 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
5: 2026-05-10 02:59:59.294 INFO: ===========LOADING INPUT DATA===========
7: 2026-05-10 02:59:59.294 INFO: Using the key specifications to parse data:
8: 2026-05-10 02:59:59.294 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
9: 2026-05-10 02:59:59.294 INFO: =============    Processing head Default     ===========
10: 2026-05-10 03:00:00.155 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
11: 2026-05-10 03:00:00.361 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
12: 2026-05-10 03:00:00.645 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
13: 2026-05-10 03:00:00.657 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
14: 2026-05-10 03:00:00.823 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
15: 2026-05-10 03:00:00.860 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
16: 2026-05-10 03:00:00.909 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
17: 2026-05-10 03:00:00.911 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
18: 2026-05-10 03:00:00.911 INFO: Total number of configurations: train=1210, valid=213, tests=[],
19: 2026-05-10 03:00:00.912 INFO: Using atomic numbers from command line argument
25: 2026-05-10 03:00:08.013 INFO: Combining 1 list datasets for head 'Default'
26: 2026-05-10 03:00:08.829 INFO: Combining 1 list datasets for head 'Default_valid'
27: 2026-05-10 03:00:08.829 INFO: Combined validation datasets for Default
28: 2026-05-10 03:00:08.829 INFO: Head 'Default' training dataset size: 1210
30: 2026-05-10 03:00:11.011 INFO: Average number of neighbors: 56.52305706170927
31: 2026-05-10 03:00:11.012 INFO: During training the following quantities will be reported: energy, forces
32: 2026-05-10 03:00:11.012 INFO: ===========MODEL DETAILS===========
35: 2026-05-10 03:00:12.704 INFO: Model configuration extracted from foundation model
36: 2026-05-10 03:00:12.704 INFO: Using weighted loss function for fine-tuning
37: 2026-05-10 03:00:12.704 INFO: Message passing with hidden irreps 128x0e)
45: 2026-05-10 03:00:27.117 INFO: Learning rate: 0.001, weight decay: 5e-07
46: 2026-05-10 03:00:27.117 INFO: WeightedEnergyForcesLoss(energy_weight=10.000, forces_weight=100.000)
47: 2026-05-10 03:00:27.119 INFO: === Layer's learning rates ===
55: 2026-05-10 03:00:27.122 INFO: ===========TRAINING===========
56: 2026-05-10 03:00:27.122 INFO: Started training, reporting errors on validation set
57: 2026-05-10 03:00:27.122 INFO: Loss metrics on validation set
58: 2026-05-10 03:00:41.928 INFO: Initial: head: Default, loss=3.47115944, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
59: 2026-05-10 03:01:19.587 INFO: Epoch 0: head: Default, loss=0.38565270, RMSE_E_per_atom=   78.91 meV, RMSE_F=  195.43 meV / A
60: 2026-05-10 03:14:16.865 INFO: Epoch 25: head: Default, loss=0.22845447, RMSE_E_per_atom=   54.87 meV, RMSE_F=  124.30 meV / A
61: 2026-05-10 03:27:23.468 INFO: Epoch 50: head: Default, loss=0.22796134, RMSE_E_per_atom=   32.62 meV, RMSE_F=  119.89 meV / A
62: 2026-05-10 03:40:47.194 INFO: Epoch 75: head: Default, loss=0.23127289, RMSE_E_per_atom=   43.38 meV, RMSE_F=  119.32 meV / A
63: 2026-05-10 03:54:00.330 INFO: Epoch 100: head: Default, loss=0.24034409, RMSE_E_per_atom=   43.48 meV, RMSE_F=  117.18 meV / A
64: 2026-05-10 04:07:26.363 INFO: Epoch 125: head: Default, loss=0.23788896, RMSE_E_per_atom=   29.00 meV, RMSE_F=  115.09 meV / A
65: 2026-05-10 04:20:55.886 INFO: Epoch 150: head: Default, loss=0.23717604, RMSE_E_per_atom=   37.53 meV, RMSE_F=  115.53 meV / A
66: 2026-05-10 04:34:22.767 INFO: Epoch 175: head: Default, loss=0.23794774, RMSE_E_per_atom=   39.34 meV, RMSE_F=  113.79 meV / A
67: 2026-05-10 04:47:25.584 INFO: Training complete
69: 2026-05-10 04:47:25.585 INFO: ===========RESULTS===========
70: 2026-05-10 04:47:25.626 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42_epoch-175.pt
71: 2026-05-10 04:47:27.782 INFO: Loaded Stage one model from epoch 175 for evaluation
72: 2026-05-10 04:47:27.782 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/checkpoints/alloy_mace_full_ew10_normal_run-42.model
73: 2026-05-10 04:47:31.326 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew10_normal/models/alloy_mace_full_ew10_normal_compiled.model
74: 2026-05-10 04:47:38.395 INFO: Computing metrics for training, validation, and test sets
75: 2026-05-10 04:47:38.396 INFO: Skipping evaluation for heads: ['pt_head']
76: 2026-05-10 04:47:38.396 INFO: Evaluating train_Default ...
77: 2026-05-10 04:47:56.409 INFO: Evaluating valid_Default ...
78: 2026-05-10 04:47:58.570 INFO: Error-table on TRAIN and VALID:
79: +---------------+---------------------+------------------+-------------------+
80: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
81: +---------------+---------------------+------------------+-------------------+
82: | train_Default |           36.5      |         82.3     |          9.14     |
83: | valid_Default |           39.3      |        113.8     |         12.82     |
84: +---------------+---------------------+------------------+-------------------+
