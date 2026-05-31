# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr1e-4_bs16/train.log

Original size: 320370 bytes. Full raw log not copied.

1: [rank0]:[W225 15:55:28.629542216 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 15:55:29.911[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 15:55:34.506[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 15:55:38.507[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 15:55:39.789[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 15:55:39.789[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 15:55:58.388[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0074, MAE(f): 0.6797, MAE(s): 0.0000, Time: 18.60s, lr: 0.00010000
39: [0m
40: [32m2026-02-25 15:56:03.704[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6792, MAE(s): 0.0000, Time: 5.31s, lr: 0.00010000
41: [0m
42: [32m2026-02-25 15:56:03.708[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 15:56:07.721[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0061, MAE(e): 0.0045, MAE(f): 0.6103, MAE(s): 0.0000, Time: 4.01s, lr: 0.00010000
44: [0m
45: [32m2026-02-25 15:56:12.433[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0056, MAE(e): 0.0039, MAE(f): 0.5618, MAE(s): 0.0000, Time: 4.71s, lr: 0.00010000
46: [0m
47: [32m2026-02-25 15:56:12.438[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 15:56:16.480[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0032, MAE(e): 0.0079, MAE(f): 0.3251, MAE(s): 0.0000, Time: 4.04s, lr: 0.00010000
49: [0m
50: [32m2026-02-25 15:56:21.252[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0027, MAE(e): 0.0050, MAE(f): 0.2759, MAE(s): 0.0000, Time: 4.77s, lr: 0.00010000
51: [0m
52: [32m2026-02-25 15:56:21.255[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 15:56:25.180[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0077, MAE(f): 0.2118, MAE(s): 0.0000, Time: 3.92s, lr: 0.00010000
54: [0m
55: [32m2026-02-25 15:56:30.204[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0020, MAE(e): 0.0035, MAE(f): 0.2020, MAE(s): 0.0000, Time: 5.02s, lr: 0.00010000
56: [0m
57: [32m2026-02-25 15:56:30.209[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 15:56:34.240[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0016, MAE(e): 0.0041, MAE(f): 0.1596, MAE(s): 0.0000, Time: 4.03s, lr: 0.00010000
59: [0m
60: [32m2026-02-25 15:56:39.225[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0031, MAE(f): 0.1580, MAE(s): 0.0000, Time: 4.98s, lr: 0.00010000
61: [0m
62: [32m2026-02-25 15:56:39.231[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 15:56:43.401[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0040, MAE(f): 0.1286, MAE(s): 0.0000, Time: 4.17s, lr: 0.00010000
64: [0m
65: [32m2026-02-25 15:56:48.290[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0026, MAE(f): 0.1289, MAE(s): 0.0000, Time: 4.89s, lr: 0.00010000
66: [0m
67: [32m2026-02-25 15:56:48.297[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 15:56:52.569[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0077, MAE(f): 0.1093, MAE(s): 0.0000, Time: 4.27s, lr: 0.00010000
69: [0m
70: [32m2026-02-25 15:56:57.226[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0021, MAE(f): 0.1109, MAE(s): 0.0000, Time: 4.65s, lr: 0.00010000
71: [0m
72: [32m2026-02-25 15:56:57.230[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 15:57:01.352[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0029, MAE(f): 0.0995, MAE(s): 0.0000, Time: 4.12s, lr: 0.00010000
74: [0m
75: [32m2026-02-25 15:57:05.950[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0019, MAE(f): 0.1011, MAE(s): 0.0000, Time: 4.60s, lr: 0.00010000
76: [0m
77: [32m2026-02-25 15:57:05.954[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 15:57:09.815[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0019, MAE(f): 0.0928, MAE(s): 0.0000, Time: 3.86s, lr: 0.00010000
79: [0m
80: [32m2026-02-25 15:57:14.562[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0017, MAE(f): 0.0945, MAE(s): 0.0000, Time: 4.75s, lr: 0.00010000
81: [0m
82: [32m2026-02-25 15:57:14.569[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 15:57:18.527[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0023, MAE(f): 0.0882, MAE(s): 0.0000, Time: 3.96s, lr: 0.00010000
84: [0m
85: [32m2026-02-25 15:57:23.310[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0016, MAE(f): 0.0892, MAE(s): 0.0000, Time: 4.78s, lr: 0.00010000
86: [0m
87: [32m2026-02-25 15:57:23.314[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 15:57:27.233[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0023, MAE(f): 0.0833, MAE(s): 0.0000, Time: 3.92s, lr: 0.00010000
89: [0m
90: [32m2026-02-25 15:57:31.886[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0015, MAE(f): 0.0850, MAE(s): 0.0000, Time: 4.65s, lr: 0.00010000
91: [0m
92: [32m2026-02-25 15:57:31.891[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 15:57:35.722[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0028, MAE(f): 0.0791, MAE(s): 0.0000, Time: 3.83s, lr: 0.00010000
94: [0m
95: [32m2026-02-25 15:57:40.326[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0014, MAE(f): 0.0813, MAE(s): 0.0000, Time: 4.60s, lr: 0.00010000
96: [0m
97: [32m2026-02-25 15:57:40.330[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 15:57:44.287[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0026, MAE(f): 0.0762, MAE(s): 0.0000, Time: 3.96s, lr: 0.00010000
99: [0m
100: [32m2026-02-25 15:57:49.149[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0014, MAE(f): 0.0783, MAE(s): 0.0000, Time: 4.86s, lr: 0.00010000
101: [0m
102: [32m2026-02-25 15:57:49.153[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 15:57:53.256[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0032, MAE(f): 0.0733, MAE(s): 0.0000, Time: 4.10s, lr: 0.00010000
104: [0m
105: [32m2026-02-25 15:57:58.033[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0757, MAE(s): 0.0000, Time: 4.77s, lr: 0.00010000
106: [0m
107: [32m2026-02-25 15:57:58.037[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 15:58:02.009[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0022, MAE(f): 0.0714, MAE(s): 0.0000, Time: 3.97s, lr: 0.00010000
109: [0m
110: [32m2026-02-25 15:58:06.732[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0012, MAE(f): 0.0733, MAE(s): 0.0000, Time: 4.72s, lr: 0.00010000
111: [0m
112: [32m2026-02-25 15:58:06.735[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 15:58:10.878[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0021, MAE(f): 0.0693, MAE(s): 0.0000, Time: 4.14s, lr: 0.00010000
114: [0m
115: [32m2026-02-25 15:58:15.555[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0012, MAE(f): 0.0713, MAE(s): 0.0000, Time: 4.67s, lr: 0.00010000
116: [0m
117: [32m2026-02-25 15:58:15.558[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 15:58:19.419[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0025, MAE(f): 0.0674, MAE(s): 0.0000, Time: 3.86s, lr: 0.00010000
119: [0m
120: [32m2026-02-25 15:58:24.058[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0011, MAE(f): 0.0695, MAE(s): 0.0000, Time: 4.64s, lr: 0.00010000
121: [0m
122: [32m2026-02-25 15:58:24.063[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 15:58:27.992[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0027, MAE(f): 0.0651, MAE(s): 0.0000, Time: 3.93s, lr: 0.00010000
124: [0m
125: [32m2026-02-25 15:58:32.719[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0011, MAE(f): 0.0678, MAE(s): 0.0000, Time: 4.72s, lr: 0.00010000
126: [0m
127: [32m2026-02-25 15:58:32.723[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 15:58:36.658[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0032, MAE(f): 0.0637, MAE(s): 0.0000, Time: 3.93s, lr: 0.00010000
129: [0m
130: [32m2026-02-25 15:58:41.354[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0011, MAE(f): 0.0663, MAE(s): 0.0000, Time: 4.69s, lr: 0.00010000
131: [0m
132: [32m2026-02-25 15:58:41.358[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 15:58:45.196[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0019, MAE(f): 0.0627, MAE(s): 0.0000, Time: 3.84s, lr: 0.00010000
134: [0m
135: [32m2026-02-25 15:58:49.630[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0650, MAE(s): 0.0000, Time: 4.43s, lr: 0.00010000
136: [0m
137: [32m2026-02-25 15:58:49.634[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 15:58:53.564[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0024, MAE(f): 0.0622, MAE(s): 0.0000, Time: 3.93s, lr: 0.00010000
139: [0m
140: [32m2026-02-25 15:58:58.270[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0637, MAE(s): 0.0000, Time: 4.70s, lr: 0.00010000
141: [0m
142: [32m2026-02-25 15:58:58.273[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 15:59:02.215[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0035, MAE(f): 0.0607, MAE(s): 0.0000, Time: 3.94s, lr: 0.00010000
144: [0m
145: [32m2026-02-25 15:59:06.767[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0626, MAE(s): 0.0000, Time: 4.55s, lr: 0.00010000
146: [0m
147: [32m2026-02-25 15:59:06.770[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 15:59:10.678[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0021, MAE(f): 0.0596, MAE(s): 0.0000, Time: 3.91s, lr: 0.00010000
149: [0m
150: [32m2026-02-25 15:59:15.384[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0615, MAE(s): 0.0000, Time: 4.70s, lr: 0.00010000
151: [0m
152: [32m2026-02-25 15:59:15.387[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 15:59:19.201[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0005, MAE(e): 0.0031, MAE(f): 0.0589, MAE(s): 0.0000, Time: 3.81s, lr: 0.00010000
154: [0m
155: [32m2026-02-25 15:59:23.655[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0605, MAE(s): 0.0000, Time: 4.45s, lr: 0.00010000
156: [0m
157: [32m2026-02-25 15:59:23.658[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 15:59:27.456[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0005, MAE(e): 0.0017, MAE(f): 0.0585, MAE(s): 0.0000, Time: 3.80s, lr: 0.00010000
159: [0m
160: [32m2026-02-25 15:59:31.959[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0005, MAE(e): 0.0010, MAE(f): 0.0596, MAE(s): 0.0000, Time: 4.50s, lr: 0.00010000
161: [0m
