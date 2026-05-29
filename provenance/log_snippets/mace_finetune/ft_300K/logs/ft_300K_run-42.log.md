# Log Snippet: repo/coursework/mace_finetune/ft_300K/logs/ft_300K_run-42.log

Original size: 72438 bytes. Full raw log not copied.

11: 2026-02-25 13:49:09.909 INFO: CUDA version: 12.4, CUDA device: 0
12: 2026-02-25 13:49:11.640 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
13: 2026-02-25 13:49:11.655 INFO: ===========LOADING INPUT DATA===========
15: 2026-02-25 13:49:11.655 INFO: Using the key specifications to parse data:
16: 2026-02-25 13:49:11.655 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
17: 2026-02-25 13:49:11.655 INFO: =============    Processing head Default     ===========
18: 2026-02-25 13:49:11.983 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
19: 2026-02-25 13:49:12.051 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
20: 2026-02-25 13:49:12.133 INFO: Training set 1/1 [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
21: 2026-02-25 13:49:12.135 INFO: Total Training set [energy: 500, stress: 0, virials: 0, dipole components: 0, head: 500, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 500, charges: 0]
22: 2026-02-25 13:49:12.135 INFO: No validation set provided, splitting training data instead.
23: 2026-02-25 13:49:12.139 INFO: Using random 5% of training set for validation with indices saved in: ./ft_300K_valid_indices_42.txt
24: 2026-02-25 13:49:12.147 INFO: Random Split Training set [energy: 475, stress: 0, virials: 0, dipole components: 0, head: 475, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 475, charges: 0]
25: 2026-02-25 13:49:12.148 INFO: Random Split Validation set [energy: 25, stress: 0, virials: 0, dipole components: 0, head: 25, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 25, charges: 0]
26: 2026-02-25 13:49:12.892 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
27: 2026-02-25 13:49:13.083 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
28: 2026-02-25 13:49:13.313 INFO: Test set 1/1 [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
29: 2026-02-25 13:49:13.320 INFO: Total Test set [energy: 1669, stress: 0, virials: 0, dipole components: 0, head: 1669, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1669, charges: 0]
30: 2026-02-25 13:49:13.320 INFO: Total number of configurations: train=475, valid=25, tests=[Default_Default: 1669],
31: 2026-02-25 13:49:13.321 INFO: Using atomic numbers from command line argument
40: 2026-02-25 13:49:15.511 INFO: Average number of neighbors: 20.47470238095238
41: 2026-02-25 13:49:15.512 INFO: During training the following quantities will be reported: energy, forces
42: 2026-02-25 13:49:15.512 INFO: ===========MODEL DETAILS===========
45: 2026-02-25 13:49:16.168 INFO: Model configuration extracted from foundation model
46: 2026-02-25 13:49:16.168 INFO: Using weighted loss function for fine-tuning
47: 2026-02-25 13:49:16.168 INFO: Message passing with hidden irreps 128x0e)
55: 2026-02-25 13:49:22.789 INFO: Learning rate: 0.01, weight decay: 5e-07
56: 2026-02-25 13:49:22.790 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
57: 2026-02-25 13:49:22.792 INFO: === Layer's learning rates ===
65: 2026-02-25 13:49:22.794 INFO: ===========TRAINING===========
66: 2026-02-25 13:49:22.794 INFO: Started training, reporting errors on validation set
67: 2026-02-25 13:49:22.794 INFO: Loss metrics on validation set
68: 2026-02-25 13:49:37.362 INFO: Initial: head: Default, loss=1.92412590, RMSE_E_per_atom=  276.31 meV, RMSE_F=  404.35 meV / A
69: 2026-02-25 13:49:45.983 INFO: Epoch 0: head: Default, loss=1.99465336, RMSE_E_per_atom=   54.74 meV, RMSE_F=  405.85 meV / A
70: 2026-02-25 13:49:48.496 INFO: Epoch 1: head: Default, loss=0.53195376, RMSE_E_per_atom=   30.81 meV, RMSE_F=  210.86 meV / A
71: 2026-02-25 13:49:50.606 INFO: Epoch 2: head: Default, loss=0.66904881, RMSE_E_per_atom=   21.52 meV, RMSE_F=  234.99 meV / A
72: 2026-02-25 13:49:52.632 INFO: Epoch 3: head: Default, loss=0.37812980, RMSE_E_per_atom=   23.47 meV, RMSE_F=  176.35 meV / A
73: 2026-02-25 13:49:54.699 INFO: Epoch 4: head: Default, loss=0.32471338, RMSE_E_per_atom=   12.30 meV, RMSE_F=  164.74 meV / A
74: 2026-02-25 13:49:56.747 INFO: Epoch 5: head: Default, loss=0.21654166, RMSE_E_per_atom=   16.85 meV, RMSE_F=  133.25 meV / A
75: 2026-02-25 13:49:58.794 INFO: Epoch 6: head: Default, loss=0.18049867, RMSE_E_per_atom=    4.57 meV, RMSE_F=  122.01 meV / A
76: 2026-02-25 13:50:00.928 INFO: Epoch 7: head: Default, loss=0.25657002, RMSE_E_per_atom=    6.87 meV, RMSE_F=  145.31 meV / A
77: 2026-02-25 13:50:02.905 INFO: Epoch 8: head: Default, loss=0.25355030, RMSE_E_per_atom=    2.04 meV, RMSE_F=  144.39 meV / A
78: 2026-02-25 13:50:04.878 INFO: Epoch 9: head: Default, loss=0.12801723, RMSE_E_per_atom=    5.80 meV, RMSE_F=  102.38 meV / A
79: 2026-02-25 13:50:06.956 INFO: Epoch 10: head: Default, loss=0.21522380, RMSE_E_per_atom=    7.57 meV, RMSE_F=  132.60 meV / A
80: 2026-02-25 13:50:08.962 INFO: Epoch 11: head: Default, loss=0.12527059, RMSE_E_per_atom=    4.94 meV, RMSE_F=  101.90 meV / A
81: 2026-02-25 13:50:11.179 INFO: Epoch 12: head: Default, loss=0.11556768, RMSE_E_per_atom=    4.39 meV, RMSE_F=   96.86 meV / A
82: 2026-02-25 13:50:13.568 INFO: Epoch 13: head: Default, loss=0.16970550, RMSE_E_per_atom=    6.37 meV, RMSE_F=  118.03 meV / A
83: 2026-02-25 13:50:15.907 INFO: Epoch 14: head: Default, loss=0.16434239, RMSE_E_per_atom=   16.96 meV, RMSE_F=  116.05 meV / A
84: 2026-02-25 13:50:18.275 INFO: Epoch 15: head: Default, loss=0.14253747, RMSE_E_per_atom=    5.61 meV, RMSE_F=  108.38 meV / A
85: 2026-02-25 13:50:20.626 INFO: Epoch 16: head: Default, loss=0.10279813, RMSE_E_per_atom=   11.48 meV, RMSE_F=   92.40 meV / A
86: 2026-02-25 13:50:23.013 INFO: Epoch 17: head: Default, loss=0.13134738, RMSE_E_per_atom=    9.74 meV, RMSE_F=  103.20 meV / A
87: 2026-02-25 13:50:25.315 INFO: Epoch 18: head: Default, loss=0.15121359, RMSE_E_per_atom=    8.33 meV, RMSE_F=  110.83 meV / A
88: 2026-02-25 13:50:27.607 INFO: Epoch 19: head: Default, loss=0.06307120, RMSE_E_per_atom=    5.07 meV, RMSE_F=   71.55 meV / A
89: 2026-02-25 13:50:29.926 INFO: Epoch 20: head: Default, loss=0.16323715, RMSE_E_per_atom=    2.25 meV, RMSE_F=  116.46 meV / A
90: 2026-02-25 13:50:32.204 INFO: Epoch 21: head: Default, loss=0.10425535, RMSE_E_per_atom=    1.72 meV, RMSE_F=   92.57 meV / A
91: 2026-02-25 13:50:34.489 INFO: Epoch 22: head: Default, loss=0.08872654, RMSE_E_per_atom=    4.74 meV, RMSE_F=   85.92 meV / A
92: 2026-02-25 13:50:36.803 INFO: Epoch 23: head: Default, loss=0.06373223, RMSE_E_per_atom=    4.37 meV, RMSE_F=   72.42 meV / A
93: 2026-02-25 13:50:39.082 INFO: Epoch 24: head: Default, loss=0.11574153, RMSE_E_per_atom=    4.76 meV, RMSE_F=   97.61 meV / A
94: 2026-02-25 13:50:41.358 INFO: Epoch 25: head: Default, loss=0.05081711, RMSE_E_per_atom=    1.80 meV, RMSE_F=   64.70 meV / A
95: 2026-02-25 13:50:43.705 INFO: Epoch 26: head: Default, loss=0.06119425, RMSE_E_per_atom=    4.23 meV, RMSE_F=   70.28 meV / A
96: 2026-02-25 13:50:45.969 INFO: Epoch 27: head: Default, loss=0.04843847, RMSE_E_per_atom=    5.48 meV, RMSE_F=   62.97 meV / A
97: 2026-02-25 13:50:48.287 INFO: Epoch 28: head: Default, loss=0.03921054, RMSE_E_per_atom=    3.44 meV, RMSE_F=   56.63 meV / A
98: 2026-02-25 13:50:50.648 INFO: Epoch 29: head: Default, loss=0.11538306, RMSE_E_per_atom=    6.16 meV, RMSE_F=   97.37 meV / A
99: 2026-02-25 13:50:52.801 INFO: Epoch 30: head: Default, loss=0.09936167, RMSE_E_per_atom=    8.91 meV, RMSE_F=   90.04 meV / A
100: 2026-02-25 13:50:54.767 INFO: Epoch 31: head: Default, loss=0.06143804, RMSE_E_per_atom=    2.45 meV, RMSE_F=   70.93 meV / A
101: 2026-02-25 13:50:56.742 INFO: Epoch 32: head: Default, loss=0.04214634, RMSE_E_per_atom=    5.60 meV, RMSE_F=   58.38 meV / A
102: 2026-02-25 13:50:58.703 INFO: Epoch 33: head: Default, loss=0.08747214, RMSE_E_per_atom=    5.06 meV, RMSE_F=   85.43 meV / A
103: 2026-02-25 13:51:00.750 INFO: Epoch 34: head: Default, loss=0.05936598, RMSE_E_per_atom=    4.45 meV, RMSE_F=   69.61 meV / A
104: 2026-02-25 13:51:03.032 INFO: Epoch 35: head: Default, loss=0.03941081, RMSE_E_per_atom=    1.34 meV, RMSE_F=   56.95 meV / A
105: 2026-02-25 13:51:05.317 INFO: Epoch 36: head: Default, loss=0.05428918, RMSE_E_per_atom=    7.01 meV, RMSE_F=   67.18 meV / A
106: 2026-02-25 13:51:07.623 INFO: Epoch 37: head: Default, loss=0.07362760, RMSE_E_per_atom=   10.24 meV, RMSE_F=   77.88 meV / A
107: 2026-02-25 13:51:09.986 INFO: Epoch 38: head: Default, loss=0.03568298, RMSE_E_per_atom=    4.01 meV, RMSE_F=   54.15 meV / A
108: 2026-02-25 13:51:12.414 INFO: Epoch 39: head: Default, loss=0.03384632, RMSE_E_per_atom=    1.55 meV, RMSE_F=   52.48 meV / A
109: 2026-02-25 13:51:14.826 INFO: Epoch 40: head: Default, loss=0.03692353, RMSE_E_per_atom=    3.12 meV, RMSE_F=   54.71 meV / A
110: 2026-02-25 13:51:17.178 INFO: Epoch 41: head: Default, loss=0.04224791, RMSE_E_per_atom=    4.32 meV, RMSE_F=   58.80 meV / A
111: 2026-02-25 13:51:19.528 INFO: Epoch 42: head: Default, loss=0.03669422, RMSE_E_per_atom=    3.84 meV, RMSE_F=   55.00 meV / A
112: 2026-02-25 13:51:21.894 INFO: Epoch 43: head: Default, loss=0.03733763, RMSE_E_per_atom=   10.59 meV, RMSE_F=   55.25 meV / A
113: 2026-02-25 13:51:24.182 INFO: Epoch 44: head: Default, loss=0.04962073, RMSE_E_per_atom=   10.02 meV, RMSE_F=   63.52 meV / A
114: 2026-02-25 13:51:26.459 INFO: Epoch 45: head: Default, loss=0.03445513, RMSE_E_per_atom=    7.08 meV, RMSE_F=   53.28 meV / A
115: 2026-02-25 13:51:28.804 INFO: Epoch 46: head: Default, loss=0.07063273, RMSE_E_per_atom=    8.87 meV, RMSE_F=   76.55 meV / A
116: 2026-02-25 13:51:31.167 INFO: Epoch 47: head: Default, loss=0.05021584, RMSE_E_per_atom=    2.74 meV, RMSE_F=   63.81 meV / A
117: 2026-02-25 13:51:33.428 INFO: Epoch 48: head: Default, loss=0.02816093, RMSE_E_per_atom=    2.22 meV, RMSE_F=   47.70 meV / A
118: 2026-02-25 13:51:35.758 INFO: Epoch 49: head: Default, loss=0.02639546, RMSE_E_per_atom=    2.75 meV, RMSE_F=   46.62 meV / A
119: 2026-02-25 13:51:38.069 INFO: Epoch 50: head: Default, loss=0.04030910, RMSE_E_per_atom=    8.17 meV, RMSE_F=   57.37 meV / A
120: 2026-02-25 13:51:40.365 INFO: Epoch 51: head: Default, loss=0.03119649, RMSE_E_per_atom=    1.99 meV, RMSE_F=   50.12 meV / A
121: 2026-02-25 13:51:42.450 INFO: Epoch 52: head: Default, loss=0.03354626, RMSE_E_per_atom=    1.21 meV, RMSE_F=   52.17 meV / A
122: 2026-02-25 13:51:44.437 INFO: Epoch 53: head: Default, loss=0.02742399, RMSE_E_per_atom=    1.32 meV, RMSE_F=   47.00 meV / A
123: 2026-02-25 13:51:46.447 INFO: Epoch 54: head: Default, loss=0.02548070, RMSE_E_per_atom=    1.47 meV, RMSE_F=   45.73 meV / A
124: 2026-02-25 13:51:48.444 INFO: Epoch 55: head: Default, loss=0.02810364, RMSE_E_per_atom=    1.23 meV, RMSE_F=   48.08 meV / A
125: 2026-02-25 13:51:50.451 INFO: Epoch 56: head: Default, loss=0.03255393, RMSE_E_per_atom=    7.03 meV, RMSE_F=   51.41 meV / A
126: 2026-02-25 13:51:52.781 INFO: Epoch 57: head: Default, loss=0.02958632, RMSE_E_per_atom=    5.58 meV, RMSE_F=   49.32 meV / A
127: 2026-02-25 13:51:55.053 INFO: Epoch 58: head: Default, loss=0.11687767, RMSE_E_per_atom=    1.37 meV, RMSE_F=   98.29 meV / A
128: 2026-02-25 13:51:57.334 INFO: Epoch 59: head: Default, loss=0.08662992, RMSE_E_per_atom=    1.50 meV, RMSE_F=   84.98 meV / A
