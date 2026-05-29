# Log Snippet: repo/coursework/mace_finetune/runs/epoch_vs_err_25/logs/epoch_vs_err_25_run-42_debug.log

Original size: 19893 bytes. Full raw log not copied.

2: 2026-03-18 15:18:18.863 INFO: MACE version: 0.3.15
3: 2026-03-18 15:18:18.863 DEBUG: Configuration: Namespace(config=None, name='epoch_vs_err_25', seed=42, work_dir='.', log_dir='/home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/logs', model_dir='/home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/models', checkpoints_dir='/home
4: 2026-03-18 15:18:18.924 INFO: CUDA version: 12.4, CUDA device: 0
5: 2026-03-18 15:18:20.759 DEBUG: Popen(['git', 'version'], cwd=/home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25, stdin=None, shell=False, universal_newlines=False)
6: 2026-03-18 15:18:20.767 DEBUG: Popen(['git', 'version'], cwd=/home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25, stdin=None, shell=False, universal_newlines=False)
7: 2026-03-18 15:18:20.772 DEBUG: sys.platform='linux', git_executable='git'
8: 2026-03-18 15:18:20.781 DEBUG: Error accessing Git repository: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25
9: 2026-03-18 15:18:22.078 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
10: 2026-03-18 15:18:22.080 INFO: ===========LOADING INPUT DATA===========
12: 2026-03-18 15:18:22.080 INFO: Using the key specifications to parse data:
13: 2026-03-18 15:18:22.080 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
14: 2026-03-18 15:18:22.080 INFO: =============    Processing head Default     ===========
15: 2026-03-18 15:18:22.083 DEBUG: Loading training file: /home/brmannanov/coursework/databases/train_300K.xyz
16: 2026-03-18 15:18:22.530 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
17: 2026-03-18 15:18:22.603 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
18: 2026-03-18 15:18:22.712 INFO: Training set 1/1 [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
19: 2026-03-18 15:18:22.715 INFO: Total Training set [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
20: 2026-03-18 15:18:22.715 INFO: No validation set provided, splitting training data instead.
21: 2026-03-18 15:18:22.717 INFO: Using random 5% of training set for validation with indices saved in: ./epoch_vs_err_25_valid_indices_42.txt
22: 2026-03-18 15:18:22.720 INFO: Random Split Training set [energy: 475, stress: 0, virials: 0, dipole components: 0, head: 475, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 475, charges: 0]
23: 2026-03-18 15:18:22.721 INFO: Random Split Validation set [energy: 25, stress: 0, virials: 0, dipole components: 0, head: 25, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 25, charges: 0]
24: 2026-03-18 15:18:23.510 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
25: 2026-03-18 15:18:23.763 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
26: 2026-03-18 15:18:24.074 INFO: Test set 1/1 [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
27: 2026-03-18 15:18:24.084 INFO: Total Test set [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
28: 2026-03-18 15:18:24.084 INFO: Total number of configurations: train=475, valid=25, tests=[Default_Default: 1669],
29: 2026-03-18 15:18:24.085 INFO: Using atomic numbers from command line argument
39: 2026-03-18 15:18:27.490 INFO: Average number of neighbors: 20.47470238095238
40: 2026-03-18 15:18:27.491 INFO: During training the following quantities will be reported: energy, forces
41: 2026-03-18 15:18:27.491 INFO: ===========MODEL DETAILS===========
44: 2026-03-18 15:18:28.085 INFO: Model configuration extracted from foundation model
45: 2026-03-18 15:18:28.085 INFO: Using weighted loss function for fine-tuning
46: 2026-03-18 15:18:28.085 INFO: Message passing with hidden irreps 128x0e)
54: 2026-03-18 15:18:38.309 INFO: Learning rate: 0.01, weight decay: 5e-07
55: 2026-03-18 15:18:38.309 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
56: 2026-03-18 15:18:38.311 INFO: === Layer's learning rates ===
64: 2026-03-18 15:18:38.312 INFO: ===========TRAINING===========
65: 2026-03-18 15:18:38.312 INFO: Started training, reporting errors on validation set
66: 2026-03-18 15:18:38.312 INFO: Loss metrics on validation set
67: 2026-03-18 15:18:49.550 INFO: Initial: head: Default, loss=1.92412590, RMSE_E_per_atom=  276.31 meV, RMSE_F=  404.35 meV / A
68: 2026-03-18 15:19:00.010 INFO: Epoch 0: head: Default, loss=1.99465336, RMSE_E_per_atom=   54.74 meV, RMSE_F=  405.85 meV / A
69: 2026-03-18 15:19:00.012 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-0.pt
70: 2026-03-18 15:19:53.681 INFO: Epoch 25: head: Default, loss=0.08188718, RMSE_E_per_atom=   10.08 meV, RMSE_F=   82.02 meV / A
71: 2026-03-18 15:19:53.683 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-25.pt
72: 2026-03-18 15:20:48.179 INFO: Epoch 50: head: Default, loss=0.04358364, RMSE_E_per_atom=    5.90 meV, RMSE_F=   59.81 meV / A
73: 2026-03-18 15:20:48.180 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-50.pt
74: 2026-03-18 15:21:42.455 INFO: Epoch 75: head: Default, loss=0.04231605, RMSE_E_per_atom=    0.80 meV, RMSE_F=   58.73 meV / A
75: 2026-03-18 15:21:42.459 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-75.pt
76: 2026-03-18 15:22:34.749 INFO: Epoch 100: head: Default, loss=0.01938021, RMSE_E_per_atom=    2.65 meV, RMSE_F=   39.48 meV / A
77: 2026-03-18 15:22:34.751 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-100.pt
78: 2026-03-18 15:23:26.775 INFO: Epoch 125: head: Default, loss=0.02004865, RMSE_E_per_atom=    1.41 meV, RMSE_F=   40.27 meV / A
79: 2026-03-18 15:23:26.777 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-125.pt
80: 2026-03-18 15:24:19.345 INFO: Epoch 150: head: Default, loss=0.01488227, RMSE_E_per_atom=    7.27 meV, RMSE_F=   34.40 meV / A
81: 2026-03-18 15:24:19.347 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-150.pt
82: 2026-03-18 15:25:12.125 INFO: Epoch 175: head: Default, loss=0.01497114, RMSE_E_per_atom=    1.79 meV, RMSE_F=   34.65 meV / A
83: 2026-03-18 15:25:12.127 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-175.pt
84: 2026-03-18 15:26:04.333 INFO: Epoch 200: head: Default, loss=0.01368140, RMSE_E_per_atom=    0.79 meV, RMSE_F=   33.31 meV / A
85: 2026-03-18 15:26:04.336 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-200.pt
86: 2026-03-18 15:26:57.772 INFO: Epoch 225: head: Default, loss=0.01366800, RMSE_E_per_atom=    1.14 meV, RMSE_F=   33.52 meV / A
87: 2026-03-18 15:26:57.773 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-225.pt
88: 2026-03-18 15:27:49.977 INFO: Epoch 250: head: Default, loss=0.01513657, RMSE_E_per_atom=    0.51 meV, RMSE_F=   34.96 meV / A
89: 2026-03-18 15:27:49.978 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-250.pt
90: 2026-03-18 15:28:42.569 INFO: Epoch 275: head: Default, loss=0.01091263, RMSE_E_per_atom=    0.87 meV, RMSE_F=   29.73 meV / A
91: 2026-03-18 15:28:42.571 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-275.pt
92: 2026-03-18 15:29:36.232 INFO: Epoch 300: head: Default, loss=0.01339592, RMSE_E_per_atom=    3.82 meV, RMSE_F=   33.13 meV / A
93: 2026-03-18 15:29:36.234 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-300.pt
94: 2026-03-18 15:30:31.615 INFO: Epoch 325: head: Default, loss=0.01015600, RMSE_E_per_atom=    2.94 meV, RMSE_F=   28.74 meV / A
95: 2026-03-18 15:30:31.617 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-325.pt
96: 2026-03-18 15:31:24.733 INFO: Epoch 350: head: Default, loss=0.01150950, RMSE_E_per_atom=    0.61 meV, RMSE_F=   30.53 meV / A
97: 2026-03-18 15:31:24.735 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-350.pt
98: 2026-03-18 15:32:16.290 INFO: Epoch 375: head: Default, loss=0.01357597, RMSE_E_per_atom=    4.50 meV, RMSE_F=   33.32 meV / A
99: 2026-03-18 15:32:16.291 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-375.pt
100: 2026-03-18 15:33:11.539 INFO: Epoch 400: head: Default, loss=0.00855676, RMSE_E_per_atom=    0.95 meV, RMSE_F=   26.40 meV / A
101: 2026-03-18 15:33:11.540 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-400.pt
102: 2026-03-18 15:34:03.158 INFO: Epoch 425: head: Default, loss=0.00866992, RMSE_E_per_atom=    0.55 meV, RMSE_F=   26.55 meV / A
103: 2026-03-18 15:34:03.159 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-425.pt
104: 2026-03-18 15:34:54.320 INFO: Epoch 450: head: Default, loss=0.01050917, RMSE_E_per_atom=    1.89 meV, RMSE_F=   29.38 meV / A
105: 2026-03-18 15:34:54.322 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-450.pt
106: 2026-03-18 15:35:45.670 INFO: Epoch 475: head: Default, loss=0.00747206, RMSE_E_per_atom=    0.51 meV, RMSE_F=   24.53 meV / A
107: 2026-03-18 15:35:45.671 DEBUG: Saving checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-475.pt
108: 2026-03-18 15:36:35.890 INFO: Training complete
110: 2026-03-18 15:36:35.891 INFO: ===========RESULTS===========
111: 2026-03-18 15:36:37.053 INFO: Loading checkpoint: /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42_epoch-475.pt
112: 2026-03-18 15:36:37.112 INFO: Loaded Stage one model from epoch 475 for evaluation
113: 2026-03-18 15:36:37.112 INFO: Saving model to /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/checkpoints/epoch_vs_err_25_run-42.model
114: 2026-03-18 15:36:37.507 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/mace_finetune/runs/epoch_vs_err_25/models/epoch_vs_err_25_compiled.model
115: 2026-03-18 15:36:40.313 INFO: Computing metrics for training, validation, and test sets
116: 2026-03-18 15:36:40.314 INFO: Skipping evaluation for heads: ['pt_head']
117: 2026-03-18 15:36:40.314 INFO: Evaluating train_Default ...
118: 2026-03-18 15:36:41.076 INFO: Evaluating valid_Default ...
119: 2026-03-18 15:36:41.482 INFO: Error-table on TRAIN and VALID:
120: +---------------+---------------------+------------------+-------------------+
121: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
122: +---------------+---------------------+------------------+-------------------+
123: | train_Default |            0.5      |         19.0     |          2.00     |
124: | valid_Default |            0.5      |         24.5     |          2.72     |
125: +---------------+---------------------+------------------+-------------------+
126: 2026-03-18 15:36:41.482 INFO: Evaluating Default_Default ...
127: 2026-03-18 15:36:47.673 INFO: Error-table on TEST:
128: +-----------------+---------------------+------------------+-------------------+
129: |   config_type   | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
130: +-----------------+---------------------+------------------+-------------------+
133: 2026-03-18 15:36:47.673 DEBUG: Running inference on train_Default dataset
134: 2026-03-18 15:36:48.392 DEBUG: Running inference on valid_Default dataset
135: 2026-03-18 15:36:48.493 DEBUG: Running inference on Default_Default dataset
