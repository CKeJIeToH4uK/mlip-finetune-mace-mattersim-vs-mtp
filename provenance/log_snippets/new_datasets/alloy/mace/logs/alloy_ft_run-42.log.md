# Log Snippet: repo/coursework/new_datasets/alloy/mace/logs/alloy_ft_run-42.log

Original size: 42908 bytes. Full raw log not copied.

3: 2026-04-02 00:17:32.278 INFO: CUDA version: 12.4, CUDA device: 0
4: 2026-04-02 00:17:32.957 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
5: 2026-04-02 00:17:32.961 INFO: ===========LOADING INPUT DATA===========
7: 2026-04-02 00:17:32.962 INFO: Using the key specifications to parse data:
8: 2026-04-02 00:17:32.962 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
9: 2026-04-02 00:17:32.962 INFO: =============    Processing head Default     ===========
10: 2026-04-02 00:17:33.689 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
11: 2026-04-02 00:17:33.865 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
12: 2026-04-02 00:17:34.089 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
13: 2026-04-02 00:17:34.096 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
14: 2026-04-02 00:17:34.208 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
15: 2026-04-02 00:17:34.239 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
16: 2026-04-02 00:17:34.279 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
17: 2026-04-02 00:17:34.281 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
18: 2026-04-02 00:17:34.281 INFO: Total number of configurations: train=1210, valid=213, tests=[],
19: 2026-04-02 00:17:34.282 INFO: Using atomic numbers from command line argument
25: 2026-04-02 00:17:39.765 INFO: Combining 1 list datasets for head 'Default'
26: 2026-04-02 00:17:40.457 INFO: Combining 1 list datasets for head 'Default_valid'
27: 2026-04-02 00:17:40.457 INFO: Combined validation datasets for Default
28: 2026-04-02 00:17:40.457 INFO: Head 'Default' training dataset size: 1210
30: 2026-04-02 00:17:41.435 INFO: Average number of neighbors: 56.52305706170927
31: 2026-04-02 00:17:41.435 INFO: During training the following quantities will be reported: energy, forces
32: 2026-04-02 00:17:41.435 INFO: ===========MODEL DETAILS===========
35: 2026-04-02 00:17:42.154 INFO: Model configuration extracted from foundation model
36: 2026-04-02 00:17:42.154 INFO: Using weighted loss function for fine-tuning
37: 2026-04-02 00:17:42.154 INFO: Message passing with hidden irreps 128x0e)
45: 2026-04-02 00:17:53.868 INFO: Learning rate: 0.01, weight decay: 5e-07
46: 2026-04-02 00:17:53.869 INFO: WeightedEnergyForcesLoss(energy_weight=1.000, forces_weight=100.000)
47: 2026-04-02 00:17:53.870 INFO: === Layer's learning rates ===
55: 2026-04-02 00:17:53.871 INFO: ===========TRAINING===========
56: 2026-04-02 00:17:53.871 INFO: Started training, reporting errors on validation set
57: 2026-04-02 00:17:53.872 INFO: Loss metrics on validation set
58: 2026-04-02 00:18:00.916 INFO: Initial: head: Default, loss=1.68970534, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
59: 2026-04-02 00:18:36.335 INFO: Epoch 0: head: Default, loss=0.45322180, RMSE_E_per_atom=  261.34 meV, RMSE_F=  198.58 meV / A
60: 2026-04-02 00:19:06.649 INFO: Epoch 1: head: Default, loss=0.33404976, RMSE_E_per_atom=  250.01 meV, RMSE_F=  173.56 meV / A
61: 2026-04-02 00:19:40.368 INFO: Epoch 2: head: Default, loss=0.29574253, RMSE_E_per_atom=  223.76 meV, RMSE_F=  170.27 meV / A
62: 2026-04-02 00:20:14.838 INFO: Epoch 3: head: Default, loss=0.32008296, RMSE_E_per_atom=  217.53 meV, RMSE_F=  159.48 meV / A
63: 2026-04-02 00:20:44.634 INFO: Epoch 4: head: Default, loss=0.27322507, RMSE_E_per_atom=  163.74 meV, RMSE_F=  153.25 meV / A
64: 2026-04-02 00:21:14.753 INFO: Epoch 5: head: Default, loss=0.23516969, RMSE_E_per_atom=  112.35 meV, RMSE_F=  150.26 meV / A
65: 2026-04-02 00:21:46.093 INFO: Epoch 6: head: Default, loss=0.27835247, RMSE_E_per_atom=  122.88 meV, RMSE_F=  168.29 meV / A
66: 2026-04-02 00:22:20.678 INFO: Epoch 7: head: Default, loss=0.29990528, RMSE_E_per_atom=  239.59 meV, RMSE_F=  154.96 meV / A
67: 2026-04-02 00:22:50.357 INFO: Epoch 8: head: Default, loss=0.19944971, RMSE_E_per_atom=  169.61 meV, RMSE_F=  136.55 meV / A
68: 2026-04-02 00:23:20.467 INFO: Epoch 9: head: Default, loss=0.24336029, RMSE_E_per_atom=  270.54 meV, RMSE_F=  146.10 meV / A
69: 2026-04-02 00:23:53.075 INFO: Epoch 10: head: Default, loss=0.23268202, RMSE_E_per_atom=  146.05 meV, RMSE_F=  148.51 meV / A
70: 2026-04-02 00:24:23.572 INFO: Epoch 11: head: Default, loss=0.21755363, RMSE_E_per_atom=  208.46 meV, RMSE_F=  148.12 meV / A
71: 2026-04-02 00:25:01.354 INFO: Epoch 12: head: Default, loss=0.24548369, RMSE_E_per_atom=  131.23 meV, RMSE_F=  148.83 meV / A
72: 2026-04-02 00:25:32.166 INFO: Epoch 13: head: Default, loss=0.19131407, RMSE_E_per_atom=   68.63 meV, RMSE_F=  130.37 meV / A
73: 2026-04-02 00:26:06.528 INFO: Epoch 14: head: Default, loss=0.21515118, RMSE_E_per_atom=  187.64 meV, RMSE_F=  148.60 meV / A
74: 2026-04-02 00:26:41.762 INFO: Epoch 15: head: Default, loss=0.21855052, RMSE_E_per_atom=   91.96 meV, RMSE_F=  135.77 meV / A
75: 2026-04-02 00:27:12.046 INFO: Epoch 16: head: Default, loss=0.23089392, RMSE_E_per_atom=  113.67 meV, RMSE_F=  141.20 meV / A
76: 2026-04-02 00:27:44.161 INFO: Epoch 17: head: Default, loss=0.30370984, RMSE_E_per_atom=  222.54 meV, RMSE_F=  166.28 meV / A
77: 2026-04-02 00:28:18.350 INFO: Epoch 18: head: Default, loss=0.18865864, RMSE_E_per_atom=  148.62 meV, RMSE_F=  134.44 meV / A
78: 2026-04-02 00:28:50.750 INFO: Epoch 19: head: Default, loss=0.19972458, RMSE_E_per_atom=  124.35 meV, RMSE_F=  135.15 meV / A
79: 2026-04-02 00:29:20.258 INFO: Epoch 20: head: Default, loss=0.17863202, RMSE_E_per_atom=  118.95 meV, RMSE_F=  128.95 meV / A
80: 2026-04-02 00:29:52.673 INFO: Epoch 21: head: Default, loss=0.22148440, RMSE_E_per_atom=  121.62 meV, RMSE_F=  145.53 meV / A
81: 2026-04-02 00:30:24.456 INFO: Epoch 22: head: Default, loss=0.18441888, RMSE_E_per_atom=   85.04 meV, RMSE_F=  131.25 meV / A
82: 2026-04-02 00:30:57.392 INFO: Epoch 23: head: Default, loss=0.20348597, RMSE_E_per_atom=  146.90 meV, RMSE_F=  144.25 meV / A
83: 2026-04-02 00:31:26.830 INFO: Epoch 24: head: Default, loss=0.18502910, RMSE_E_per_atom=  167.87 meV, RMSE_F=  134.48 meV / A
84: 2026-04-02 00:31:56.620 INFO: Epoch 25: head: Default, loss=0.18866166, RMSE_E_per_atom=   85.69 meV, RMSE_F=  131.15 meV / A
85: 2026-04-02 00:32:27.185 INFO: Epoch 26: head: Default, loss=0.18488951, RMSE_E_per_atom=   67.04 meV, RMSE_F=  132.65 meV / A
86: 2026-04-02 00:32:59.325 INFO: Epoch 27: head: Default, loss=0.16543825, RMSE_E_per_atom=  153.29 meV, RMSE_F=  132.71 meV / A
87: 2026-04-02 00:33:35.378 INFO: Epoch 28: head: Default, loss=0.15429333, RMSE_E_per_atom=  119.99 meV, RMSE_F=  126.04 meV / A
88: 2026-04-02 00:34:10.046 INFO: Epoch 29: head: Default, loss=0.16103959, RMSE_E_per_atom=  100.93 meV, RMSE_F=  130.65 meV / A
89: 2026-04-02 00:34:42.150 INFO: Epoch 30: head: Default, loss=0.15702184, RMSE_E_per_atom=  121.26 meV, RMSE_F=  122.08 meV / A
90: 2026-04-02 00:35:15.282 INFO: Epoch 31: head: Default, loss=0.19523196, RMSE_E_per_atom=   63.19 meV, RMSE_F=  130.63 meV / A
91: 2026-04-02 00:35:45.412 INFO: Epoch 32: head: Default, loss=0.18936562, RMSE_E_per_atom=  103.57 meV, RMSE_F=  124.39 meV / A
92: 2026-04-02 00:36:17.908 INFO: Epoch 33: head: Default, loss=0.20138281, RMSE_E_per_atom=   71.93 meV, RMSE_F=  135.64 meV / A
93: 2026-04-02 00:36:52.743 INFO: Epoch 34: head: Default, loss=0.16738704, RMSE_E_per_atom=  117.17 meV, RMSE_F=  125.00 meV / A
94: 2026-04-02 00:37:27.890 INFO: Epoch 35: head: Default, loss=0.18228372, RMSE_E_per_atom=  124.03 meV, RMSE_F=  124.99 meV / A
95: 2026-04-02 00:38:02.678 INFO: Epoch 36: head: Default, loss=0.15053511, RMSE_E_per_atom=   64.45 meV, RMSE_F=  123.25 meV / A
96: 2026-04-02 00:38:33.926 INFO: Epoch 37: head: Default, loss=0.18913691, RMSE_E_per_atom=  156.16 meV, RMSE_F=  135.44 meV / A
97: 2026-04-02 00:39:07.320 INFO: Epoch 38: head: Default, loss=0.19899925, RMSE_E_per_atom=  113.48 meV, RMSE_F=  129.81 meV / A
98: 2026-04-02 00:39:39.724 INFO: Epoch 39: head: Default, loss=0.18862359, RMSE_E_per_atom=  102.75 meV, RMSE_F=  131.31 meV / A
99: 2026-04-02 00:40:09.069 INFO: Epoch 40: head: Default, loss=0.17346756, RMSE_E_per_atom=  108.21 meV, RMSE_F=  132.08 meV / A
100: 2026-04-02 00:40:39.437 INFO: Epoch 41: head: Default, loss=0.17265066, RMSE_E_per_atom=  136.93 meV, RMSE_F=  130.27 meV / A
101: 2026-04-02 00:41:11.019 INFO: Epoch 42: head: Default, loss=0.16951807, RMSE_E_per_atom=  117.65 meV, RMSE_F=  128.48 meV / A
102: 2026-04-02 00:41:41.607 INFO: Epoch 43: head: Default, loss=0.15055918, RMSE_E_per_atom=  146.76 meV, RMSE_F=  120.69 meV / A
103: 2026-04-02 00:42:12.797 INFO: Epoch 44: head: Default, loss=0.17438536, RMSE_E_per_atom=   74.10 meV, RMSE_F=  124.40 meV / A
104: 2026-04-02 00:42:47.011 INFO: Epoch 45: head: Default, loss=0.16769089, RMSE_E_per_atom=  105.91 meV, RMSE_F=  125.35 meV / A
105: 2026-04-02 00:43:21.770 INFO: Epoch 46: head: Default, loss=0.18211223, RMSE_E_per_atom=  106.53 meV, RMSE_F=  126.37 meV / A
106: 2026-04-02 00:43:51.740 INFO: Epoch 47: head: Default, loss=0.15728386, RMSE_E_per_atom=  161.74 meV, RMSE_F=  121.41 meV / A
107: 2026-04-02 00:44:23.936 INFO: Epoch 48: head: Default, loss=0.16604896, RMSE_E_per_atom=   69.76 meV, RMSE_F=  123.44 meV / A
108: 2026-04-02 00:44:58.467 INFO: Epoch 49: head: Default, loss=0.15334130, RMSE_E_per_atom=  114.51 meV, RMSE_F=  122.68 meV / A
109: 2026-04-02 00:45:31.422 INFO: Epoch 50: head: Default, loss=0.16981882, RMSE_E_per_atom=   56.63 meV, RMSE_F=  124.09 meV / A
110: 2026-04-02 00:46:00.978 INFO: Epoch 51: head: Default, loss=0.16567382, RMSE_E_per_atom=  104.68 meV, RMSE_F=  123.92 meV / A
111: 2026-04-02 00:46:32.556 INFO: Epoch 52: head: Default, loss=0.18219318, RMSE_E_per_atom=  122.23 meV, RMSE_F=  132.30 meV / A
112: 2026-04-02 00:47:02.553 INFO: Epoch 53: head: Default, loss=0.15408888, RMSE_E_per_atom=  116.52 meV, RMSE_F=  123.58 meV / A
113: 2026-04-02 00:47:39.644 INFO: Epoch 54: head: Default, loss=0.16272420, RMSE_E_per_atom=  155.68 meV, RMSE_F=  123.89 meV / A
114: 2026-04-02 00:48:12.413 INFO: Epoch 55: head: Default, loss=0.20589814, RMSE_E_per_atom=  114.07 meV, RMSE_F=  126.67 meV / A
115: 2026-04-02 00:48:44.907 INFO: Epoch 56: head: Default, loss=0.17383056, RMSE_E_per_atom=  142.09 meV, RMSE_F=  122.47 meV / A
116: 2026-04-02 00:49:14.679 INFO: Epoch 57: head: Default, loss=0.16736223, RMSE_E_per_atom=   98.06 meV, RMSE_F=  123.43 meV / A
117: 2026-04-02 00:49:45.498 INFO: Epoch 58: head: Default, loss=0.19401327, RMSE_E_per_atom=   95.39 meV, RMSE_F=  132.85 meV / A
118: 2026-04-02 00:50:16.534 INFO: Epoch 59: head: Default, loss=0.19060371, RMSE_E_per_atom=   59.13 meV, RMSE_F=  128.18 meV / A
119: 2026-04-02 00:50:48.291 INFO: Epoch 60: head: Default, loss=0.20763094, RMSE_E_per_atom=   91.54 meV, RMSE_F=  133.30 meV / A
120: 2026-04-02 00:51:17.669 INFO: Epoch 61: head: Default, loss=0.17916374, RMSE_E_per_atom=  140.98 meV, RMSE_F=  122.47 meV / A
