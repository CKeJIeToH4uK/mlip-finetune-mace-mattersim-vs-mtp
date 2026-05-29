# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr1e-4_bs64/train.log

Original size: 320369 bytes. Full raw log not copied.

1: [rank0]:[W225 16:12:34.362072967 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 16:12:34.800[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 16:12:37.688[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 16:12:42.031[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 16:12:42.409[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 16:12:42.410[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 16:12:48.068[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0136, MAE(f): 0.6854, MAE(s): 0.0000, Time: 5.66s, lr: 0.00010000
39: [0m
40: [32m2026-02-25 16:12:50.632[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0051, MAE(f): 0.6949, MAE(s): 0.0000, Time: 2.56s, lr: 0.00010000
41: [0m
42: [32m2026-02-25 16:12:50.637[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 16:12:52.175[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0059, MAE(f): 0.6837, MAE(s): 0.0000, Time: 1.54s, lr: 0.00010000
44: [0m
45: [32m2026-02-25 16:12:54.186[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0057, MAE(f): 0.6917, MAE(s): 0.0000, Time: 2.01s, lr: 0.00010000
46: [0m
47: [32m2026-02-25 16:12:54.191[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 16:12:55.676[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0051, MAE(f): 0.6783, MAE(s): 0.0000, Time: 1.48s, lr: 0.00010000
49: [0m
50: [32m2026-02-25 16:12:57.399[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0051, MAE(f): 0.6866, MAE(s): 0.0000, Time: 1.72s, lr: 0.00010000
51: [0m
52: [32m2026-02-25 16:12:57.404[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 16:12:58.790[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0052, MAE(f): 0.6714, MAE(s): 0.0000, Time: 1.39s, lr: 0.00010000
54: [0m
55: [32m2026-02-25 16:13:00.565[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0049, MAE(f): 0.6798, MAE(s): 0.0000, Time: 1.77s, lr: 0.00010000
56: [0m
57: [32m2026-02-25 16:13:00.569[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 16:13:01.991[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6603, MAE(s): 0.0000, Time: 1.42s, lr: 0.00010000
59: [0m
60: [32m2026-02-25 16:13:03.795[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0046, MAE(f): 0.6694, MAE(s): 0.0000, Time: 1.80s, lr: 0.00010000
61: [0m
62: [32m2026-02-25 16:13:03.800[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 16:13:05.259[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0064, MAE(e): 0.0046, MAE(f): 0.6404, MAE(s): 0.0000, Time: 1.46s, lr: 0.00010000
64: [0m
65: [32m2026-02-25 16:13:07.197[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0065, MAE(e): 0.0046, MAE(f): 0.6513, MAE(s): 0.0000, Time: 1.93s, lr: 0.00010000
66: [0m
67: [32m2026-02-25 16:13:07.201[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 16:13:08.637[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0059, MAE(e): 0.0044, MAE(f): 0.5979, MAE(s): 0.0000, Time: 1.44s, lr: 0.00010000
69: [0m
70: [32m2026-02-25 16:13:10.454[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0061, MAE(e): 0.0043, MAE(f): 0.6157, MAE(s): 0.0000, Time: 1.81s, lr: 0.00010000
71: [0m
72: [32m2026-02-25 16:13:10.459[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 16:13:11.839[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0049, MAE(e): 0.0045, MAE(f): 0.4943, MAE(s): 0.0000, Time: 1.38s, lr: 0.00010000
74: [0m
75: [32m2026-02-25 16:13:13.661[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0053, MAE(e): 0.0038, MAE(f): 0.5308, MAE(s): 0.0000, Time: 1.82s, lr: 0.00010000
76: [0m
77: [32m2026-02-25 16:13:13.665[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 16:13:15.097[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0038, MAE(e): 0.0071, MAE(f): 0.3828, MAE(s): 0.0000, Time: 1.43s, lr: 0.00010000
79: [0m
80: [32m2026-02-25 16:13:16.982[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0041, MAE(e): 0.0045, MAE(f): 0.4159, MAE(s): 0.0000, Time: 1.88s, lr: 0.00010000
81: [0m
82: [32m2026-02-25 16:13:16.987[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 16:13:18.368[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0031, MAE(e): 0.0061, MAE(f): 0.3086, MAE(s): 0.0000, Time: 1.38s, lr: 0.00010000
84: [0m
85: [32m2026-02-25 16:13:20.129[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0033, MAE(e): 0.0053, MAE(f): 0.3370, MAE(s): 0.0000, Time: 1.76s, lr: 0.00010000
86: [0m
87: [32m2026-02-25 16:13:20.133[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 16:13:21.571[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0056, MAE(f): 0.2726, MAE(s): 0.0000, Time: 1.44s, lr: 0.00010000
89: [0m
90: [32m2026-02-25 16:13:23.314[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0029, MAE(e): 0.0055, MAE(f): 0.2892, MAE(s): 0.0000, Time: 1.74s, lr: 0.00010000
91: [0m
92: [32m2026-02-25 16:13:23.320[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 16:13:24.760[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0024, MAE(e): 0.0059, MAE(f): 0.2417, MAE(s): 0.0000, Time: 1.44s, lr: 0.00010000
94: [0m
95: [32m2026-02-25 16:13:26.470[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0025, MAE(e): 0.0045, MAE(f): 0.2583, MAE(s): 0.0000, Time: 1.71s, lr: 0.00010000
96: [0m
97: [32m2026-02-25 16:13:26.475[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 16:13:27.837[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0049, MAE(f): 0.2154, MAE(s): 0.0000, Time: 1.36s, lr: 0.00010000
99: [0m
100: [32m2026-02-25 16:13:29.583[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0023, MAE(e): 0.0039, MAE(f): 0.2336, MAE(s): 0.0000, Time: 1.74s, lr: 0.00010000
101: [0m
102: [32m2026-02-25 16:13:29.587[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 16:13:30.944[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0049, MAE(f): 0.1937, MAE(s): 0.0000, Time: 1.36s, lr: 0.00010000
104: [0m
105: [32m2026-02-25 16:13:32.887[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0021, MAE(e): 0.0035, MAE(f): 0.2119, MAE(s): 0.0000, Time: 1.94s, lr: 0.00010000
106: [0m
107: [32m2026-02-25 16:13:32.891[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 16:13:34.273[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0017, MAE(e): 0.0057, MAE(f): 0.1760, MAE(s): 0.0000, Time: 1.38s, lr: 0.00010000
109: [0m
110: [32m2026-02-25 16:13:35.912[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0019, MAE(e): 0.0035, MAE(f): 0.1935, MAE(s): 0.0000, Time: 1.64s, lr: 0.00010000
111: [0m
112: [32m2026-02-25 16:13:35.916[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 16:13:37.333[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0016, MAE(e): 0.0037, MAE(f): 0.1608, MAE(s): 0.0000, Time: 1.42s, lr: 0.00010000
114: [0m
115: [32m2026-02-25 16:13:38.971[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0017, MAE(e): 0.0033, MAE(f): 0.1779, MAE(s): 0.0000, Time: 1.64s, lr: 0.00010000
116: [0m
117: [32m2026-02-25 16:13:38.975[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 16:13:40.394[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0014, MAE(e): 0.0040, MAE(f): 0.1482, MAE(s): 0.0000, Time: 1.42s, lr: 0.00010000
119: [0m
120: [32m2026-02-25 16:13:42.184[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0016, MAE(e): 0.0031, MAE(f): 0.1643, MAE(s): 0.0000, Time: 1.79s, lr: 0.00010000
121: [0m
122: [32m2026-02-25 16:13:42.188[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 16:13:43.576[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0042, MAE(f): 0.1376, MAE(s): 0.0000, Time: 1.39s, lr: 0.00010000
124: [0m
125: [32m2026-02-25 16:13:45.229[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0029, MAE(f): 0.1526, MAE(s): 0.0000, Time: 1.65s, lr: 0.00010000
126: [0m
127: [32m2026-02-25 16:13:45.233[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 16:13:46.806[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0041, MAE(f): 0.1291, MAE(s): 0.0000, Time: 1.57s, lr: 0.00010000
129: [0m
130: [32m2026-02-25 16:13:48.672[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0026, MAE(f): 0.1424, MAE(s): 0.0000, Time: 1.86s, lr: 0.00010000
131: [0m
132: [32m2026-02-25 16:13:48.676[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 16:13:50.063[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0029, MAE(f): 0.1212, MAE(s): 0.0000, Time: 1.39s, lr: 0.00010000
134: [0m
135: [32m2026-02-25 16:13:52.009[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0025, MAE(f): 0.1335, MAE(s): 0.0000, Time: 1.94s, lr: 0.00010000
136: [0m
137: [32m2026-02-25 16:13:52.014[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 16:13:53.323[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0025, MAE(f): 0.1141, MAE(s): 0.0000, Time: 1.31s, lr: 0.00010000
139: [0m
140: [32m2026-02-25 16:13:54.968[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0023, MAE(f): 0.1259, MAE(s): 0.0000, Time: 1.64s, lr: 0.00010000
141: [0m
142: [32m2026-02-25 16:13:54.973[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 16:13:56.412[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0035, MAE(f): 0.1091, MAE(s): 0.0000, Time: 1.44s, lr: 0.00010000
144: [0m
145: [32m2026-02-25 16:13:58.135[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0021, MAE(f): 0.1193, MAE(s): 0.0000, Time: 1.72s, lr: 0.00010000
146: [0m
147: [32m2026-02-25 16:13:58.140[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 16:13:59.661[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0029, MAE(f): 0.1049, MAE(s): 0.0000, Time: 1.52s, lr: 0.00010000
149: [0m
150: [32m2026-02-25 16:14:01.469[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0020, MAE(f): 0.1140, MAE(s): 0.0000, Time: 1.81s, lr: 0.00010000
151: [0m
152: [32m2026-02-25 16:14:01.475[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 16:14:02.877[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0034, MAE(f): 0.1016, MAE(s): 0.0000, Time: 1.40s, lr: 0.00010000
154: [0m
155: [32m2026-02-25 16:14:04.637[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0019, MAE(f): 0.1096, MAE(s): 0.0000, Time: 1.76s, lr: 0.00010000
156: [0m
157: [32m2026-02-25 16:14:04.642[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 16:14:06.022[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0020, MAE(f): 0.0987, MAE(s): 0.0000, Time: 1.38s, lr: 0.00010000
159: [0m
160: [32m2026-02-25 16:14:07.785[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0019, MAE(f): 0.1060, MAE(s): 0.0000, Time: 1.76s, lr: 0.00010000
161: [0m
