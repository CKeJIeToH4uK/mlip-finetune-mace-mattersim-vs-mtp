# Log Snippet: repo/coursework/mace_finetune/runs/epoch_vs_err_25/logs/epoch_vs_err_25_run-42.log

Original size: 11261 bytes. Full raw log not copied.

3: 2026-03-18 15:18:18.924 INFO: CUDA version: 12.4, CUDA device: 0
4: 2026-03-18 15:18:22.078 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
5: 2026-03-18 15:18:22.080 INFO: ===========LOADING INPUT DATA===========
7: 2026-03-18 15:18:22.080 INFO: Using the key specifications to parse data:
8: 2026-03-18 15:18:22.080 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
9: 2026-03-18 15:18:22.080 INFO: =============    Processing head Default     ===========
10: 2026-03-18 15:18:22.530 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
11: 2026-03-18 15:18:22.603 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
12: 2026-03-18 15:18:22.712 INFO: Training set 1/1 [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
13: 2026-03-18 15:18:22.715 INFO: Total Training set [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
14: 2026-03-18 15:18:22.715 INFO: No validation set provided, splitting training data instead.
15: 2026-03-18 15:18:22.717 INFO: Using random 5% of training set for validation with indices saved in: ./epoch_vs_err_25_valid_indices_42.txt
16: 2026-03-18 15:18:22.720 INFO: Random Split Training set [energy: 475, stress: 0, virials: 0, dipole components: 0, head: 475, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 475, charges: 0]
17: 2026-03-18 15:18:22.721 INFO: Random Split Validation set [energy: 25, stress: 0, virials: 0, dipole components: 0, head: 25, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 25, charges: 0]
18: 2026-03-18 15:18:23.510 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
19: 2026-03-18 15:18:23.763 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
20: 2026-03-18 15:18:24.074 INFO: Test set 1/1 [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
21: 2026-03-18 15:18:24.084 INFO: Total Test set [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
22: 2026-03-18 15:18:24.084 INFO: Total number of configurations: train=475, valid=25, tests=[Default_Default: 1669],
23: 2026-03-18 15:18:24.085 INFO: Using atomic numbers from command line argument
32: 2026-03-18 15:18:27.490 INFO: Average number of neighbors: 20.47470238095238
33: 2026-03-18 15:18:27.491 INFO: During training the following quantities will be reported: energy, forces
34: 2026-03-18 15:18:27.491 INFO: ===========MODEL DETAILS===========
37: 2026-03-18 15:18:28.085 INFO: Model configuration extracted from foundation model
38: 2026-03-18 15:18:28.085 INFO: Using weighted loss function for fine-tuning
39: 2026-03-18 15:18:28.085 INFO: Message passing with hidden irreps 128x0e)
47: 2026-03-18 15:18:38.309 INFO: Learning rate: 0.01, weight decay: 5e-07
48: 2026-03-18 15:18:38.309 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
49: 2026-03-18 15:18:38.311 INFO: === Layer's learning rates ===
57: 2026-03-18 15:18:38.312 INFO: ===========TRAINING===========
58: 2026-03-18 15:18:38.312 INFO: Started training, reporting errors on validation set
59: 2026-03-18 15:18:38.312 INFO: Loss metrics on validation set
60: 2026-03-18 15:18:49.550 INFO: Initial: head: Default, loss=1.92412590, RMSE_E_per_atom=  276.31 meV, RMSE_F=  404.35 meV / A
61: 2026-03-18 15:19:00.010 INFO: Epoch 0: head: Default, loss=1.99465336, RMSE_E_per_atom=   54.74 meV, RMSE_F=  405.85 meV / A
62: 2026-03-18 15:19:53.681 INFO: Epoch 25: head: Default, loss=0.08188718, RMSE_E_per_atom=   10.08 meV, RMSE_F=   82.02 meV / A
63: 2026-03-18 15:20:48.179 INFO: Epoch 50: head: Default, loss=0.04358364, RMSE_E_per_atom=    5.90 meV, RMSE_F=   59.81 meV / A
64: 2026-03-18 15:21:42.455 INFO: Epoch 75: head: Default, loss=0.04231605, RMSE_E_per_atom=    0.80 meV, RMSE_F=   58.73 meV / A
65: 2026-03-18 15:22:34.749 INFO: Epoch 100: head: Default, loss=0.01938021, RMSE_E_per_atom=    2.65 meV, RMSE_F=   39.48 meV / A
66: 2026-03-18 15:23:26.775 INFO: Epoch 125: head: Default, loss=0.02004865, RMSE_E_per_atom=    1.41 meV, RMSE_F=   40.27 meV / A
67: 2026-03-18 15:24:19.345 INFO: Epoch 150: head: Default, loss=0.01488227, RMSE_E_per_atom=    7.27 meV, RMSE_F=   34.40 meV / A
68: 2026-03-18 15:25:12.125 INFO: Epoch 175: head: Default, loss=0.01497114, RMSE_E_per_atom=    1.79 meV, RMSE_F=   34.65 meV / A
69: 2026-03-18 15:26:04.333 INFO: Epoch 200: head: Default, loss=0.01368140, RMSE_E_per_atom=    0.79 meV, RMSE_F=   33.31 meV / A
70: 2026-03-18 15:26:57.772 INFO: Epoch 225: head: Default, loss=0.01366800, RMSE_E_per_atom=    1.14 meV, RMSE_F=   33.52 meV / A
71: 2026-03-18 15:27:49.977 INFO: Epoch 250: head: Default, loss=0.01513657, RMSE_E_per_atom=    0.51 meV, RMSE_F=   34.96 meV / A
72: 2026-03-18 15:28:42.569 INFO: Epoch 275: head: Default, loss=0.01091263, RMSE_E_per_atom=    0.87 meV, RMSE_F=   29.73 meV / A
73: 2026-03-18 15:29:36.232 INFO: Epoch 300: head: Default, loss=0.01339592, RMSE_E_per_atom=    3.82 meV, RMSE_F=   33.13 meV / A
74: 2026-03-18 15:30:31.615 INFO: Epoch 325: head: Default, loss=0.01015600, RMSE_E_per_atom=    2.94 meV, RMSE_F=   28.74 meV / A
75: 2026-03-18 15:31:24.733 INFO: Epoch 350: head: Default, loss=0.01150950, RMSE_E_per_atom=    0.61 meV, RMSE_F=   30.53 meV / A
76: 2026-03-18 15:32:16.290 INFO: Epoch 375: head: Default, loss=0.01357597, RMSE_E_per_atom=    4.50 meV, RMSE_F=   33.32 meV / A
77: 2026-03-18 15:33:11.539 INFO: Epoch 400: head: Default, loss=0.00855676, RMSE_E_per_atom=    0.95 meV, RMSE_F=   26.40 meV / A
78: 2026-03-18 15:34:03.158 INFO: Epoch 425: head: Default, loss=0.00866992, RMSE_E_per_atom=    0.55 meV, RMSE_F=   26.55 meV / A
79: 2026-03-18 15:34:54.320 INFO: Epoch 450: head: Default, loss=0.01050917, RMSE_E_per_atom=    1.89 meV, RMSE_F=   29.38 meV / A
80: 2026-03-18 15:35:45.670 INFO: Epoch 475: head: Default, loss=0.00747206, RMSE_E_per_atom=    0.51 meV, RMSE_F=   24.53 meV / A
81: 2026-03-18 15:36:35.890 INFO: Training complete
83: 2026-03-18 15:36:35.891 INFO: ===========RESULTS===========
84: 2026-03-18 15:36:37.053 INFO: Loading checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-475.pt
85: 2026-03-18 15:36:37.112 INFO: Loaded Stage one model from epoch 475 for evaluation
86: 2026-03-18 15:36:37.112 INFO: Saving model to /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42.model
87: 2026-03-18 15:36:37.507 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/models/epoch_vs_err_25_compiled.model
88: 2026-03-18 15:36:40.313 INFO: Computing metrics for training, validation, and test sets
89: 2026-03-18 15:36:40.314 INFO: Skipping evaluation for heads: ['pt_head']
90: 2026-03-18 15:36:40.314 INFO: Evaluating train_Default ...
91: 2026-03-18 15:36:41.076 INFO: Evaluating valid_Default ...
92: 2026-03-18 15:36:41.482 INFO: Error-table on TRAIN and VALID:
93: +---------------+---------------------+------------------+-------------------+
94: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
95: +---------------+---------------------+------------------+-------------------+
96: | train_Default |            0.5      |         19.0     |          2.00     |
97: | valid_Default |            0.5      |         24.5     |          2.72     |
98: +---------------+---------------------+------------------+-------------------+
99: 2026-03-18 15:36:41.482 INFO: Evaluating Default_Default ...
100: 2026-03-18 15:36:47.673 INFO: Error-table on TEST:
101: +-----------------+---------------------+------------------+-------------------+
102: |   config_type   | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
103: +-----------------+---------------------+------------------+-------------------+
