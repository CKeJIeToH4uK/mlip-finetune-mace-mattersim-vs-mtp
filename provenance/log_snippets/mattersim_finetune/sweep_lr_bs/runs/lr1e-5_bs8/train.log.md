# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr1e-5_bs8/train.log

Original size: 320388 bytes. Full raw log not copied.

1: [rank0]:[W225 18:48:46.200936799 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 18:48:46.667[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 18:48:48.067[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 18:48:51.004[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 18:48:51.110[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 18:48:51.110[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 18:49:00.204[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0149, MAE(f): 0.6850, MAE(s): 0.0000, Time: 9.09s, lr: 0.00001000
39: [0m
40: [32m2026-02-25 18:49:09.672[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0080, MAE(f): 0.6936, MAE(s): 0.0000, Time: 9.47s, lr: 0.00001000
41: [0m
42: [32m2026-02-25 18:49:09.678[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 18:49:14.363[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0050, MAE(f): 0.6827, MAE(s): 0.0000, Time: 4.68s, lr: 0.00001000
44: [0m
45: [32m2026-02-25 18:49:22.050[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6907, MAE(s): 0.0000, Time: 7.69s, lr: 0.00001000
46: [0m
47: [32m2026-02-25 18:49:22.053[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 18:49:27.474[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6780, MAE(s): 0.0000, Time: 5.42s, lr: 0.00001000
49: [0m
50: [32m2026-02-25 18:49:36.830[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6857, MAE(s): 0.0000, Time: 9.35s, lr: 0.00001000
51: [0m
52: [32m2026-02-25 18:49:36.837[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 18:49:43.085[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6703, MAE(s): 0.0000, Time: 6.25s, lr: 0.00001000
54: [0m
55: [32m2026-02-25 18:49:53.996[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6781, MAE(s): 0.0000, Time: 10.91s, lr: 0.00001000
56: [0m
57: [32m2026-02-25 18:49:54.001[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 18:50:00.315[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0047, MAE(f): 0.6558, MAE(s): 0.0000, Time: 6.31s, lr: 0.00001000
59: [0m
60: [32m2026-02-25 18:50:10.618[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6648, MAE(s): 0.0000, Time: 10.30s, lr: 0.00001000
61: [0m
62: [32m2026-02-25 18:50:10.621[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 18:50:16.088[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0062, MAE(e): 0.0045, MAE(f): 0.6226, MAE(s): 0.0000, Time: 5.47s, lr: 0.00001000
64: [0m
65: [32m2026-02-25 18:50:26.184[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0063, MAE(e): 0.0044, MAE(f): 0.6366, MAE(s): 0.0000, Time: 10.09s, lr: 0.00001000
66: [0m
67: [32m2026-02-25 18:50:26.188[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 18:50:31.706[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0051, MAE(e): 0.0042, MAE(f): 0.5182, MAE(s): 0.0000, Time: 5.52s, lr: 0.00001000
69: [0m
70: [32m2026-02-25 18:50:40.901[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0055, MAE(e): 0.0038, MAE(f): 0.5553, MAE(s): 0.0000, Time: 9.19s, lr: 0.00001000
71: [0m
72: [32m2026-02-25 18:50:40.906[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 18:50:46.856[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0038, MAE(e): 0.0054, MAE(f): 0.3868, MAE(s): 0.0000, Time: 5.95s, lr: 0.00001000
74: [0m
75: [32m2026-02-25 18:50:56.776[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0043, MAE(e): 0.0038, MAE(f): 0.4329, MAE(s): 0.0000, Time: 9.92s, lr: 0.00001000
76: [0m
77: [32m2026-02-25 18:50:56.779[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 18:51:02.296[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0031, MAE(e): 0.0041, MAE(f): 0.3150, MAE(s): 0.0000, Time: 5.52s, lr: 0.00001000
79: [0m
80: [32m2026-02-25 18:51:11.919[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0035, MAE(e): 0.0040, MAE(f): 0.3500, MAE(s): 0.0000, Time: 9.62s, lr: 0.00001000
81: [0m
82: [32m2026-02-25 18:51:11.923[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 18:51:17.432[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0046, MAE(f): 0.2737, MAE(s): 0.0000, Time: 5.51s, lr: 0.00001000
84: [0m
85: [32m2026-02-25 18:51:27.561[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0030, MAE(e): 0.0037, MAE(f): 0.2991, MAE(s): 0.0000, Time: 10.13s, lr: 0.00001000
86: [0m
87: [32m2026-02-25 18:51:27.565[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 18:51:33.205[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0025, MAE(e): 0.0042, MAE(f): 0.2495, MAE(s): 0.0000, Time: 5.64s, lr: 0.00001000
89: [0m
90: [32m2026-02-25 18:51:42.914[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0026, MAE(e): 0.0035, MAE(f): 0.2683, MAE(s): 0.0000, Time: 9.71s, lr: 0.00001000
91: [0m
92: [32m2026-02-25 18:51:42.917[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 18:51:48.366[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0023, MAE(e): 0.0040, MAE(f): 0.2313, MAE(s): 0.0000, Time: 5.45s, lr: 0.00001000
94: [0m
95: [32m2026-02-25 18:51:56.504[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0024, MAE(e): 0.0034, MAE(f): 0.2472, MAE(s): 0.0000, Time: 8.14s, lr: 0.00001000
96: [0m
97: [32m2026-02-25 18:51:56.507[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 18:52:01.642[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0039, MAE(f): 0.2153, MAE(s): 0.0000, Time: 5.13s, lr: 0.00001000
99: [0m
100: [32m2026-02-25 18:52:11.142[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0023, MAE(e): 0.0034, MAE(f): 0.2307, MAE(s): 0.0000, Time: 9.50s, lr: 0.00001000
101: [0m
102: [32m2026-02-25 18:52:11.148[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 18:52:16.594[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0020, MAE(e): 0.0036, MAE(f): 0.2022, MAE(s): 0.0000, Time: 5.45s, lr: 0.00001000
104: [0m
105: [32m2026-02-25 18:52:25.678[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0021, MAE(e): 0.0033, MAE(f): 0.2168, MAE(s): 0.0000, Time: 9.08s, lr: 0.00001000
106: [0m
107: [32m2026-02-25 18:52:25.682[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 18:52:31.233[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0038, MAE(f): 0.1903, MAE(s): 0.0000, Time: 5.55s, lr: 0.00001000
109: [0m
110: [32m2026-02-25 18:52:41.713[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0020, MAE(e): 0.0032, MAE(f): 0.2045, MAE(s): 0.0000, Time: 10.48s, lr: 0.00001000
111: [0m
112: [32m2026-02-25 18:52:41.717[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 18:52:47.655[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0018, MAE(e): 0.0036, MAE(f): 0.1803, MAE(s): 0.0000, Time: 5.94s, lr: 0.00001000
114: [0m
115: [32m2026-02-25 18:52:57.163[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0019, MAE(e): 0.0031, MAE(f): 0.1933, MAE(s): 0.0000, Time: 9.51s, lr: 0.00001000
116: [0m
117: [32m2026-02-25 18:52:57.169[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 18:53:03.099[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0017, MAE(e): 0.0035, MAE(f): 0.1706, MAE(s): 0.0000, Time: 5.93s, lr: 0.00001000
119: [0m
120: [32m2026-02-25 18:53:11.957[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0018, MAE(e): 0.0030, MAE(f): 0.1830, MAE(s): 0.0000, Time: 8.86s, lr: 0.00001000
121: [0m
122: [32m2026-02-25 18:53:11.961[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 18:53:18.046[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0016, MAE(e): 0.0032, MAE(f): 0.1624, MAE(s): 0.0000, Time: 6.08s, lr: 0.00001000
124: [0m
125: [32m2026-02-25 18:53:28.624[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0017, MAE(e): 0.0029, MAE(f): 0.1737, MAE(s): 0.0000, Time: 10.58s, lr: 0.00001000
126: [0m
127: [32m2026-02-25 18:53:28.628[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 18:53:35.025[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0033, MAE(f): 0.1549, MAE(s): 0.0000, Time: 6.40s, lr: 0.00001000
129: [0m
130: [32m2026-02-25 18:53:43.601[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0016, MAE(e): 0.0027, MAE(f): 0.1652, MAE(s): 0.0000, Time: 8.58s, lr: 0.00001000
131: [0m
132: [32m2026-02-25 18:53:43.605[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 18:53:50.086[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0014, MAE(e): 0.0028, MAE(f): 0.1477, MAE(s): 0.0000, Time: 6.48s, lr: 0.00001000
134: [0m
135: [32m2026-02-25 18:54:01.176[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0026, MAE(f): 0.1574, MAE(s): 0.0000, Time: 11.09s, lr: 0.00001000
136: [0m
137: [32m2026-02-25 18:54:01.181[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 18:54:07.226[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0014, MAE(e): 0.0029, MAE(f): 0.1414, MAE(s): 0.0000, Time: 6.04s, lr: 0.00001000
139: [0m
140: [32m2026-02-25 18:54:18.111[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0025, MAE(f): 0.1503, MAE(s): 0.0000, Time: 10.88s, lr: 0.00001000
141: [0m
142: [32m2026-02-25 18:54:18.116[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 18:54:24.157[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0028, MAE(f): 0.1356, MAE(s): 0.0000, Time: 6.04s, lr: 0.00001000
144: [0m
145: [32m2026-02-25 18:54:35.130[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0024, MAE(f): 0.1437, MAE(s): 0.0000, Time: 10.97s, lr: 0.00001000
146: [0m
147: [32m2026-02-25 18:54:35.134[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 18:54:41.131[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0031, MAE(f): 0.1301, MAE(s): 0.0000, Time: 6.00s, lr: 0.00001000
149: [0m
150: [32m2026-02-25 18:54:50.681[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0023, MAE(f): 0.1375, MAE(s): 0.0000, Time: 9.55s, lr: 0.00001000
151: [0m
152: [32m2026-02-25 18:54:50.686[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 18:54:56.635[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0025, MAE(f): 0.1246, MAE(s): 0.0000, Time: 5.95s, lr: 0.00001000
154: [0m
155: [32m2026-02-25 18:55:07.659[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0022, MAE(f): 0.1319, MAE(s): 0.0000, Time: 11.02s, lr: 0.00001000
156: [0m
157: [32m2026-02-25 18:55:07.664[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 18:55:13.607[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0026, MAE(f): 0.1200, MAE(s): 0.0000, Time: 5.94s, lr: 0.00001000
159: [0m
160: [32m2026-02-25 18:55:24.346[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0022, MAE(f): 0.1266, MAE(s): 0.0000, Time: 10.74s, lr: 0.00001000
161: [0m
