# Log Snippet: repo/coursework/new_datasets/alloy/mace_ablation_20260509/lora_ew10_normal/logs/alloy_mace_lora_ew10_normal_run-42.log

Original size: 9218 bytes. Full raw log not copied.

3: 2026-05-10 05:14:55.430 INFO: CUDA version: 12.4, CUDA device: 0
4: 2026-05-10 05:14:56.701 INFO: Using foundation model /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model as initial checkpoint.
5: 2026-05-10 05:14:56.703 INFO: ===========LOADING INPUT DATA===========
7: 2026-05-10 05:14:56.703 INFO: Using the key specifications to parse data:
8: 2026-05-10 05:14:56.704 INFO: Default: KeySpecification(info_keys={'energy': 'energy', 'stress': 'REF_stress', 'virials': 'REF_virials', 'dipole': 'dipole', 'head': 'head', 'elec_temp': 'elec_temp', 'total_charge': 'total_charge', 'polarizability': 'polarizability', 'total_spin': 'total_spin'}, arra
9: 2026-05-10 05:14:56.704 INFO: =============    Processing head Default     ===========
10: 2026-05-10 05:14:57.234 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
11: 2026-05-10 05:14:57.414 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
12: 2026-05-10 05:14:57.647 INFO: Training set 1/1 [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
13: 2026-05-10 05:14:57.653 INFO: Total Training set [energy: 1210, stress: 0, virials: 0, dipole components: 0, head: 1210, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 1210, charges: 0]
14: 2026-05-10 05:14:57.762 WARNING: Since ASE version 3.23.0b1, using energy_key 'energy' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'energy' to 'REF_energy'. You need to use --energy_key='REF_energy' to specify the chosen key name.
15: 2026-05-10 05:14:57.793 WARNING: Since ASE version 3.23.0b1, using forces_key 'forces' is no longer safe when communicating between MACE and ASE. We recommend using a different key, rewriting 'forces' to 'REF_forces'. You need to use --forces_key='REF_forces' to specify the chosen key name.
16: 2026-05-10 05:14:57.833 INFO: Validation set 1/1 [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
17: 2026-05-10 05:14:57.835 INFO: Total Validation set [energy: 213, stress: 0, virials: 0, dipole components: 0, head: 213, elec_temp: 0, total_charge: 0, polarizability: 0, total_spin: 0, forces: 213, charges: 0]
18: 2026-05-10 05:14:57.835 INFO: Total number of configurations: train=1210, valid=213, tests=[],
19: 2026-05-10 05:14:57.836 INFO: Using atomic numbers from command line argument
25: 2026-05-10 05:15:02.137 INFO: Combining 1 list datasets for head 'Default'
26: 2026-05-10 05:15:02.809 INFO: Combining 1 list datasets for head 'Default_valid'
27: 2026-05-10 05:15:02.809 INFO: Combined validation datasets for Default
28: 2026-05-10 05:15:02.809 INFO: Head 'Default' training dataset size: 1210
30: 2026-05-10 05:15:03.671 INFO: Average number of neighbors: 56.52305706170927
31: 2026-05-10 05:15:03.672 INFO: During training the following quantities will be reported: energy, forces
32: 2026-05-10 05:15:03.672 INFO: ===========MODEL DETAILS===========
35: 2026-05-10 05:15:04.551 INFO: Model configuration extracted from foundation model
36: 2026-05-10 05:15:04.551 INFO: Using weighted loss function for fine-tuning
37: 2026-05-10 05:15:04.551 INFO: Message passing with hidden irreps 128x0e)
48: 2026-05-10 05:15:08.276 INFO: Learning rate: 0.001, weight decay: 5e-07
49: 2026-05-10 05:15:08.276 INFO: WeightedEnergyForcesLoss(energy_weight=10.000, forces_weight=100.000)
50: 2026-05-10 05:15:08.277 INFO: === Layer's learning rates ===
58: 2026-05-10 05:15:08.279 INFO: ===========TRAINING===========
59: 2026-05-10 05:15:08.279 INFO: Started training, reporting errors on validation set
60: 2026-05-10 05:15:08.279 INFO: Loss metrics on validation set
61: 2026-05-10 05:15:15.200 INFO: Initial: head: Default, loss=3.47115944, RMSE_E_per_atom= 1393.24 meV, RMSE_F=  387.23 meV / A
62: 2026-05-10 05:15:53.157 INFO: Epoch 0: head: Default, loss=1.43121206, RMSE_E_per_atom=  688.06 meV, RMSE_F=  309.12 meV / A
63: 2026-05-10 05:28:51.008 INFO: Epoch 25: head: Default, loss=0.30607701, RMSE_E_per_atom=  100.76 meV, RMSE_F=  174.39 meV / A
64: 2026-05-10 05:41:48.975 INFO: Epoch 50: head: Default, loss=0.23219021, RMSE_E_per_atom=   45.36 meV, RMSE_F=  152.42 meV / A
65: 2026-05-10 05:54:46.954 INFO: Epoch 75: head: Default, loss=0.21460615, RMSE_E_per_atom=   43.13 meV, RMSE_F=  142.52 meV / A
66: 2026-05-10 06:07:45.295 INFO: Epoch 100: head: Default, loss=0.21255503, RMSE_E_per_atom=   38.72 meV, RMSE_F=  137.50 meV / A
67: 2026-05-10 06:20:45.977 INFO: Epoch 125: head: Default, loss=0.20763277, RMSE_E_per_atom=   35.96 meV, RMSE_F=  133.50 meV / A
68: 2026-05-10 06:33:43.609 INFO: Epoch 150: head: Default, loss=0.20280107, RMSE_E_per_atom=   34.71 meV, RMSE_F=  131.19 meV / A
69: 2026-05-10 06:46:34.322 INFO: Epoch 175: head: Default, loss=0.20116240, RMSE_E_per_atom=   33.51 meV, RMSE_F=  129.08 meV / A
70: 2026-05-10 06:58:47.009 INFO: Training complete
72: 2026-05-10 06:58:47.010 INFO: ===========RESULTS===========
73: 2026-05-10 06:58:47.020 INFO: Loading checkpoint: /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/lora_ew10_normal/checkpoints/alloy_mace_lora_ew10_normal_run-42_epoch-175.pt
74: 2026-05-10 06:58:47.132 INFO: Loaded Stage one model from epoch 175 for evaluation
75: 2026-05-10 06:58:47.133 INFO: Saving model to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/lora_ew10_normal/checkpoints/alloy_mace_lora_ew10_normal_run-42.model
77: 2026-05-10 06:58:47.550 INFO: Compiling model, saving metadata to /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509/lora_ew10_normal/models/alloy_mace_lora_ew10_normal_compiled.model
78: 2026-05-10 06:58:48.980 INFO: Computing metrics for training, validation, and test sets
79: 2026-05-10 06:58:48.981 INFO: Skipping evaluation for heads: ['pt_head']
80: 2026-05-10 06:58:48.981 INFO: Evaluating train_Default ...
81: 2026-05-10 06:59:00.929 INFO: Evaluating valid_Default ...
82: 2026-05-10 06:59:02.845 INFO: Error-table on TRAIN and VALID:
83: +---------------+---------------------+------------------+-------------------+
84: |  config_type  | RMSE E / meV / atom | RMSE F / meV / A | relative F RMSE % |
85: +---------------+---------------------+------------------+-------------------+
86: | train_Default |           41.8      |        115.2     |         12.79     |
87: | valid_Default |           33.5      |        129.1     |         14.55     |
88: +---------------+---------------------+------------------+-------------------+
