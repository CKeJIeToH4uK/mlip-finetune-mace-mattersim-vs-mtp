# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr1e-5_bs16/train.log

Original size: 320369 bytes. Full raw log not copied.

1: [rank0]:[W225 18:49:47.808485971 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 18:49:48.367[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 18:49:50.461[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 18:49:54.904[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 18:49:55.109[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 18:49:55.110[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 18:50:02.692[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0195, MAE(f): 0.6852, MAE(s): 0.0000, Time: 7.58s, lr: 0.00001000
39: [0m
40: [32m2026-02-25 18:50:08.712[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0070, MAE(e): 0.0157, MAE(f): 0.6940, MAE(s): 0.0000, Time: 6.02s, lr: 0.00001000
41: [0m
42: [32m2026-02-25 18:50:08.718[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 18:50:12.543[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0099, MAE(f): 0.6836, MAE(s): 0.0000, Time: 3.82s, lr: 0.00001000
44: [0m
45: [32m2026-02-25 18:50:17.464[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0078, MAE(f): 0.6937, MAE(s): 0.0000, Time: 4.92s, lr: 0.00001000
46: [0m
47: [32m2026-02-25 18:50:17.469[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 18:50:21.159[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0053, MAE(f): 0.6834, MAE(s): 0.0000, Time: 3.69s, lr: 0.00001000
49: [0m
50: [32m2026-02-25 18:50:25.942[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0051, MAE(f): 0.6925, MAE(s): 0.0000, Time: 4.78s, lr: 0.00001000
51: [0m
52: [32m2026-02-25 18:50:25.947[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 18:50:29.576[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0049, MAE(f): 0.6819, MAE(s): 0.0000, Time: 3.63s, lr: 0.00001000
54: [0m
55: [32m2026-02-25 18:50:34.304[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0049, MAE(f): 0.6905, MAE(s): 0.0000, Time: 4.73s, lr: 0.00001000
56: [0m
57: [32m2026-02-25 18:50:34.309[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 18:50:37.882[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6784, MAE(s): 0.0000, Time: 3.57s, lr: 0.00001000
59: [0m
60: [32m2026-02-25 18:50:42.885[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6880, MAE(s): 0.0000, Time: 5.00s, lr: 0.00001000
61: [0m
62: [32m2026-02-25 18:50:42.890[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 18:50:46.494[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6757, MAE(s): 0.0000, Time: 3.60s, lr: 0.00001000
64: [0m
65: [32m2026-02-25 18:50:51.660[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6850, MAE(s): 0.0000, Time: 5.16s, lr: 0.00001000
66: [0m
67: [32m2026-02-25 18:50:51.666[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 18:50:55.307[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6721, MAE(s): 0.0000, Time: 3.64s, lr: 0.00001000
69: [0m
70: [32m2026-02-25 18:51:00.172[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6812, MAE(s): 0.0000, Time: 4.86s, lr: 0.00001000
71: [0m
72: [32m2026-02-25 18:51:00.177[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 18:51:03.814[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0047, MAE(f): 0.6663, MAE(s): 0.0000, Time: 3.64s, lr: 0.00001000
74: [0m
75: [32m2026-02-25 18:51:08.606[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6762, MAE(s): 0.0000, Time: 4.79s, lr: 0.00001000
76: [0m
77: [32m2026-02-25 18:51:08.611[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 18:51:12.505[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0045, MAE(f): 0.6566, MAE(s): 0.0000, Time: 3.89s, lr: 0.00001000
79: [0m
80: [32m2026-02-25 18:51:17.497[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6693, MAE(s): 0.0000, Time: 4.99s, lr: 0.00001000
81: [0m
82: [32m2026-02-25 18:51:17.501[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 18:51:21.100[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0064, MAE(e): 0.0046, MAE(f): 0.6428, MAE(s): 0.0000, Time: 3.60s, lr: 0.00001000
84: [0m
85: [32m2026-02-25 18:51:25.886[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6594, MAE(s): 0.0000, Time: 4.78s, lr: 0.00001000
86: [0m
87: [32m2026-02-25 18:51:25.890[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 18:51:29.459[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0062, MAE(e): 0.0045, MAE(f): 0.6217, MAE(s): 0.0000, Time: 3.57s, lr: 0.00001000
89: [0m
90: [32m2026-02-25 18:51:35.697[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0064, MAE(e): 0.0044, MAE(f): 0.6439, MAE(s): 0.0000, Time: 6.24s, lr: 0.00001000
91: [0m
92: [32m2026-02-25 18:51:35.710[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 18:51:40.371[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0057, MAE(e): 0.0042, MAE(f): 0.5755, MAE(s): 0.0000, Time: 4.66s, lr: 0.00001000
94: [0m
95: [32m2026-02-25 18:51:45.273[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0061, MAE(e): 0.0042, MAE(f): 0.6164, MAE(s): 0.0000, Time: 4.90s, lr: 0.00001000
96: [0m
97: [32m2026-02-25 18:51:45.278[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 18:51:48.838[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0049, MAE(e): 0.0044, MAE(f): 0.4939, MAE(s): 0.0000, Time: 3.56s, lr: 0.00001000
99: [0m
100: [32m2026-02-25 18:51:53.703[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0056, MAE(e): 0.0038, MAE(f): 0.5657, MAE(s): 0.0000, Time: 4.86s, lr: 0.00001000
101: [0m
102: [32m2026-02-25 18:51:53.708[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 18:51:57.195[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0041, MAE(e): 0.0041, MAE(f): 0.4147, MAE(s): 0.0000, Time: 3.49s, lr: 0.00001000
104: [0m
105: [32m2026-02-25 18:52:01.938[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0049, MAE(e): 0.0036, MAE(f): 0.4975, MAE(s): 0.0000, Time: 4.74s, lr: 0.00001000
106: [0m
107: [32m2026-02-25 18:52:01.944[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 18:52:05.487[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0036, MAE(e): 0.0051, MAE(f): 0.3588, MAE(s): 0.0000, Time: 3.54s, lr: 0.00001000
109: [0m
110: [32m2026-02-25 18:52:10.232[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0043, MAE(e): 0.0038, MAE(f): 0.4310, MAE(s): 0.0000, Time: 4.74s, lr: 0.00001000
111: [0m
112: [32m2026-02-25 18:52:10.236[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 18:52:13.779[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0032, MAE(e): 0.0051, MAE(f): 0.3191, MAE(s): 0.0000, Time: 3.54s, lr: 0.00001000
114: [0m
115: [32m2026-02-25 18:52:18.456[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0038, MAE(e): 0.0040, MAE(f): 0.3790, MAE(s): 0.0000, Time: 4.68s, lr: 0.00001000
116: [0m
117: [32m2026-02-25 18:52:18.460[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 18:52:21.966[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0029, MAE(e): 0.0041, MAE(f): 0.2902, MAE(s): 0.0000, Time: 3.51s, lr: 0.00001000
119: [0m
120: [32m2026-02-25 18:52:26.697[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0034, MAE(e): 0.0040, MAE(f): 0.3398, MAE(s): 0.0000, Time: 4.73s, lr: 0.00001000
121: [0m
122: [32m2026-02-25 18:52:26.701[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 18:52:30.203[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0038, MAE(f): 0.2704, MAE(s): 0.0000, Time: 3.50s, lr: 0.00001000
124: [0m
125: [32m2026-02-25 18:52:34.927[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0031, MAE(e): 0.0038, MAE(f): 0.3097, MAE(s): 0.0000, Time: 4.72s, lr: 0.00001000
126: [0m
127: [32m2026-02-25 18:52:34.932[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 18:52:38.464[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0025, MAE(e): 0.0037, MAE(f): 0.2556, MAE(s): 0.0000, Time: 3.53s, lr: 0.00001000
129: [0m
130: [32m2026-02-25 18:52:43.285[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0028, MAE(e): 0.0037, MAE(f): 0.2870, MAE(s): 0.0000, Time: 4.82s, lr: 0.00001000
131: [0m
132: [32m2026-02-25 18:52:43.290[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 18:52:46.828[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0024, MAE(e): 0.0039, MAE(f): 0.2427, MAE(s): 0.0000, Time: 3.54s, lr: 0.00001000
134: [0m
135: [32m2026-02-25 18:52:51.793[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0027, MAE(e): 0.0035, MAE(f): 0.2695, MAE(s): 0.0000, Time: 4.96s, lr: 0.00001000
136: [0m
137: [32m2026-02-25 18:52:51.798[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 18:52:55.336[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0023, MAE(e): 0.0037, MAE(f): 0.2315, MAE(s): 0.0000, Time: 3.54s, lr: 0.00001000
139: [0m
140: [32m2026-02-25 18:53:00.308[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0025, MAE(e): 0.0035, MAE(f): 0.2554, MAE(s): 0.0000, Time: 4.97s, lr: 0.00001000
141: [0m
142: [32m2026-02-25 18:53:00.313[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 18:53:03.882[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0022, MAE(e): 0.0037, MAE(f): 0.2212, MAE(s): 0.0000, Time: 3.57s, lr: 0.00001000
144: [0m
145: [32m2026-02-25 18:53:08.742[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0024, MAE(e): 0.0034, MAE(f): 0.2434, MAE(s): 0.0000, Time: 4.86s, lr: 0.00001000
146: [0m
147: [32m2026-02-25 18:53:08.746[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 18:53:12.785[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0036, MAE(f): 0.2119, MAE(s): 0.0000, Time: 4.04s, lr: 0.00001000
149: [0m
150: [32m2026-02-25 18:53:17.911[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0023, MAE(e): 0.0034, MAE(f): 0.2331, MAE(s): 0.0000, Time: 5.12s, lr: 0.00001000
151: [0m
152: [32m2026-02-25 18:53:17.916[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 18:53:21.488[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0020, MAE(e): 0.0039, MAE(f): 0.2035, MAE(s): 0.0000, Time: 3.57s, lr: 0.00001000
154: [0m
155: [32m2026-02-25 18:53:26.318[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0022, MAE(e): 0.0033, MAE(f): 0.2240, MAE(s): 0.0000, Time: 4.83s, lr: 0.00001000
156: [0m
157: [32m2026-02-25 18:53:26.322[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 18:53:29.863[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0037, MAE(f): 0.1964, MAE(s): 0.0000, Time: 3.54s, lr: 0.00001000
159: [0m
160: [32m2026-02-25 18:53:34.640[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0021, MAE(e): 0.0033, MAE(f): 0.2157, MAE(s): 0.0000, Time: 4.77s, lr: 0.00001000
161: [0m
