# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr1e-4_bs32/train.log

Original size: 320369 bytes. Full raw log not copied.

1: [rank0]:[W225 15:57:58.192362886 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 15:57:59.307[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 15:58:01.454[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 15:58:05.500[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 15:58:05.749[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 15:58:05.749[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 15:58:12.383[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0095, MAE(f): 0.6848, MAE(s): 0.0000, Time: 6.63s, lr: 0.00010000
39: [0m
40: [32m2026-02-25 15:58:15.399[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0058, MAE(f): 0.6910, MAE(s): 0.0000, Time: 3.01s, lr: 0.00010000
41: [0m
42: [32m2026-02-25 15:58:15.403[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 15:58:17.622[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0054, MAE(f): 0.6746, MAE(s): 0.0000, Time: 2.22s, lr: 0.00010000
44: [0m
45: [32m2026-02-25 15:58:20.003[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6794, MAE(s): 0.0000, Time: 2.38s, lr: 0.00010000
46: [0m
47: [32m2026-02-25 15:58:20.008[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 15:58:22.376[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0048, MAE(f): 0.6513, MAE(s): 0.0000, Time: 2.37s, lr: 0.00010000
49: [0m
50: [32m2026-02-25 15:58:24.757[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0065, MAE(e): 0.0045, MAE(f): 0.6523, MAE(s): 0.0000, Time: 2.38s, lr: 0.00010000
51: [0m
52: [32m2026-02-25 15:58:24.761[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 15:58:26.961[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0055, MAE(e): 0.0042, MAE(f): 0.5583, MAE(s): 0.0000, Time: 2.20s, lr: 0.00010000
54: [0m
55: [32m2026-02-25 15:58:29.365[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0054, MAE(e): 0.0038, MAE(f): 0.5448, MAE(s): 0.0000, Time: 2.40s, lr: 0.00010000
56: [0m
57: [32m2026-02-25 15:58:29.369[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 15:58:31.600[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0035, MAE(e): 0.0067, MAE(f): 0.3526, MAE(s): 0.0000, Time: 2.23s, lr: 0.00010000
59: [0m
60: [32m2026-02-25 15:58:33.940[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0034, MAE(e): 0.0062, MAE(f): 0.3440, MAE(s): 0.0000, Time: 2.34s, lr: 0.00010000
61: [0m
62: [32m2026-02-25 15:58:33.944[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 15:58:36.084[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0026, MAE(e): 0.0059, MAE(f): 0.2596, MAE(s): 0.0000, Time: 2.14s, lr: 0.00010000
64: [0m
65: [32m2026-02-25 15:58:38.540[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0026, MAE(e): 0.0046, MAE(f): 0.2604, MAE(s): 0.0000, Time: 2.45s, lr: 0.00010000
66: [0m
67: [32m2026-02-25 15:58:38.545[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 15:58:40.783[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0052, MAE(f): 0.2082, MAE(s): 0.0000, Time: 2.24s, lr: 0.00010000
69: [0m
70: [32m2026-02-25 15:58:43.129[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0021, MAE(e): 0.0037, MAE(f): 0.2150, MAE(s): 0.0000, Time: 2.34s, lr: 0.00010000
71: [0m
72: [32m2026-02-25 15:58:43.133[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 15:58:45.137[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0017, MAE(e): 0.0039, MAE(f): 0.1734, MAE(s): 0.0000, Time: 2.00s, lr: 0.00010000
74: [0m
75: [32m2026-02-25 15:58:47.424[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0018, MAE(e): 0.0034, MAE(f): 0.1820, MAE(s): 0.0000, Time: 2.28s, lr: 0.00010000
76: [0m
77: [32m2026-02-25 15:58:47.428[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 15:58:49.644[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0043, MAE(f): 0.1485, MAE(s): 0.0000, Time: 2.22s, lr: 0.00010000
79: [0m
80: [32m2026-02-25 15:58:52.118[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0031, MAE(f): 0.1570, MAE(s): 0.0000, Time: 2.47s, lr: 0.00010000
81: [0m
82: [32m2026-02-25 15:58:52.122[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 15:58:54.312[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0044, MAE(f): 0.1294, MAE(s): 0.0000, Time: 2.19s, lr: 0.00010000
84: [0m
85: [32m2026-02-25 15:58:56.671[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0026, MAE(f): 0.1381, MAE(s): 0.0000, Time: 2.36s, lr: 0.00010000
86: [0m
87: [32m2026-02-25 15:58:56.675[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 15:58:58.712[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0042, MAE(f): 0.1156, MAE(s): 0.0000, Time: 2.04s, lr: 0.00010000
89: [0m
90: [32m2026-02-25 15:59:01.127[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0023, MAE(f): 0.1234, MAE(s): 0.0000, Time: 2.41s, lr: 0.00010000
91: [0m
92: [32m2026-02-25 15:59:01.131[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 15:59:03.327[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0038, MAE(f): 0.1065, MAE(s): 0.0000, Time: 2.20s, lr: 0.00010000
94: [0m
95: [32m2026-02-25 15:59:05.780[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0021, MAE(f): 0.1127, MAE(s): 0.0000, Time: 2.45s, lr: 0.00010000
96: [0m
97: [32m2026-02-25 15:59:05.784[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 15:59:07.639[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0026, MAE(f): 0.1006, MAE(s): 0.0000, Time: 1.85s, lr: 0.00010000
99: [0m
100: [32m2026-02-25 15:59:09.891[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0019, MAE(f): 0.1055, MAE(s): 0.0000, Time: 2.25s, lr: 0.00010000
101: [0m
102: [32m2026-02-25 15:59:09.894[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 15:59:12.134[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0022, MAE(f): 0.0961, MAE(s): 0.0000, Time: 2.24s, lr: 0.00010000
104: [0m
105: [32m2026-02-25 15:59:14.520[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0018, MAE(f): 0.1002, MAE(s): 0.0000, Time: 2.38s, lr: 0.00010000
106: [0m
107: [32m2026-02-25 15:59:14.524[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 15:59:16.631[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0026, MAE(f): 0.0922, MAE(s): 0.0000, Time: 2.11s, lr: 0.00010000
109: [0m
110: [32m2026-02-25 15:59:19.130[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0017, MAE(f): 0.0959, MAE(s): 0.0000, Time: 2.50s, lr: 0.00010000
111: [0m
112: [32m2026-02-25 15:59:19.134[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 15:59:21.284[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0025, MAE(f): 0.0881, MAE(s): 0.0000, Time: 2.15s, lr: 0.00010000
114: [0m
115: [32m2026-02-25 15:59:23.762[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0016, MAE(f): 0.0923, MAE(s): 0.0000, Time: 2.48s, lr: 0.00010000
116: [0m
117: [32m2026-02-25 15:59:23.766[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 15:59:25.826[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0032, MAE(f): 0.0853, MAE(s): 0.0000, Time: 2.06s, lr: 0.00010000
119: [0m
120: [32m2026-02-25 15:59:28.295[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0016, MAE(f): 0.0891, MAE(s): 0.0000, Time: 2.47s, lr: 0.00010000
121: [0m
122: [32m2026-02-25 15:59:28.298[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 15:59:30.221[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0032, MAE(f): 0.0829, MAE(s): 0.0000, Time: 1.92s, lr: 0.00010000
124: [0m
125: [32m2026-02-25 15:59:32.542[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0015, MAE(f): 0.0864, MAE(s): 0.0000, Time: 2.32s, lr: 0.00010000
126: [0m
127: [32m2026-02-25 15:59:32.546[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 15:59:34.607[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0025, MAE(f): 0.0801, MAE(s): 0.0000, Time: 2.06s, lr: 0.00010000
129: [0m
130: [32m2026-02-25 15:59:36.981[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0015, MAE(f): 0.0840, MAE(s): 0.0000, Time: 2.37s, lr: 0.00010000
131: [0m
132: [32m2026-02-25 15:59:36.985[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 15:59:39.000[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0026, MAE(f): 0.0783, MAE(s): 0.0000, Time: 2.02s, lr: 0.00010000
134: [0m
135: [32m2026-02-25 15:59:41.374[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0014, MAE(f): 0.0818, MAE(s): 0.0000, Time: 2.37s, lr: 0.00010000
136: [0m
137: [32m2026-02-25 15:59:41.378[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 15:59:43.551[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0025, MAE(f): 0.0760, MAE(s): 0.0000, Time: 2.17s, lr: 0.00010000
139: [0m
140: [32m2026-02-25 15:59:45.922[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0014, MAE(f): 0.0799, MAE(s): 0.0000, Time: 2.37s, lr: 0.00010000
141: [0m
142: [32m2026-02-25 15:59:45.926[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 15:59:47.912[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0028, MAE(f): 0.0754, MAE(s): 0.0000, Time: 1.98s, lr: 0.00010000
144: [0m
145: [32m2026-02-25 15:59:50.288[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0014, MAE(f): 0.0781, MAE(s): 0.0000, Time: 2.37s, lr: 0.00010000
146: [0m
147: [32m2026-02-25 15:59:50.292[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 15:59:52.335[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0024, MAE(f): 0.0734, MAE(s): 0.0000, Time: 2.04s, lr: 0.00010000
149: [0m
150: [32m2026-02-25 15:59:54.626[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0765, MAE(s): 0.0000, Time: 2.29s, lr: 0.00010000
151: [0m
152: [32m2026-02-25 15:59:54.630[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 15:59:56.706[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0027, MAE(f): 0.0715, MAE(s): 0.0000, Time: 2.08s, lr: 0.00010000
154: [0m
155: [32m2026-02-25 15:59:59.011[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0751, MAE(s): 0.0000, Time: 2.30s, lr: 0.00010000
156: [0m
157: [32m2026-02-25 15:59:59.015[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 16:00:01.047[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0040, MAE(f): 0.0700, MAE(s): 0.0000, Time: 2.03s, lr: 0.00010000
159: [0m
160: [32m2026-02-25 16:00:03.397[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0737, MAE(s): 0.0000, Time: 2.35s, lr: 0.00010000
161: [0m
