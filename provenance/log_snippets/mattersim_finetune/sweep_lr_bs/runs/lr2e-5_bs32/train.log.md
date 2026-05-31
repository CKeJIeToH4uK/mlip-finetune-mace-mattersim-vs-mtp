# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr2e-5_bs32/train.log

Original size: 320369 bytes. Full raw log not copied.

1: [rank0]:[W225 18:06:31.249762873 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 18:06:31.909[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 18:06:34.165[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 18:06:38.843[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 18:06:39.119[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 18:06:39.119[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 18:06:46.797[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0070, MAE(e): 0.0196, MAE(f): 0.6856, MAE(s): 0.0000, Time: 7.68s, lr: 0.00002000
39: [0m
40: [32m2026-02-25 18:06:51.005[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0070, MAE(e): 0.0157, MAE(f): 0.6943, MAE(s): 0.0000, Time: 4.20s, lr: 0.00002000
41: [0m
42: [32m2026-02-25 18:06:51.011[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 18:06:53.520[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0099, MAE(f): 0.6849, MAE(s): 0.0000, Time: 2.51s, lr: 0.00002000
44: [0m
45: [32m2026-02-25 18:06:56.392[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0075, MAE(f): 0.6941, MAE(s): 0.0000, Time: 2.87s, lr: 0.00002000
46: [0m
47: [32m2026-02-25 18:06:56.398[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 18:06:58.697[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0051, MAE(f): 0.6839, MAE(s): 0.0000, Time: 2.30s, lr: 0.00002000
49: [0m
50: [32m2026-02-25 18:07:02.400[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6932, MAE(s): 0.0000, Time: 3.70s, lr: 0.00002000
51: [0m
52: [32m2026-02-25 18:07:02.408[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 18:07:05.280[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6827, MAE(s): 0.0000, Time: 2.87s, lr: 0.00002000
54: [0m
55: [32m2026-02-25 18:07:08.334[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6912, MAE(s): 0.0000, Time: 3.05s, lr: 0.00002000
56: [0m
57: [32m2026-02-25 18:07:08.341[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 18:07:11.272[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6790, MAE(s): 0.0000, Time: 2.93s, lr: 0.00002000
59: [0m
60: [32m2026-02-25 18:07:14.190[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6888, MAE(s): 0.0000, Time: 2.92s, lr: 0.00002000
61: [0m
62: [32m2026-02-25 18:07:14.195[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 18:07:17.100[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6767, MAE(s): 0.0000, Time: 2.90s, lr: 0.00002000
64: [0m
65: [32m2026-02-25 18:07:20.248[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6860, MAE(s): 0.0000, Time: 3.15s, lr: 0.00002000
66: [0m
67: [32m2026-02-25 18:07:20.255[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 18:07:23.166[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6726, MAE(s): 0.0000, Time: 2.91s, lr: 0.00002000
69: [0m
70: [32m2026-02-25 18:07:26.368[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6826, MAE(s): 0.0000, Time: 3.20s, lr: 0.00002000
71: [0m
72: [32m2026-02-25 18:07:26.374[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 18:07:28.863[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0047, MAE(f): 0.6673, MAE(s): 0.0000, Time: 2.49s, lr: 0.00002000
74: [0m
75: [32m2026-02-25 18:07:31.988[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6781, MAE(s): 0.0000, Time: 3.12s, lr: 0.00002000
76: [0m
77: [32m2026-02-25 18:07:31.993[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 18:07:34.495[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6603, MAE(s): 0.0000, Time: 2.50s, lr: 0.00002000
79: [0m
80: [32m2026-02-25 18:07:37.751[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6723, MAE(s): 0.0000, Time: 3.25s, lr: 0.00002000
81: [0m
82: [32m2026-02-25 18:07:37.757[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 18:07:40.908[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0046, MAE(f): 0.6500, MAE(s): 0.0000, Time: 3.15s, lr: 0.00002000
84: [0m
85: [32m2026-02-25 18:07:44.895[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6641, MAE(s): 0.0000, Time: 3.98s, lr: 0.00002000
86: [0m
87: [32m2026-02-25 18:07:44.900[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 18:07:47.989[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0063, MAE(e): 0.0045, MAE(f): 0.6332, MAE(s): 0.0000, Time: 3.09s, lr: 0.00002000
89: [0m
90: [32m2026-02-25 18:07:52.327[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0065, MAE(e): 0.0045, MAE(f): 0.6522, MAE(s): 0.0000, Time: 4.33s, lr: 0.00002000
91: [0m
92: [32m2026-02-25 18:07:52.338[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 18:07:54.594[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0060, MAE(e): 0.0043, MAE(f): 0.6042, MAE(s): 0.0000, Time: 2.26s, lr: 0.00002000
94: [0m
95: [32m2026-02-25 18:07:57.556[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0063, MAE(e): 0.0044, MAE(f): 0.6332, MAE(s): 0.0000, Time: 2.96s, lr: 0.00002000
96: [0m
97: [32m2026-02-25 18:07:57.561[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 18:08:00.352[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0054, MAE(e): 0.0041, MAE(f): 0.5464, MAE(s): 0.0000, Time: 2.79s, lr: 0.00002000
99: [0m
100: [32m2026-02-25 18:08:03.498[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0060, MAE(e): 0.0041, MAE(f): 0.5996, MAE(s): 0.0000, Time: 3.14s, lr: 0.00002000
101: [0m
102: [32m2026-02-25 18:08:03.504[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 18:08:06.924[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0046, MAE(e): 0.0045, MAE(f): 0.4634, MAE(s): 0.0000, Time: 3.42s, lr: 0.00002000
104: [0m
105: [32m2026-02-25 18:08:10.046[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0054, MAE(e): 0.0038, MAE(f): 0.5421, MAE(s): 0.0000, Time: 3.12s, lr: 0.00002000
106: [0m
107: [32m2026-02-25 18:08:10.052[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 18:08:12.333[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0039, MAE(e): 0.0044, MAE(f): 0.3923, MAE(s): 0.0000, Time: 2.28s, lr: 0.00002000
109: [0m
110: [32m2026-02-25 18:08:15.456[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0047, MAE(e): 0.0037, MAE(f): 0.4723, MAE(s): 0.0000, Time: 3.12s, lr: 0.00002000
111: [0m
112: [32m2026-02-25 18:08:15.463[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 18:08:18.172[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0034, MAE(e): 0.0052, MAE(f): 0.3401, MAE(s): 0.0000, Time: 2.71s, lr: 0.00002000
114: [0m
115: [32m2026-02-25 18:08:21.784[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0041, MAE(e): 0.0043, MAE(f): 0.4096, MAE(s): 0.0000, Time: 3.61s, lr: 0.00002000
116: [0m
117: [32m2026-02-25 18:08:21.789[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 18:08:24.019[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0030, MAE(e): 0.0044, MAE(f): 0.3011, MAE(s): 0.0000, Time: 2.23s, lr: 0.00002000
119: [0m
120: [32m2026-02-25 18:08:27.807[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0036, MAE(e): 0.0045, MAE(f): 0.3609, MAE(s): 0.0000, Time: 3.79s, lr: 0.00002000
121: [0m
122: [32m2026-02-25 18:08:27.813[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 18:08:29.810[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0042, MAE(f): 0.2766, MAE(s): 0.0000, Time: 2.00s, lr: 0.00002000
124: [0m
125: [32m2026-02-25 18:08:33.382[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0032, MAE(e): 0.0043, MAE(f): 0.3230, MAE(s): 0.0000, Time: 3.57s, lr: 0.00002000
126: [0m
127: [32m2026-02-25 18:08:33.387[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 18:08:36.546[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0025, MAE(e): 0.0037, MAE(f): 0.2581, MAE(s): 0.0000, Time: 3.16s, lr: 0.00002000
129: [0m
130: [32m2026-02-25 18:08:40.049[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0029, MAE(e): 0.0039, MAE(f): 0.2946, MAE(s): 0.0000, Time: 3.50s, lr: 0.00002000
131: [0m
132: [32m2026-02-25 18:08:40.056[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 18:08:42.181[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0024, MAE(e): 0.0037, MAE(f): 0.2428, MAE(s): 0.0000, Time: 2.12s, lr: 0.00002000
134: [0m
135: [32m2026-02-25 18:08:45.263[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0027, MAE(e): 0.0037, MAE(f): 0.2733, MAE(s): 0.0000, Time: 3.08s, lr: 0.00002000
136: [0m
137: [32m2026-02-25 18:08:45.270[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 18:08:48.299[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0023, MAE(e): 0.0036, MAE(f): 0.2290, MAE(s): 0.0000, Time: 3.03s, lr: 0.00002000
139: [0m
140: [32m2026-02-25 18:08:51.157[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0025, MAE(e): 0.0035, MAE(f): 0.2565, MAE(s): 0.0000, Time: 2.86s, lr: 0.00002000
141: [0m
142: [32m2026-02-25 18:08:51.161[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 18:08:53.390[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0037, MAE(f): 0.2171, MAE(s): 0.0000, Time: 2.23s, lr: 0.00002000
144: [0m
145: [32m2026-02-25 18:08:57.151[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0024, MAE(e): 0.0034, MAE(f): 0.2424, MAE(s): 0.0000, Time: 3.76s, lr: 0.00002000
146: [0m
147: [32m2026-02-25 18:08:57.155[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 18:08:59.500[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0020, MAE(e): 0.0037, MAE(f): 0.2063, MAE(s): 0.0000, Time: 2.34s, lr: 0.00002000
149: [0m
150: [32m2026-02-25 18:09:02.512[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0023, MAE(e): 0.0033, MAE(f): 0.2302, MAE(s): 0.0000, Time: 3.01s, lr: 0.00002000
151: [0m
152: [32m2026-02-25 18:09:02.516[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 18:09:04.844[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0039, MAE(f): 0.1968, MAE(s): 0.0000, Time: 2.33s, lr: 0.00002000
154: [0m
155: [32m2026-02-25 18:09:08.325[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0022, MAE(e): 0.0033, MAE(f): 0.2194, MAE(s): 0.0000, Time: 3.48s, lr: 0.00002000
156: [0m
157: [32m2026-02-25 18:09:08.334[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 18:09:10.734[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0018, MAE(e): 0.0038, MAE(f): 0.1888, MAE(s): 0.0000, Time: 2.40s, lr: 0.00002000
159: [0m
160: [32m2026-02-25 18:09:14.042[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0021, MAE(e): 0.0032, MAE(f): 0.2098, MAE(s): 0.0000, Time: 3.30s, lr: 0.00002000
161: [0m
