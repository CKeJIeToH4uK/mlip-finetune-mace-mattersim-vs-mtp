# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr5e-5_bs32/train.log

Original size: 320369 bytes. Full raw log not copied.

1: [rank0]:[W225 16:42:30.609493074 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 16:42:30.649[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 16:42:32.716[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 16:42:37.250[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 16:42:37.398[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 16:42:37.398[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 16:42:43.180[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0130, MAE(f): 0.6856, MAE(s): 0.0000, Time: 5.78s, lr: 0.00005000
39: [0m
40: [32m2026-02-25 16:42:46.378[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0051, MAE(f): 0.6941, MAE(s): 0.0000, Time: 3.19s, lr: 0.00005000
41: [0m
42: [32m2026-02-25 16:42:46.384[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 16:42:48.391[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0050, MAE(f): 0.6826, MAE(s): 0.0000, Time: 2.01s, lr: 0.00005000
44: [0m
45: [32m2026-02-25 16:42:50.967[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6902, MAE(s): 0.0000, Time: 2.57s, lr: 0.00005000
46: [0m
47: [32m2026-02-25 16:42:50.973[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 16:42:52.907[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6760, MAE(s): 0.0000, Time: 1.93s, lr: 0.00005000
49: [0m
50: [32m2026-02-25 16:42:55.476[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0049, MAE(f): 0.6840, MAE(s): 0.0000, Time: 2.57s, lr: 0.00005000
51: [0m
52: [32m2026-02-25 16:42:55.481[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 16:42:57.343[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6669, MAE(s): 0.0000, Time: 1.86s, lr: 0.00005000
54: [0m
55: [32m2026-02-25 16:42:59.921[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6742, MAE(s): 0.0000, Time: 2.58s, lr: 0.00005000
56: [0m
57: [32m2026-02-25 16:42:59.925[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 16:43:01.808[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0064, MAE(e): 0.0045, MAE(f): 0.6464, MAE(s): 0.0000, Time: 1.88s, lr: 0.00005000
59: [0m
60: [32m2026-02-25 16:43:04.282[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0065, MAE(e): 0.0045, MAE(f): 0.6558, MAE(s): 0.0000, Time: 2.47s, lr: 0.00005000
61: [0m
62: [32m2026-02-25 16:43:04.287[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 16:43:06.518[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0059, MAE(e): 0.0042, MAE(f): 0.5966, MAE(s): 0.0000, Time: 2.23s, lr: 0.00005000
64: [0m
65: [32m2026-02-25 16:43:09.096[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0061, MAE(e): 0.0042, MAE(f): 0.6123, MAE(s): 0.0000, Time: 2.58s, lr: 0.00005000
66: [0m
67: [32m2026-02-25 16:43:09.101[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 16:43:11.074[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0046, MAE(e): 0.0046, MAE(f): 0.4638, MAE(s): 0.0000, Time: 1.97s, lr: 0.00005000
69: [0m
70: [32m2026-02-25 16:43:14.885[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0049, MAE(e): 0.0037, MAE(f): 0.4925, MAE(s): 0.0000, Time: 3.81s, lr: 0.00005000
71: [0m
72: [32m2026-02-25 16:43:14.890[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 16:43:17.506[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0033, MAE(e): 0.0047, MAE(f): 0.3379, MAE(s): 0.0000, Time: 2.62s, lr: 0.00005000
74: [0m
75: [32m2026-02-25 16:43:21.519[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0037, MAE(e): 0.0054, MAE(f): 0.3685, MAE(s): 0.0000, Time: 4.01s, lr: 0.00005000
76: [0m
77: [32m2026-02-25 16:43:21.530[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 16:43:24.282[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0047, MAE(f): 0.2731, MAE(s): 0.0000, Time: 2.75s, lr: 0.00005000
79: [0m
80: [32m2026-02-25 16:43:27.297[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0029, MAE(e): 0.0050, MAE(f): 0.2934, MAE(s): 0.0000, Time: 3.01s, lr: 0.00005000
81: [0m
82: [32m2026-02-25 16:43:27.302[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 16:43:29.552[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0023, MAE(e): 0.0046, MAE(f): 0.2364, MAE(s): 0.0000, Time: 2.25s, lr: 0.00005000
84: [0m
85: [32m2026-02-25 16:43:32.068[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0025, MAE(e): 0.0039, MAE(f): 0.2537, MAE(s): 0.0000, Time: 2.51s, lr: 0.00005000
86: [0m
87: [32m2026-02-25 16:43:32.073[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 16:43:33.867[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0060, MAE(f): 0.2082, MAE(s): 0.0000, Time: 1.79s, lr: 0.00005000
89: [0m
90: [32m2026-02-25 16:43:36.243[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0022, MAE(e): 0.0037, MAE(f): 0.2252, MAE(s): 0.0000, Time: 2.37s, lr: 0.00005000
91: [0m
92: [32m2026-02-25 16:43:36.247[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 16:43:38.013[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0053, MAE(f): 0.1880, MAE(s): 0.0000, Time: 1.77s, lr: 0.00005000
94: [0m
95: [32m2026-02-25 16:43:40.430[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0020, MAE(e): 0.0034, MAE(f): 0.2034, MAE(s): 0.0000, Time: 2.42s, lr: 0.00005000
96: [0m
97: [32m2026-02-25 16:43:40.435[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 16:43:42.185[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0017, MAE(e): 0.0050, MAE(f): 0.1710, MAE(s): 0.0000, Time: 1.75s, lr: 0.00005000
99: [0m
100: [32m2026-02-25 16:43:44.513[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0018, MAE(e): 0.0032, MAE(f): 0.1859, MAE(s): 0.0000, Time: 2.33s, lr: 0.00005000
101: [0m
102: [32m2026-02-25 16:43:44.517[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 16:43:46.208[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0036, MAE(f): 0.1579, MAE(s): 0.0000, Time: 1.69s, lr: 0.00005000
104: [0m
105: [32m2026-02-25 16:43:48.568[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0017, MAE(e): 0.0030, MAE(f): 0.1713, MAE(s): 0.0000, Time: 2.36s, lr: 0.00005000
106: [0m
107: [32m2026-02-25 16:43:48.572[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 16:43:50.337[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0014, MAE(e): 0.0036, MAE(f): 0.1460, MAE(s): 0.0000, Time: 1.76s, lr: 0.00005000
109: [0m
110: [32m2026-02-25 16:43:52.761[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0028, MAE(f): 0.1590, MAE(s): 0.0000, Time: 2.42s, lr: 0.00005000
111: [0m
112: [32m2026-02-25 16:43:52.766[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 16:43:54.549[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0037, MAE(f): 0.1362, MAE(s): 0.0000, Time: 1.78s, lr: 0.00005000
114: [0m
115: [32m2026-02-25 16:43:57.034[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0026, MAE(f): 0.1484, MAE(s): 0.0000, Time: 2.48s, lr: 0.00005000
116: [0m
117: [32m2026-02-25 16:43:57.038[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 16:43:58.862[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0031, MAE(f): 0.1272, MAE(s): 0.0000, Time: 1.82s, lr: 0.00005000
119: [0m
120: [32m2026-02-25 16:44:01.461[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0024, MAE(f): 0.1391, MAE(s): 0.0000, Time: 2.60s, lr: 0.00005000
121: [0m
122: [32m2026-02-25 16:44:01.465[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 16:44:03.260[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0030, MAE(f): 0.1196, MAE(s): 0.0000, Time: 1.79s, lr: 0.00005000
124: [0m
125: [32m2026-02-25 16:44:05.826[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0022, MAE(f): 0.1308, MAE(s): 0.0000, Time: 2.56s, lr: 0.00005000
126: [0m
127: [32m2026-02-25 16:44:05.830[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 16:44:07.693[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0044, MAE(f): 0.1130, MAE(s): 0.0000, Time: 1.86s, lr: 0.00005000
129: [0m
130: [32m2026-02-25 16:44:10.263[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0021, MAE(f): 0.1235, MAE(s): 0.0000, Time: 2.57s, lr: 0.00005000
131: [0m
132: [32m2026-02-25 16:44:10.268[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 16:44:12.012[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0032, MAE(f): 0.1078, MAE(s): 0.0000, Time: 1.74s, lr: 0.00005000
134: [0m
135: [32m2026-02-25 16:44:14.422[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0020, MAE(f): 0.1172, MAE(s): 0.0000, Time: 2.41s, lr: 0.00005000
136: [0m
137: [32m2026-02-25 16:44:14.426[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 16:44:16.192[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0028, MAE(f): 0.1041, MAE(s): 0.0000, Time: 1.77s, lr: 0.00005000
139: [0m
140: [32m2026-02-25 16:44:18.536[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0019, MAE(f): 0.1120, MAE(s): 0.0000, Time: 2.34s, lr: 0.00005000
141: [0m
142: [32m2026-02-25 16:44:18.540[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 16:44:20.296[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0022, MAE(f): 0.1009, MAE(s): 0.0000, Time: 1.75s, lr: 0.00005000
144: [0m
145: [32m2026-02-25 16:44:22.710[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0018, MAE(f): 0.1078, MAE(s): 0.0000, Time: 2.41s, lr: 0.00005000
146: [0m
147: [32m2026-02-25 16:44:22.714[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 16:44:24.413[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0021, MAE(f): 0.0979, MAE(s): 0.0000, Time: 1.70s, lr: 0.00005000
149: [0m
150: [32m2026-02-25 16:44:26.702[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0018, MAE(f): 0.1043, MAE(s): 0.0000, Time: 2.29s, lr: 0.00005000
151: [0m
152: [32m2026-02-25 16:44:26.706[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 16:44:28.362[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0021, MAE(f): 0.0955, MAE(s): 0.0000, Time: 1.66s, lr: 0.00005000
154: [0m
155: [32m2026-02-25 16:44:30.765[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0017, MAE(f): 0.1014, MAE(s): 0.0000, Time: 2.40s, lr: 0.00005000
156: [0m
157: [32m2026-02-25 16:44:30.769[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 16:44:32.468[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0020, MAE(f): 0.0931, MAE(s): 0.0000, Time: 1.70s, lr: 0.00005000
159: [0m
160: [32m2026-02-25 16:44:34.851[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0017, MAE(f): 0.0989, MAE(s): 0.0000, Time: 2.38s, lr: 0.00005000
161: [0m
