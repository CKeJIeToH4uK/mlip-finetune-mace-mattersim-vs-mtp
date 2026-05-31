# Log Snippet: repo/coursework/FLiNaK/run_all/3909461/train.log

Original size: 320197 bytes. Full raw log not copied.

1: [rank0]:[W422 18:42:01.208761103 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-04-22 18:42:02.918[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
25:          0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000])
26: [32m2026-04-22 18:42:11.289[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
27: [32m2026-04-22 18:42:15.548[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
28: [32m2026-04-22 18:42:15.852[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
29: [32m2026-04-22 18:42:15.853[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
30: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
31: grad.sizes() = [1, 128], strides() = [1, 1]
33:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
34: [32m2026-04-22 18:42:36.235[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0048, MAE(e): 0.0491, MAE(f): 0.4438, MAE(s): 0.0000, Time: 20.38s, lr: 0.00005000
35: [0m
36: [32m2026-04-22 18:42:38.903[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0049, MAE(e): 0.0502, MAE(f): 0.4446, MAE(s): 0.0000, Time: 2.67s, lr: 0.00005000
37: [0m
38: [32m2026-04-22 18:42:39.216[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
39: [32m2026-04-22 18:42:45.071[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0048, MAE(e): 0.0490, MAE(f): 0.4419, MAE(s): 0.0000, Time: 5.85s, lr: 0.00005000
40: [0m
41: [32m2026-04-22 18:42:47.427[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0048, MAE(e): 0.0499, MAE(f): 0.4425, MAE(s): 0.0000, Time: 2.35s, lr: 0.00005000
42: [0m
43: [32m2026-04-22 18:42:47.625[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
44: [32m2026-04-22 18:42:53.778[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0048, MAE(e): 0.0482, MAE(f): 0.4368, MAE(s): 0.0000, Time: 6.15s, lr: 0.00005000
45: [0m
46: [32m2026-04-22 18:42:56.027[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0048, MAE(e): 0.0489, MAE(f): 0.4365, MAE(s): 0.0000, Time: 2.25s, lr: 0.00005000
47: [0m
48: [32m2026-04-22 18:42:56.211[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
49: [32m2026-04-22 18:43:02.130[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0045, MAE(e): 0.0445, MAE(f): 0.4107, MAE(s): 0.0000, Time: 5.92s, lr: 0.00005000
50: [0m
51: [32m2026-04-22 18:43:04.345[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0044, MAE(e): 0.0443, MAE(f): 0.4081, MAE(s): 0.0000, Time: 2.21s, lr: 0.00005000
52: [0m
53: [32m2026-04-22 18:43:04.530[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
54: [32m2026-04-22 18:43:10.438[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0037, MAE(e): 0.0357, MAE(f): 0.3434, MAE(s): 0.0000, Time: 5.91s, lr: 0.00005000
55: [0m
56: [32m2026-04-22 18:43:12.842[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0037, MAE(e): 0.0360, MAE(f): 0.3433, MAE(s): 0.0000, Time: 2.40s, lr: 0.00005000
57: [0m
58: [32m2026-04-22 18:43:13.026[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
59: [32m2026-04-22 18:43:19.326[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0028, MAE(e): 0.0263, MAE(f): 0.2623, MAE(s): 0.0000, Time: 6.30s, lr: 0.00005000
60: [0m
61: [32m2026-04-22 18:43:22.090[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0029, MAE(e): 0.0263, MAE(f): 0.2686, MAE(s): 0.0000, Time: 2.76s, lr: 0.00005000
62: [0m
63: [32m2026-04-22 18:43:22.301[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
64: [32m2026-04-22 18:43:28.310[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0022, MAE(e): 0.0166, MAE(f): 0.2162, MAE(s): 0.0000, Time: 6.01s, lr: 0.00005000
65: [0m
66: [32m2026-04-22 18:43:30.674[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0023, MAE(e): 0.0176, MAE(f): 0.2248, MAE(s): 0.0000, Time: 2.36s, lr: 0.00005000
67: [0m
68: [32m2026-04-22 18:43:30.856[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
69: [32m2026-04-22 18:43:36.726[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0114, MAE(f): 0.1840, MAE(s): 0.0000, Time: 5.87s, lr: 0.00005000
70: [0m
71: [32m2026-04-22 18:43:39.089[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0020, MAE(e): 0.0120, MAE(f): 0.1933, MAE(s): 0.0000, Time: 2.36s, lr: 0.00005000
72: [0m
73: [32m2026-04-22 18:43:39.294[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
74: [32m2026-04-22 18:43:45.138[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0016, MAE(e): 0.0097, MAE(f): 0.1625, MAE(s): 0.0000, Time: 5.84s, lr: 0.00005000
75: [0m
76: [32m2026-04-22 18:43:47.432[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0017, MAE(e): 0.0093, MAE(f): 0.1714, MAE(s): 0.0000, Time: 2.29s, lr: 0.00005000
77: [0m
78: [32m2026-04-22 18:43:47.636[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
79: [32m2026-04-22 18:43:53.345[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0088, MAE(f): 0.1466, MAE(s): 0.0000, Time: 5.71s, lr: 0.00005000
80: [0m
81: [32m2026-04-22 18:43:55.492[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0083, MAE(f): 0.1553, MAE(s): 0.0000, Time: 2.14s, lr: 0.00005000
82: [0m
83: [32m2026-04-22 18:43:55.665[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
84: [32m2026-04-22 18:44:01.501[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0078, MAE(f): 0.1335, MAE(s): 0.0000, Time: 5.84s, lr: 0.00005000
85: [0m
86: [32m2026-04-22 18:44:03.739[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0077, MAE(f): 0.1422, MAE(s): 0.0000, Time: 2.23s, lr: 0.00005000
87: [0m
88: [32m2026-04-22 18:44:03.945[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
89: [32m2026-04-22 18:44:09.876[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0080, MAE(f): 0.1219, MAE(s): 0.0000, Time: 5.93s, lr: 0.00005000
90: [0m
91: [32m2026-04-22 18:44:12.410[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0072, MAE(f): 0.1308, MAE(s): 0.0000, Time: 2.53s, lr: 0.00005000
92: [0m
93: [32m2026-04-22 18:44:12.639[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
94: [32m2026-04-22 18:44:18.734[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0063, MAE(f): 0.1126, MAE(s): 0.0000, Time: 6.09s, lr: 0.00005000
95: [0m
96: [32m2026-04-22 18:44:21.443[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0067, MAE(f): 0.1211, MAE(s): 0.0000, Time: 2.70s, lr: 0.00005000
97: [0m
98: [32m2026-04-22 18:44:21.624[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
99: [32m2026-04-22 18:44:27.843[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0064, MAE(f): 0.1048, MAE(s): 0.0000, Time: 6.22s, lr: 0.00005000
100: [0m
101: [32m2026-04-22 18:44:30.263[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0063, MAE(f): 0.1129, MAE(s): 0.0000, Time: 2.41s, lr: 0.00005000
102: [0m
103: [32m2026-04-22 18:44:30.484[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
104: [32m2026-04-22 18:44:36.656[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0059, MAE(f): 0.0983, MAE(s): 0.0000, Time: 6.17s, lr: 0.00005000
105: [0m
106: [32m2026-04-22 18:44:39.159[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0059, MAE(f): 0.1059, MAE(s): 0.0000, Time: 2.50s, lr: 0.00005000
107: [0m
108: [32m2026-04-22 18:44:39.364[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
109: [32m2026-04-22 18:44:45.384[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0051, MAE(f): 0.0927, MAE(s): 0.0000, Time: 6.02s, lr: 0.00005000
110: [0m
111: [32m2026-04-22 18:44:47.589[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0055, MAE(f): 0.1000, MAE(s): 0.0000, Time: 2.20s, lr: 0.00005000
112: [0m
113: [32m2026-04-22 18:44:47.756[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
114: [32m2026-04-22 18:44:53.616[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0048, MAE(f): 0.0877, MAE(s): 0.0000, Time: 5.86s, lr: 0.00005000
115: [0m
116: [32m2026-04-22 18:44:55.829[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0052, MAE(f): 0.0948, MAE(s): 0.0000, Time: 2.21s, lr: 0.00005000
117: [0m
118: [32m2026-04-22 18:44:55.998[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
119: [32m2026-04-22 18:45:01.816[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0046, MAE(f): 0.0831, MAE(s): 0.0000, Time: 5.82s, lr: 0.00005000
120: [0m
121: [32m2026-04-22 18:45:03.967[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0049, MAE(f): 0.0901, MAE(s): 0.0000, Time: 2.15s, lr: 0.00005000
122: [0m
123: [32m2026-04-22 18:45:04.218[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
124: [32m2026-04-22 18:45:10.192[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0046, MAE(f): 0.0791, MAE(s): 0.0000, Time: 5.97s, lr: 0.00005000
125: [0m
126: [32m2026-04-22 18:45:12.708[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0046, MAE(f): 0.0858, MAE(s): 0.0000, Time: 2.51s, lr: 0.00005000
127: [0m
128: [32m2026-04-22 18:45:12.878[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
129: [32m2026-04-22 18:45:18.766[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0041, MAE(f): 0.0756, MAE(s): 0.0000, Time: 5.89s, lr: 0.00005000
130: [0m
131: [32m2026-04-22 18:45:21.069[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0044, MAE(f): 0.0821, MAE(s): 0.0000, Time: 2.30s, lr: 0.00005000
132: [0m
133: [32m2026-04-22 18:45:21.275[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
134: [32m2026-04-22 18:45:27.146[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0043, MAE(f): 0.0727, MAE(s): 0.0000, Time: 5.87s, lr: 0.00005000
135: [0m
136: [32m2026-04-22 18:45:29.364[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0042, MAE(f): 0.0787, MAE(s): 0.0000, Time: 2.21s, lr: 0.00005000
137: [0m
138: [32m2026-04-22 18:45:29.541[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
139: [32m2026-04-22 18:45:35.387[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0040, MAE(f): 0.0701, MAE(s): 0.0000, Time: 5.85s, lr: 0.00005000
140: [0m
141: [32m2026-04-22 18:45:37.537[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0040, MAE(f): 0.0757, MAE(s): 0.0000, Time: 2.15s, lr: 0.00005000
142: [0m
143: [32m2026-04-22 18:45:37.707[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
144: [32m2026-04-22 18:45:43.510[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0036, MAE(f): 0.0675, MAE(s): 0.0000, Time: 5.80s, lr: 0.00005000
145: [0m
146: [32m2026-04-22 18:45:45.942[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0038, MAE(f): 0.0730, MAE(s): 0.0000, Time: 2.43s, lr: 0.00005000
147: [0m
148: [32m2026-04-22 18:45:46.110[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
149: [32m2026-04-22 18:45:52.095[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0037, MAE(f): 0.0653, MAE(s): 0.0000, Time: 5.98s, lr: 0.00005000
150: [0m
151: [32m2026-04-22 18:45:54.508[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0036, MAE(f): 0.0705, MAE(s): 0.0000, Time: 2.41s, lr: 0.00005000
152: [0m
153: [32m2026-04-22 18:45:54.698[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
154: [32m2026-04-22 18:46:00.647[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0038, MAE(f): 0.0634, MAE(s): 0.0000, Time: 5.95s, lr: 0.00005000
155: [0m
156: [32m2026-04-22 18:46:03.071[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0035, MAE(f): 0.0683, MAE(s): 0.0000, Time: 2.42s, lr: 0.00005000
157: [0m
