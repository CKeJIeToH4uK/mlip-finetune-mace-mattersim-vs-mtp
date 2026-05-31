# Log Snippet: repo/coursework/mattersim_finetune/shift/train.log

Original size: 320416 bytes. Full raw log not copied.

1: [rank0]:[W225 22:02:36.417878863 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 22:02:37.620[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 22:02:43.169[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 22:02:47.187[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 22:02:49.214[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,129[0m
33: [32m2026-02-25 22:02:49.214[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 22:03:07.445[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0130, MAE(f): 0.6856, MAE(s): 0.0000, Time: 18.23s, lr: 0.00005000
39: [0m
40: [32m2026-02-25 22:03:10.918[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0051, MAE(f): 0.6941, MAE(s): 0.0000, Time: 3.47s, lr: 0.00005000
41: [0m
42: [32m2026-02-25 22:03:11.235[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 22:03:13.866[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0050, MAE(f): 0.6826, MAE(s): 0.0000, Time: 2.63s, lr: 0.00005000
44: [0m
45: [32m2026-02-25 22:03:16.698[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6902, MAE(s): 0.0000, Time: 2.83s, lr: 0.00005000
46: [0m
47: [32m2026-02-25 22:03:16.855[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 22:03:19.591[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6760, MAE(s): 0.0000, Time: 2.73s, lr: 0.00005000
49: [0m
50: [32m2026-02-25 22:03:22.455[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0049, MAE(f): 0.6840, MAE(s): 0.0000, Time: 2.86s, lr: 0.00005000
51: [0m
52: [32m2026-02-25 22:03:22.607[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 22:03:25.183[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6669, MAE(s): 0.0000, Time: 2.58s, lr: 0.00005000
54: [0m
55: [32m2026-02-25 22:03:27.700[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6742, MAE(s): 0.0000, Time: 2.51s, lr: 0.00005000
56: [0m
57: [32m2026-02-25 22:03:27.855[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 22:03:30.374[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0064, MAE(e): 0.0045, MAE(f): 0.6464, MAE(s): 0.0000, Time: 2.52s, lr: 0.00005000
59: [0m
60: [32m2026-02-25 22:03:32.858[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0065, MAE(e): 0.0045, MAE(f): 0.6558, MAE(s): 0.0000, Time: 2.48s, lr: 0.00005000
61: [0m
62: [32m2026-02-25 22:03:33.009[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 22:03:35.607[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0059, MAE(e): 0.0042, MAE(f): 0.5966, MAE(s): 0.0000, Time: 2.60s, lr: 0.00005000
64: [0m
65: [32m2026-02-25 22:03:38.212[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0061, MAE(e): 0.0042, MAE(f): 0.6123, MAE(s): 0.0000, Time: 2.60s, lr: 0.00005000
66: [0m
67: [32m2026-02-25 22:03:38.365[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 22:03:40.669[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0046, MAE(e): 0.0046, MAE(f): 0.4639, MAE(s): 0.0000, Time: 2.30s, lr: 0.00005000
69: [0m
70: [32m2026-02-25 22:03:43.607[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0049, MAE(e): 0.0037, MAE(f): 0.4925, MAE(s): 0.0000, Time: 2.93s, lr: 0.00005000
71: [0m
72: [32m2026-02-25 22:03:43.769[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 22:03:46.197[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0033, MAE(e): 0.0047, MAE(f): 0.3379, MAE(s): 0.0000, Time: 2.43s, lr: 0.00005000
74: [0m
75: [32m2026-02-25 22:03:49.251[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0037, MAE(e): 0.0054, MAE(f): 0.3685, MAE(s): 0.0000, Time: 3.05s, lr: 0.00005000
76: [0m
77: [32m2026-02-25 22:03:49.408[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 22:03:52.076[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0047, MAE(f): 0.2731, MAE(s): 0.0000, Time: 2.67s, lr: 0.00005000
79: [0m
80: [32m2026-02-25 22:03:54.652[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0029, MAE(e): 0.0050, MAE(f): 0.2934, MAE(s): 0.0000, Time: 2.57s, lr: 0.00005000
81: [0m
82: [32m2026-02-25 22:03:54.803[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 22:03:57.314[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0023, MAE(e): 0.0046, MAE(f): 0.2365, MAE(s): 0.0000, Time: 2.51s, lr: 0.00005000
84: [0m
85: [32m2026-02-25 22:03:59.912[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0025, MAE(e): 0.0039, MAE(f): 0.2537, MAE(s): 0.0000, Time: 2.59s, lr: 0.00005000
86: [0m
87: [32m2026-02-25 22:04:00.067[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 22:04:02.430[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0060, MAE(f): 0.2083, MAE(s): 0.0000, Time: 2.36s, lr: 0.00005000
89: [0m
90: [32m2026-02-25 22:04:04.914[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0022, MAE(e): 0.0037, MAE(f): 0.2253, MAE(s): 0.0000, Time: 2.48s, lr: 0.00005000
91: [0m
92: [32m2026-02-25 22:04:05.068[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 22:04:07.344[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0053, MAE(f): 0.1880, MAE(s): 0.0000, Time: 2.28s, lr: 0.00005000
94: [0m
95: [32m2026-02-25 22:04:09.864[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0020, MAE(e): 0.0034, MAE(f): 0.2034, MAE(s): 0.0000, Time: 2.52s, lr: 0.00005000
96: [0m
97: [32m2026-02-25 22:04:10.019[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 22:04:12.339[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0017, MAE(e): 0.0050, MAE(f): 0.1711, MAE(s): 0.0000, Time: 2.32s, lr: 0.00005000
99: [0m
100: [32m2026-02-25 22:04:14.855[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0018, MAE(e): 0.0032, MAE(f): 0.1859, MAE(s): 0.0000, Time: 2.51s, lr: 0.00005000
101: [0m
102: [32m2026-02-25 22:04:15.009[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 22:04:17.487[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0036, MAE(f): 0.1579, MAE(s): 0.0000, Time: 2.48s, lr: 0.00005000
104: [0m
105: [32m2026-02-25 22:04:20.071[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0017, MAE(e): 0.0030, MAE(f): 0.1714, MAE(s): 0.0000, Time: 2.58s, lr: 0.00005000
106: [0m
107: [32m2026-02-25 22:04:20.230[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 22:04:22.627[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0014, MAE(e): 0.0036, MAE(f): 0.1460, MAE(s): 0.0000, Time: 2.40s, lr: 0.00005000
109: [0m
110: [32m2026-02-25 22:04:25.940[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0028, MAE(f): 0.1591, MAE(s): 0.0000, Time: 3.31s, lr: 0.00005000
111: [0m
112: [32m2026-02-25 22:04:26.102[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 22:04:28.639[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0037, MAE(f): 0.1362, MAE(s): 0.0000, Time: 2.54s, lr: 0.00005000
114: [0m
115: [32m2026-02-25 22:04:32.025[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0026, MAE(f): 0.1484, MAE(s): 0.0000, Time: 3.38s, lr: 0.00005000
116: [0m
117: [32m2026-02-25 22:04:32.189[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 22:04:35.282[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0031, MAE(f): 0.1272, MAE(s): 0.0000, Time: 3.09s, lr: 0.00005000
119: [0m
120: [32m2026-02-25 22:04:38.080[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0024, MAE(f): 0.1391, MAE(s): 0.0000, Time: 2.79s, lr: 0.00005000
121: [0m
122: [32m2026-02-25 22:04:38.261[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 22:04:40.646[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0030, MAE(f): 0.1197, MAE(s): 0.0000, Time: 2.38s, lr: 0.00005000
124: [0m
125: [32m2026-02-25 22:04:43.332[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0022, MAE(f): 0.1309, MAE(s): 0.0000, Time: 2.68s, lr: 0.00005000
126: [0m
127: [32m2026-02-25 22:04:43.496[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 22:04:46.350[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0044, MAE(f): 0.1130, MAE(s): 0.0000, Time: 2.85s, lr: 0.00005000
129: [0m
130: [32m2026-02-25 22:04:48.992[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0021, MAE(f): 0.1235, MAE(s): 0.0000, Time: 2.64s, lr: 0.00005000
131: [0m
132: [32m2026-02-25 22:04:49.155[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 22:04:51.964[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0032, MAE(f): 0.1078, MAE(s): 0.0000, Time: 2.81s, lr: 0.00005000
134: [0m
135: [32m2026-02-25 22:04:54.648[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0020, MAE(f): 0.1172, MAE(s): 0.0000, Time: 2.68s, lr: 0.00005000
136: [0m
137: [32m2026-02-25 22:04:54.806[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 22:04:57.447[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0028, MAE(f): 0.1041, MAE(s): 0.0000, Time: 2.64s, lr: 0.00005000
139: [0m
140: [32m2026-02-25 22:05:00.090[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0019, MAE(f): 0.1120, MAE(s): 0.0000, Time: 2.64s, lr: 0.00005000
141: [0m
142: [32m2026-02-25 22:05:00.338[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 22:05:03.138[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0022, MAE(f): 0.1009, MAE(s): 0.0000, Time: 2.80s, lr: 0.00005000
144: [0m
145: [32m2026-02-25 22:05:05.937[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0018, MAE(f): 0.1078, MAE(s): 0.0000, Time: 2.79s, lr: 0.00005000
146: [0m
147: [32m2026-02-25 22:05:06.101[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 22:05:08.841[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0021, MAE(f): 0.0979, MAE(s): 0.0000, Time: 2.74s, lr: 0.00005000
149: [0m
150: [32m2026-02-25 22:05:11.869[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0018, MAE(f): 0.1044, MAE(s): 0.0000, Time: 3.02s, lr: 0.00005000
151: [0m
152: [32m2026-02-25 22:05:12.033[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 22:05:14.739[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0021, MAE(f): 0.0956, MAE(s): 0.0000, Time: 2.71s, lr: 0.00005000
154: [0m
155: [32m2026-02-25 22:05:17.661[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0017, MAE(f): 0.1014, MAE(s): 0.0000, Time: 2.92s, lr: 0.00005000
156: [0m
157: [32m2026-02-25 22:05:17.822[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 22:05:20.227[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0020, MAE(f): 0.0931, MAE(s): 0.0000, Time: 2.41s, lr: 0.00005000
159: [0m
160: [32m2026-02-25 22:05:23.483[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0017, MAE(f): 0.0989, MAE(s): 0.0000, Time: 3.25s, lr: 0.00005000
161: [0m
