# Log Snippet: repo/coursework/logs/smoke_300K_pbc_run-123_debug.log

Original size: 36403 bytes. Full raw log not copied.

2: 2026-02-25 11:24:37.848 INFO: MACE version: 0.3.15
3: 2026-02-25 11:24:37.848 DEBUG: Configuration: Namespace(config=None, name='smoke_300K_pbc', seed=123, work_dir='.', log_dir='./logs', model_dir='.', checkpoints_dir='./checkpoints', results_dir='./results', downloads_dir='./downloads', device='cuda', default_dtype='float64', distributed=False, launc
4: 2026-02-25 11:24:38.006 INFO: CUDA version: 12.4, CUDA device: 0
7: 2026-02-25 11:24:38.649 DEBUG: sys.platform='linux', git_executable='git'
8: 2026-02-25 11:24:38.653 DEBUG: Error accessing Git repository: /home/brmannanov/coursework
9: 2026-02-25 11:24:38.653 INFO: ===========LOADING INPUT DATA===========
11: 2026-02-25 11:24:38.653 INFO: Using the key specifications to parse data:
12: 2026-02-25 11:24:38.653 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
13: 2026-02-25 11:24:38.653 INFO: =============    Processing head Default     ===========
16: 2026-02-25 12:07:51.640 INFO: MACE version: 0.3.15
17: 2026-02-25 12:07:51.641 DEBUG: Configuration: Namespace(config=None, name='smoke_300K_pbc', seed=123, work_dir='.', log_dir='./logs', model_dir='.', checkpoints_dir='./checkpoints', results_dir='./results', downloads_dir='./downloads', device='cuda', default_dtype='float64', distributed=False, launc
18: 2026-02-25 12:07:51.693 INFO: CUDA version: 12.4, CUDA device: 0
21: 2026-02-25 12:07:52.081 DEBUG: sys.platform='linux', git_executable='git'
22: 2026-02-25 12:07:52.086 DEBUG: Error accessing Git repository: /home/brmannanov/coursework
23: 2026-02-25 12:07:52.086 INFO: ===========LOADING INPUT DATA===========
25: 2026-02-25 12:07:52.087 INFO: Using the key specifications to parse data:
26: 2026-02-25 12:07:52.087 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
27: 2026-02-25 12:07:52.087 INFO: =============    Processing head Default     ===========
28: 2026-02-25 12:07:52.089 DEBUG: Loading training file: databases/train_300K.xyz
29: 2026-02-25 12:07:52.289 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
30: 2026-02-25 12:07:52.343 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
31: 2026-02-25 12:07:52.415 INFO: Training set 1/1 [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
32: 2026-02-25 12:07:52.417 INFO: Total Training set [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
33: 2026-02-25 12:07:52.417 INFO: No validation set provided, splitting training data instead.
34: 2026-02-25 12:07:52.421 INFO: Using random 10% of training set for validation with indices saved in: ./smoke_300K_pbc_valid_indices_123.txt
35: 2026-02-25 12:07:52.423 INFO: Random Split Training set [energy: 450, stress: 0, virials: 0, dipole components: 0, head: 450, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 450, charges: 0]
36: 2026-02-25 12:07:52.424 INFO: Random Split Validation set [energy: 50, stress: 0, virials: 0, dipole components: 0, head: 50, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 50, charges: 0]
37: 2026-02-25 12:07:53.048 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
38: 2026-02-25 12:07:53.224 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
39: 2026-02-25 12:07:53.436 INFO: Test set 1/1 [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
40: 2026-02-25 12:07:53.444 INFO: Total Test set [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
41: 2026-02-25 12:07:53.444 INFO: Total number of configurations: train=450, valid=50, tests=[Default_Default: 1669],
42: 2026-02-25 12:07:53.444 INFO: Using atomic numbers from command line argument
45: 2026-02-25 12:40:29.942 INFO: MACE version: 0.3.15
46: 2026-02-25 12:40:29.943 DEBUG: Configuration: Namespace(config=None, name='smoke_300K_pbc', seed=123, work_dir='.', log_dir='./logs', model_dir='.', checkpoints_dir='./checkpoints', results_dir='./results', downloads_dir='./downloads', device='cuda', default_dtype='float64', distributed=False, launc
47: 2026-02-25 12:40:29.988 INFO: CUDA version: 12.4, CUDA device: 0
50: 2026-02-25 12:40:30.632 DEBUG: sys.platform='linux', git_executable='git'
51: 2026-02-25 12:40:30.636 DEBUG: Error accessing Git repository: /home/brmannanov/coursework
52: 2026-02-25 12:40:30.636 INFO: ===========LOADING INPUT DATA===========
54: 2026-02-25 12:40:30.637 INFO: Using the key specifications to parse data:
55: 2026-02-25 12:40:30.637 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
56: 2026-02-25 12:40:30.637 INFO: =============    Processing head Default     ===========
57: 2026-02-25 12:40:30.639 DEBUG: Loading training file: databases/train_300K.xyz
58: 2026-02-25 12:40:30.876 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
59: 2026-02-25 12:40:30.958 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
60: 2026-02-25 12:40:31.059 INFO: Training set 1/1 [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
61: 2026-02-25 12:40:31.063 INFO: Total Training set [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
62: 2026-02-25 12:40:31.063 INFO: No validation set provided, splitting training data instead.
63: 2026-02-25 12:40:31.067 INFO: Using random 10% of training set for validation with indices saved in: ./smoke_300K_pbc_valid_indices_123.txt
64: 2026-02-25 12:40:31.070 INFO: Random Split Training set [energy: 450, stress: 0, virials: 0, dipole components: 0, head: 450, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 450, charges: 0]
65: 2026-02-25 12:40:31.070 INFO: Random Split Validation set [energy: 50, stress: 0, virials: 0, dipole components: 0, head: 50, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 50, charges: 0]
66: 2026-02-25 12:40:31.876 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
67: 2026-02-25 12:40:32.114 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
68: 2026-02-25 12:40:32.409 INFO: Test set 1/1 [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
69: 2026-02-25 12:40:32.418 INFO: Total Test set [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
70: 2026-02-25 12:40:32.418 INFO: Total number of configurations: train=450, valid=50, tests=[Default_Default: 1669],
71: 2026-02-25 12:40:32.418 INFO: Using atomic numbers from command line argument
74: 2026-02-25 12:49:28.961 INFO: MACE version: 0.3.15
75: 2026-02-25 12:49:28.961 DEBUG: Configuration: Namespace(config=None, name='smoke_300K_pbc', seed=123, work_dir='.', log_dir='./logs', model_dir='.', checkpoints_dir='./checkpoints', results_dir='./results', downloads_dir='./downloads', device='cuda', default_dtype='float64', distributed=False, launc
76: 2026-02-25 12:49:28.997 INFO: CUDA version: 12.4, CUDA device: 0
79: 2026-02-25 12:49:29.107 DEBUG: sys.platform='linux', git_executable='git'
80: 2026-02-25 12:49:29.109 DEBUG: Error accessing Git repository: /home/brmannanov/coursework
81: 2026-02-25 12:49:29.110 INFO: ===========LOADING INPUT DATA===========
83: 2026-02-25 12:49:29.110 INFO: Using the key specifications to parse data:
84: 2026-02-25 12:49:29.110 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
85: 2026-02-25 12:49:29.110 INFO: =============    Processing head Default     ===========
86: 2026-02-25 12:49:29.110 DEBUG: Loading training file: databases/train_300K.xyz
87: 2026-02-25 12:49:29.321 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
88: 2026-02-25 12:49:29.401 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
89: 2026-02-25 12:49:29.498 INFO: Training set 1/1 [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
90: 2026-02-25 12:49:29.501 INFO: Total Training set [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
91: 2026-02-25 12:49:29.501 INFO: No validation set provided, splitting training data instead.
92: 2026-02-25 12:49:29.504 INFO: Using random 10% of training set for validation with indices saved in: ./smoke_300K_pbc_valid_indices_123.txt
93: 2026-02-25 12:49:29.507 INFO: Random Split Training set [energy: 450, stress: 0, virials: 0, dipole components: 0, head: 450, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 450, charges: 0]
94: 2026-02-25 12:49:29.508 INFO: Random Split Validation set [energy: 50, stress: 0, virials: 0, dipole components: 0, head: 50, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 50, charges: 0]
95: 2026-02-25 12:49:30.329 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
96: 2026-02-25 12:49:30.600 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
97: 2026-02-25 12:49:30.917 INFO: Test set 1/1 [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
98: 2026-02-25 12:49:30.926 INFO: Total Test set [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
99: 2026-02-25 12:49:30.927 INFO: Total number of configurations: train=450, valid=50, tests=[Default_Default: 1669],
100: 2026-02-25 12:49:30.927 INFO: Using atomic numbers from command line argument
110: 2026-02-25 12:49:34.545 INFO: Average number of neighbors: 16.715608465608465
111: 2026-02-25 12:49:34.545 INFO: During training the following quantities will be reported: energy, forces
112: 2026-02-25 12:49:34.545 INFO: ===========MODEL DETAILS===========
124: 2026-02-25 12:49:39.153 INFO: Learning rate: 0.01, weight decay: 5e-07
125: 2026-02-25 12:49:39.153 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
126: 2026-02-25 12:49:39.154 INFO: === Layer's learning rates ===
134: 2026-02-25 12:49:39.155 INFO: ===========TRAINING===========
135: 2026-02-25 12:49:39.155 INFO: Started training, reporting errors on validation set
136: 2026-02-25 12:49:39.155 INFO: Loss metrics on validation set
137: 2026-02-25 12:49:55.455 INFO: Initial: head: Default, loss=9.30808796, RMSE_E_per_atom=    4.69 meV, RMSE_F=  964.78 meV / A
138: 2026-02-25 12:50:13.230 INFO: Epoch 0: head: Default, loss=0.67630494, RMSE_E_per_atom=  541.24 meV, RMSE_F=  254.36 meV / A
139: 2026-02-25 12:50:13.231 DEBUG: Saving checkpoint: ./checkpoints/smoke_300K_pbc_run-123_epoch-0.pt
140: 2026-02-25 12:50:23.979 INFO: Epoch 1: head: Default, loss=0.31033352, RMSE_E_per_atom=  104.99 meV, RMSE_F=  175.85 meV / A
141: 2026-02-25 12:50:23.980 DEBUG: Deleting old checkpoint file: ./checkpoints/smoke_300K_pbc_run-123_epoch-0.pt
142: 2026-02-25 12:50:23.991 DEBUG: Saving checkpoint: ./checkpoints/smoke_300K_pbc_run-123_epoch-1.pt
143: 2026-02-25 12:50:34.524 INFO: Epoch 2: head: Default, loss=0.14233344, RMSE_E_per_atom=   59.78 meV, RMSE_F=  119.15 meV / A
144: 2026-02-25 12:50:34.526 DEBUG: Deleting old checkpoint file: ./checkpoints/smoke_300K_pbc_run-123_epoch-1.pt
145: 2026-02-25 12:50:34.536 DEBUG: Saving checkpoint: ./checkpoints/smoke_300K_pbc_run-123_epoch-2.pt
146: 2026-02-25 12:50:44.894 INFO: Epoch 3: head: Default, loss=0.15565791, RMSE_E_per_atom=   73.74 meV, RMSE_F=  124.54 meV / A
147: 2026-02-25 12:50:55.230 INFO: Epoch 4: head: Default, loss=0.08899874, RMSE_E_per_atom=    5.96 meV, RMSE_F=   94.34 meV / A
148: 2026-02-25 12:50:55.232 DEBUG: Deleting old checkpoint file: ./checkpoints/smoke_300K_pbc_run-123_epoch-2.pt
149: 2026-02-25 12:50:55.242 DEBUG: Saving checkpoint: ./checkpoints/smoke_300K_pbc_run-123_epoch-4.pt
150: 2026-02-25 12:50:55.337 INFO: Training complete
152: 2026-02-25 12:50:55.338 INFO: ===========RESULTS===========
153: 2026-02-25 12:50:56.745 INFO: Loading checkpoint: ./checkpoints/smoke_300K_pbc_run-123_epoch-4.pt
154: 2026-02-25 12:50:56.923 INFO: Loaded Stage one model from epoch 4 for evaluation
155: 2026-02-25 12:50:56.924 INFO: Saving model to checkpoints/smoke_300K_pbc_run-123.model
156: 2026-02-25 12:50:57.386 INFO: Compiling model, saving metadata to smoke_300K_pbc_compiled.model
157: 2026-02-25 12:50:59.840 INFO: Computing metrics for training, validation, and test sets
158: 2026-02-25 12:50:59.841 INFO: Skipping evaluation for heads: ['pt_head']
159: 2026-02-25 12:50:59.841 INFO: Evaluating train_Default ...
160: 2026-02-25 12:51:05.355 INFO: Evaluating valid_Default ...
161: 2026-02-25 12:51:05.631 INFO: Error-table on TRAIN and VALID:
162: +---------------+---------------------+------------------+-------------------+
163: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
164: +---------------+---------------------+------------------+-------------------+
165: | train_Default |            6.0      |         93.3     |          9.85     |
166: | valid_Default |            6.0      |         94.3     |          9.78     |
167: +---------------+---------------------+------------------+-------------------+
168: 2026-02-25 12:51:05.631 INFO: Evaluating Default_Default ...
169: 2026-02-25 12:51:15.163 INFO: Error-table on TEST:
170: +-----------------+---------------------+------------------+-------------------+
171: |   config_type   | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
172: +-----------------+---------------------+------------------+-------------------+
175: 2026-02-25 12:51:15.164 DEBUG: Running inference on train_Default dataset
176: 2026-02-25 12:51:21.070 DEBUG: Running inference on valid_Default dataset
177: 2026-02-25 12:51:21.332 DEBUG: Running inference on Default_Default dataset
