# Log Snippet: repo/coursework/mace_finetune/ft_300K/logs/ft_300K_run-42_debug.log

Original size: 96678 bytes. Full raw log not copied.

2: 2026-02-25 13:25:19.436 INFO: MACE version: 0.3.15
3: 2026-02-25 13:25:19.437 DEBUG: Configuration: Namespace(config=None, name='ft_300K', seed=42, work_dir='.', log_dir='./logs', model_dir='.', checkpoints_dir='./checkpoints', results_dir='./results', downloads_dir='./downloads', device='cuda', default_dtype='float64', distributed=False, launcher='slu
4: 2026-02-25 13:25:19.499 INFO: CUDA version: 12.4, CUDA device: 0
7: 2026-02-25 13:25:20.222 DEBUG: sys.platform='linux', git_executable='git'
8: 2026-02-25 13:25:20.229 DEBUG: Error accessing Git repository: /home/brmannanov/coursework/mace_finetune/ft_300K
9: 2026-02-25 13:25:20.229 INFO: Using foundation model mace small as initial checkpoint.
11: 2026-02-25 13:41:37.131 INFO: MACE version: 0.3.15
12: 2026-02-25 13:41:37.131 DEBUG: Configuration: Namespace(config=None, name='ft_300K', seed=42, work_dir='.', log_dir='./logs', model_dir='.', checkpoints_dir='./checkpoints', results_dir='./results', downloads_dir='./downloads', device='cuda', default_dtype='float64', distributed=False, launcher='slu
13: 2026-02-25 13:41:37.228 INFO: CUDA version: 12.4, CUDA device: 0
16: 2026-02-25 13:41:38.237 DEBUG: sys.platform='linux', git_executable='git'
17: 2026-02-25 13:41:38.245 DEBUG: Error accessing Git repository: /home/brmannanov/coursework/mace_finetune/ft_300K
18: 2026-02-25 13:41:38.245 INFO: Using foundation model mace small as initial checkpoint.
20: 2026-02-25 13:49:09.865 INFO: MACE version: 0.3.15
21: 2026-02-25 13:49:09.866 DEBUG: Configuration: Namespace(config=None, name='ft_300K', seed=42, work_dir='.', log_dir='./logs', model_dir='.', checkpoints_dir='./checkpoints', results_dir='./results', downloads_dir='./downloads', device='cuda', default_dtype='float64', distributed=False, launcher='slu
22: 2026-02-25 13:49:09.909 INFO: CUDA version: 12.4, CUDA device: 0
25: 2026-02-25 13:49:10.242 DEBUG: sys.platform='linux', git_executable='git'
26: 2026-02-25 13:49:10.249 DEBUG: Error accessing Git repository: /home/brmannanov/coursework/mace_finetune/ft_300K
27: 2026-02-25 13:49:11.640 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
28: 2026-02-25 13:49:11.655 INFO: ===========LOADING INPUT DATA===========
30: 2026-02-25 13:49:11.655 INFO: Using the key specifications to parse data:
31: 2026-02-25 13:49:11.655 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
32: 2026-02-25 13:49:11.655 INFO: =============    Processing head Default     ===========
33: 2026-02-25 13:49:11.657 DEBUG: Loading training file: /home/brmannanov/coursework/databases/train_300K.xyz
34: 2026-02-25 13:49:11.983 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
35: 2026-02-25 13:49:12.051 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
36: 2026-02-25 13:49:12.133 INFO: Training set 1/1 [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
37: 2026-02-25 13:49:12.135 INFO: Total Training set [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
38: 2026-02-25 13:49:12.135 INFO: No validation set provided, splitting training data instead.
39: 2026-02-25 13:49:12.139 INFO: Using random 5% of training set for validation with indices saved in: ./ft_300K_valid_indices_42.txt
40: 2026-02-25 13:49:12.147 INFO: Random Split Training set [energy: 475, stress: 0, virials: 0, dipole components: 0, head: 475, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 475, charges: 0]
41: 2026-02-25 13:49:12.148 INFO: Random Split Validation set [energy: 25, stress: 0, virials: 0, dipole components: 0, head: 25, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 25, charges: 0]
42: 2026-02-25 13:49:12.892 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
43: 2026-02-25 13:49:13.083 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
44: 2026-02-25 13:49:13.313 INFO: Test set 1/1 [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
45: 2026-02-25 13:49:13.320 INFO: Total Test set [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
46: 2026-02-25 13:49:13.320 INFO: Total number of configurations: train=475, valid=25, tests=[Default_Default: 1669],
47: 2026-02-25 13:49:13.321 INFO: Using atomic numbers from command line argument
57: 2026-02-25 13:49:15.511 INFO: Average number of neighbors: 20.47470238095238
58: 2026-02-25 13:49:15.512 INFO: During training the following quantities will be reported: energy, forces
59: 2026-02-25 13:49:15.512 INFO: ===========MODEL DETAILS===========
62: 2026-02-25 13:49:16.168 INFO: Model configuration extracted from foundation model
63: 2026-02-25 13:49:16.168 INFO: Using weighted loss function for fine-tuning
64: 2026-02-25 13:49:16.168 INFO: Message passing with hidden irreps 128x0e)
72: 2026-02-25 13:49:22.789 INFO: Learning rate: 0.01, weight decay: 5e-07
73: 2026-02-25 13:49:22.790 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
74: 2026-02-25 13:49:22.792 INFO: === Layer's learning rates ===
82: 2026-02-25 13:49:22.794 INFO: ===========TRAINING===========
83: 2026-02-25 13:49:22.794 INFO: Started training, reporting errors on validation set
84: 2026-02-25 13:49:22.794 INFO: Loss metrics on validation set
85: 2026-02-25 13:49:37.362 INFO: Initial: head: Default, loss=1.92412590, RMSE_E_per_atom=  276.31 meV, RMSE_F=  404.35 meV / A
86: 2026-02-25 13:49:45.983 INFO: Epoch 0: head: Default, loss=1.99465336, RMSE_E_per_atom=   54.74 meV, RMSE_F=  405.85 meV / A
87: 2026-02-25 13:49:45.985 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-0.pt
88: 2026-02-25 13:49:48.496 INFO: Epoch 1: head: Default, loss=0.53195376, RMSE_E_per_atom=   30.81 meV, RMSE_F=  210.86 meV / A
89: 2026-02-25 13:49:48.498 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-0.pt
90: 2026-02-25 13:49:48.501 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-1.pt
91: 2026-02-25 13:49:50.606 INFO: Epoch 2: head: Default, loss=0.66904881, RMSE_E_per_atom=   21.52 meV, RMSE_F=  234.99 meV / A
92: 2026-02-25 13:49:52.632 INFO: Epoch 3: head: Default, loss=0.37812980, RMSE_E_per_atom=   23.47 meV, RMSE_F=  176.35 meV / A
93: 2026-02-25 13:49:52.633 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-1.pt
94: 2026-02-25 13:49:52.637 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-3.pt
95: 2026-02-25 13:49:54.699 INFO: Epoch 4: head: Default, loss=0.32471338, RMSE_E_per_atom=   12.30 meV, RMSE_F=  164.74 meV / A
96: 2026-02-25 13:49:54.700 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-3.pt
97: 2026-02-25 13:49:54.705 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-4.pt
98: 2026-02-25 13:49:56.747 INFO: Epoch 5: head: Default, loss=0.21654166, RMSE_E_per_atom=   16.85 meV, RMSE_F=  133.25 meV / A
99: 2026-02-25 13:49:56.748 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-4.pt
100: 2026-02-25 13:49:56.751 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-5.pt
101: 2026-02-25 13:49:58.794 INFO: Epoch 6: head: Default, loss=0.18049867, RMSE_E_per_atom=    4.57 meV, RMSE_F=  122.01 meV / A
102: 2026-02-25 13:49:58.796 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-5.pt
103: 2026-02-25 13:49:58.800 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-6.pt
104: 2026-02-25 13:50:00.928 INFO: Epoch 7: head: Default, loss=0.25657002, RMSE_E_per_atom=    6.87 meV, RMSE_F=  145.31 meV / A
105: 2026-02-25 13:50:02.905 INFO: Epoch 8: head: Default, loss=0.25355030, RMSE_E_per_atom=    2.04 meV, RMSE_F=  144.39 meV / A
106: 2026-02-25 13:50:04.878 INFO: Epoch 9: head: Default, loss=0.12801723, RMSE_E_per_atom=    5.80 meV, RMSE_F=  102.38 meV / A
107: 2026-02-25 13:50:04.879 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-6.pt
108: 2026-02-25 13:50:04.885 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-9.pt
109: 2026-02-25 13:50:06.956 INFO: Epoch 10: head: Default, loss=0.21522380, RMSE_E_per_atom=    7.57 meV, RMSE_F=  132.60 meV / A
110: 2026-02-25 13:50:08.962 INFO: Epoch 11: head: Default, loss=0.12527059, RMSE_E_per_atom=    4.94 meV, RMSE_F=  101.90 meV / A
111: 2026-02-25 13:50:08.963 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-9.pt
112: 2026-02-25 13:50:08.966 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-11.pt
113: 2026-02-25 13:50:11.179 INFO: Epoch 12: head: Default, loss=0.11556768, RMSE_E_per_atom=    4.39 meV, RMSE_F=   96.86 meV / A
114: 2026-02-25 13:50:11.180 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-11.pt
115: 2026-02-25 13:50:11.185 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-12.pt
116: 2026-02-25 13:50:13.568 INFO: Epoch 13: head: Default, loss=0.16970550, RMSE_E_per_atom=    6.37 meV, RMSE_F=  118.03 meV / A
117: 2026-02-25 13:50:15.907 INFO: Epoch 14: head: Default, loss=0.16434239, RMSE_E_per_atom=   16.96 meV, RMSE_F=  116.05 meV / A
118: 2026-02-25 13:50:18.275 INFO: Epoch 15: head: Default, loss=0.14253747, RMSE_E_per_atom=    5.61 meV, RMSE_F=  108.38 meV / A
119: 2026-02-25 13:50:20.626 INFO: Epoch 16: head: Default, loss=0.10279813, RMSE_E_per_atom=   11.48 meV, RMSE_F=   92.40 meV / A
120: 2026-02-25 13:50:20.628 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-12.pt
121: 2026-02-25 13:50:20.634 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-16.pt
122: 2026-02-25 13:50:23.013 INFO: Epoch 17: head: Default, loss=0.13134738, RMSE_E_per_atom=    9.74 meV, RMSE_F=  103.20 meV / A
123: 2026-02-25 13:50:25.315 INFO: Epoch 18: head: Default, loss=0.15121359, RMSE_E_per_atom=    8.33 meV, RMSE_F=  110.83 meV / A
124: 2026-02-25 13:50:27.607 INFO: Epoch 19: head: Default, loss=0.06307120, RMSE_E_per_atom=    5.07 meV, RMSE_F=   71.55 meV / A
125: 2026-02-25 13:50:27.608 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-16.pt
126: 2026-02-25 13:50:27.612 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-19.pt
127: 2026-02-25 13:50:29.926 INFO: Epoch 20: head: Default, loss=0.16323715, RMSE_E_per_atom=    2.25 meV, RMSE_F=  116.46 meV / A
128: 2026-02-25 13:50:32.204 INFO: Epoch 21: head: Default, loss=0.10425535, RMSE_E_per_atom=    1.72 meV, RMSE_F=   92.57 meV / A
129: 2026-02-25 13:50:34.489 INFO: Epoch 22: head: Default, loss=0.08872654, RMSE_E_per_atom=    4.74 meV, RMSE_F=   85.92 meV / A
130: 2026-02-25 13:50:36.803 INFO: Epoch 23: head: Default, loss=0.06373223, RMSE_E_per_atom=    4.37 meV, RMSE_F=   72.42 meV / A
131: 2026-02-25 13:50:39.082 INFO: Epoch 24: head: Default, loss=0.11574153, RMSE_E_per_atom=    4.76 meV, RMSE_F=   97.61 meV / A
132: 2026-02-25 13:50:41.358 INFO: Epoch 25: head: Default, loss=0.05081711, RMSE_E_per_atom=    1.80 meV, RMSE_F=   64.70 meV / A
133: 2026-02-25 13:50:41.360 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-19.pt
134: 2026-02-25 13:50:41.364 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-25.pt
135: 2026-02-25 13:50:43.705 INFO: Epoch 26: head: Default, loss=0.06119425, RMSE_E_per_atom=    4.23 meV, RMSE_F=   70.28 meV / A
136: 2026-02-25 13:50:45.969 INFO: Epoch 27: head: Default, loss=0.04843847, RMSE_E_per_atom=    5.48 meV, RMSE_F=   62.97 meV / A
137: 2026-02-25 13:50:45.970 DEBUG: Deleting old checkpoint file: ./checkpoints/ft_300K_run-42_epoch-25.pt
138: 2026-02-25 13:50:45.975 DEBUG: Saving checkpoint: ./checkpoints/ft_300K_run-42_epoch-27.pt
139: 2026-02-25 13:50:48.287 INFO: Epoch 28: head: Default, loss=0.03921054, RMSE_E_per_atom=    3.44 meV, RMSE_F=   56.63 meV / A
