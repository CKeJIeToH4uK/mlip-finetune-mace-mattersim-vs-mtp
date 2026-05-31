# Log Snippet: repo/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew50_normal/logs/alloy_mace_full_ew50_normal_run-42.log

Original size: 8917 bytes. Full raw log not copied.

3: 2026-05-10 04:52:40.969 INFO: CUDA version: 12.4, CUDA device: 0
4: 2026-05-10 04:52:42.795 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
5: 2026-05-10 04:52:42.797 INFO: ===========LOADING INPUT DATA===========
7: 2026-05-10 04:52:42.798 INFO: Using the key specifications to parse data:
8: 2026-05-10 04:52:42.798 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
9: 2026-05-10 04:52:42.798 INFO: =============    Processing head Default     ===========
10: 2026-05-10 04:52:43.366 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
11: 2026-05-10 04:52:43.556 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
12: 2026-05-10 04:52:43.796 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
13: 2026-05-10 04:52:43.802 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
14: 2026-05-10 04:52:43.917 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
15: 2026-05-10 04:52:43.951 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
16: 2026-05-10 04:52:43.996 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
17: 2026-05-10 04:52:43.997 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
18: 2026-05-10 04:52:43.998 INFO: Total number of configurations: train=1210, valid=213, tests=[],
19: 2026-05-10 04:52:43.998 INFO: Using atomic numbers from command line argument
25: 2026-05-10 04:52:49.251 INFO: Combining 1 list datasets for head 'Default'
26: 2026-05-10 04:52:49.924 INFO: Combining 1 list datasets for head 'Default_valid'
27: 2026-05-10 04:52:49.924 INFO: Combined validation datasets for Default
28: 2026-05-10 04:52:49.925 INFO: Head 'Default' training dataset size: 1210
30: 2026-05-10 04:52:51.005 INFO: Average number of neighbors: 56.52305706170927
31: 2026-05-10 04:52:51.005 INFO: During training the following quantities will be reported: energy, forces
32: 2026-05-10 04:52:51.005 INFO: ===========MODEL DETAILS===========
35: 2026-05-10 04:52:52.311 INFO: Model configuration extracted from foundation model
36: 2026-05-10 04:52:52.311 INFO: Using weighted loss function for fine-tuning
37: 2026-05-10 04:52:52.312 INFO: Message passing with hidden irreps 128x0e)
45: 2026-05-10 04:53:07.018 INFO: Learning rate: 0.001, weight decay: 5e-07
46: 2026-05-10 04:53:07.018 INFO: WeightedEnergyForcesLoss(energy_weight=50.000, forces_weight=100.000)
47: 2026-05-10 04:53:07.019 INFO: === Layer's learning rates ===
55: 2026-05-10 04:53:07.020 INFO: ===========TRAINING===========
56: 2026-05-10 04:53:07.020 INFO: Started training, reporting errors on validation set
57: 2026-05-10 04:53:07.020 INFO: Loss metrics on validation set
58: 2026-05-10 04:53:14.892 INFO: Initial: head: Default, loss=11.38873320, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
59: 2026-05-10 04:54:02.231 INFO: Epoch 0: head: Default, loss=0.45346139, RMSE_E_per_atom=   61.18 meV, RMSE_F=  202.74 meV / A
60: 2026-05-10 05:07:45.117 INFO: Epoch 25: head: Default, loss=0.26979299, RMSE_E_per_atom=   32.16 meV, RMSE_F=  125.75 meV / A
61: 2026-05-10 05:20:58.283 INFO: Epoch 50: head: Default, loss=0.28868670, RMSE_E_per_atom=   48.70 meV, RMSE_F=  120.90 meV / A
62: 2026-05-10 05:34:12.517 INFO: Epoch 75: head: Default, loss=0.27177958, RMSE_E_per_atom=   31.77 meV, RMSE_F=  117.62 meV / A
63: 2026-05-10 05:47:44.512 INFO: Epoch 100: head: Default, loss=0.29011811, RMSE_E_per_atom=   26.26 meV, RMSE_F=  118.70 meV / A
64: 2026-05-10 06:00:46.965 INFO: Epoch 125: head: Default, loss=0.28446121, RMSE_E_per_atom=   25.02 meV, RMSE_F=  116.65 meV / A
65: 2026-05-10 06:14:12.906 INFO: Epoch 150: head: Default, loss=0.26874296, RMSE_E_per_atom=   26.73 meV, RMSE_F=  115.35 meV / A
66: 2026-05-10 06:27:15.697 INFO: Epoch 175: head: Default, loss=0.28971679, RMSE_E_per_atom=   32.62 meV, RMSE_F=  113.90 meV / A
67: 2026-05-10 06:39:48.076 INFO: Training complete
69: 2026-05-10 06:39:48.078 INFO: ===========RESULTS===========
70: 2026-05-10 06:39:48.104 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew50_normal/checkpoints/alloy_mace_full_ew50_normal_run-42_epoch-175.pt
71: 2026-05-10 06:39:48.494 INFO: Loaded Stage one model from epoch 175 for evaluation
72: 2026-05-10 06:39:48.494 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew50_normal/checkpoints/alloy_mace_full_ew50_normal_run-42.model
73: 2026-05-10 06:39:50.101 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509/full_ew50_normal/models/alloy_mace_full_ew50_normal_compiled.model
74: 2026-05-10 06:39:53.167 INFO: Computing metrics for training, validation, and test sets
75: 2026-05-10 06:39:53.168 INFO: Skipping evaluation for heads: ['pt_head']
76: 2026-05-10 06:39:53.168 INFO: Evaluating train_Default ...
77: 2026-05-10 06:40:09.729 INFO: Evaluating valid_Default ...
78: 2026-05-10 06:40:11.515 INFO: Error-table on TRAIN and VALID:
79: +---------------+---------------------+------------------+-------------------+
80: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
81: +---------------+---------------------+------------------+-------------------+
82: | train_Default |           27.5      |         84.2     |          9.35     |
83: | valid_Default |           32.6      |        113.9     |         12.84     |
84: +---------------+---------------------+------------------+-------------------+
