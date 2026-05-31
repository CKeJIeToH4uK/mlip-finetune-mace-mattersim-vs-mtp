# Log Snippet: repo/coursework/mattersim_finetune/norm_nenorm/not_norm/train.log

Original size: 318570 bytes. Full raw log not copied.

1: [rank0]:[W225 22:20:28.523992060 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 22:20:29.457[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
3: [32m2026-02-25 22:20:31.554[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
4: [32m2026-02-25 22:20:35.565[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
5: [32m2026-02-25 22:20:36.085[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
6: [32m2026-02-25 22:20:36.086[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
7: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
8: grad.sizes() = [1, 128], strides() = [1, 1]
10:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
11: [32m2026-02-25 22:20:43.364[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 6.4752, MAE(e): 647.3500, MAE(f): 0.1766, MAE(s): 0.0000, Time: 7.28s, lr: 0.00005000
12: [0m
13: [32m2026-02-25 22:20:47.574[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.4720, MAE(e): 647.0540, MAE(f): 0.1509, MAE(s): 0.0000, Time: 4.20s, lr: 0.00005000
14: [0m
15: [32m2026-02-25 22:20:47.829[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
16: [32m2026-02-25 22:20:51.065[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 6.4675, MAE(e): 646.6082, MAE(f): 0.1544, MAE(s): 0.0000, Time: 3.24s, lr: 0.00005000
17: [0m
18: [32m2026-02-25 22:20:55.109[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.4649, MAE(e): 646.3429, MAE(f): 0.1620, MAE(s): 0.0000, Time: 4.04s, lr: 0.00005000
19: [0m
20: [32m2026-02-25 22:20:55.337[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
21: [32m2026-02-25 22:20:58.561[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 6.4589, MAE(e): 645.7142, MAE(f): 0.1845, MAE(s): 0.0000, Time: 3.22s, lr: 0.00005000
22: [0m
23: [32m2026-02-25 22:21:02.493[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.4567, MAE(e): 645.4891, MAE(f): 0.1939, MAE(s): 0.0000, Time: 3.93s, lr: 0.00005000
24: [0m
25: [32m2026-02-25 22:21:02.656[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
26: [32m2026-02-25 22:21:05.303[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 6.4474, MAE(e): 644.5028, MAE(f): 0.2459, MAE(s): 0.0000, Time: 2.65s, lr: 0.00005000
27: [0m
28: [32m2026-02-25 22:21:09.495[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.4457, MAE(e): 644.3250, MAE(f): 0.2567, MAE(s): 0.0000, Time: 4.19s, lr: 0.00005000
29: [0m
30: [32m2026-02-25 22:21:09.653[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
31: [32m2026-02-25 22:21:11.848[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 6.4292, MAE(e): 642.5509, MAE(f): 0.3742, MAE(s): 0.0000, Time: 2.19s, lr: 0.00005000
32: [0m
33: [32m2026-02-25 22:21:16.284[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.4287, MAE(e): 642.4996, MAE(f): 0.3817, MAE(s): 0.0000, Time: 4.43s, lr: 0.00005000
34: [0m
35: [32m2026-02-25 22:21:16.481[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
36: [32m2026-02-25 22:21:19.670[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 6.3954, MAE(e): 638.8268, MAE(f): 0.7245, MAE(s): 0.0000, Time: 3.19s, lr: 0.00005000
37: [0m
38: [32m2026-02-25 22:21:24.969[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.3989, MAE(e): 639.2157, MAE(f): 0.6886, MAE(s): 0.0000, Time: 5.30s, lr: 0.00005000
39: [0m
40: [32m2026-02-25 22:21:25.193[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
41: [32m2026-02-25 22:21:28.400[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 6.3264, MAE(e): 631.1080, MAE(f): 1.5430, MAE(s): 0.0000, Time: 3.21s, lr: 0.00005000
42: [0m
43: [32m2026-02-25 22:21:32.602[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.3425, MAE(e): 632.9119, MAE(f): 1.3447, MAE(s): 0.0000, Time: 4.20s, lr: 0.00005000
44: [0m
45: [32m2026-02-25 22:21:32.819[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
46: [32m2026-02-25 22:21:35.480[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 6.1735, MAE(e): 613.2274, MAE(f): 4.1324, MAE(s): 0.0000, Time: 2.66s, lr: 0.00005000
47: [0m
48: [32m2026-02-25 22:21:40.056[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.2302, MAE(e): 620.1345, MAE(f): 2.8952, MAE(s): 0.0000, Time: 4.57s, lr: 0.00005000
49: [0m
50: [32m2026-02-25 22:21:40.278[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
51: [32m2026-02-25 22:21:43.447[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 5.8350, MAE(e): 572.3948, MAE(f): 11.1171, MAE(s): 0.0000, Time: 3.17s, lr: 0.00005000
52: [0m
53: [32m2026-02-25 22:21:48.510[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 6.0044, MAE(e): 593.5016, MAE(f): 6.9503, MAE(s): 0.0000, Time: 5.06s, lr: 0.00005000
54: [0m
55: [32m2026-02-25 22:21:48.670[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
56: [32m2026-02-25 22:21:51.598[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 5.1299, MAE(e): 488.8420, MAE(f): 24.1534, MAE(s): 0.0000, Time: 2.93s, lr: 0.00005000
57: [0m
58: [32m2026-02-25 22:21:55.906[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 5.5552, MAE(e): 539.5095, MAE(f): 16.0191, MAE(s): 0.0000, Time: 4.30s, lr: 0.00005000
59: [0m
60: [32m2026-02-25 22:21:56.098[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
61: [32m2026-02-25 22:21:58.993[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 3.9293, MAE(e): 351.5069, MAE(f): 41.4288, MAE(s): 0.0000, Time: 2.89s, lr: 0.00005000
62: [0m
63: [32m2026-02-25 22:22:02.277[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 4.7340, MAE(e): 442.1816, MAE(f): 31.2309, MAE(s): 0.0000, Time: 3.28s, lr: 0.00005000
64: [0m
65: [32m2026-02-25 22:22:02.443[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
66: [32m2026-02-25 22:22:04.890[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 2.1865, MAE(e): 152.8182, MAE(f): 65.8383, MAE(s): 0.0000, Time: 2.45s, lr: 0.00005000
67: [0m
68: [32m2026-02-25 22:22:08.551[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 3.4929, MAE(e): 301.1219, MAE(f): 48.1732, MAE(s): 0.0000, Time: 3.66s, lr: 0.00005000
69: [0m
70: [32m2026-02-25 22:22:08.718[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
71: [32m2026-02-25 22:22:11.543[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.9728, MAE(e): 18.1271, MAE(f): 79.1650, MAE(s): 0.0000, Time: 2.82s, lr: 0.00005000
72: [0m
73: [32m2026-02-25 22:22:15.843[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 2.2238, MAE(e): 163.4400, MAE(f): 58.9505, MAE(s): 0.0000, Time: 4.30s, lr: 0.00005000
74: [0m
75: [32m2026-02-25 22:22:16.055[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
76: [32m2026-02-25 22:22:19.226[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.6692, MAE(e): 6.4396, MAE(f): 60.4867, MAE(s): 0.0000, Time: 3.17s, lr: 0.00005000
77: [0m
78: [32m2026-02-25 22:22:22.560[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 1.4607, MAE(e): 89.7942, MAE(f): 56.2846, MAE(s): 0.0000, Time: 3.33s, lr: 0.00005000
79: [0m
80: [32m2026-02-25 22:22:22.728[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
81: [32m2026-02-25 22:22:25.386[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.5397, MAE(e): 5.2673, MAE(f): 48.7102, MAE(s): 0.0000, Time: 2.66s, lr: 0.00005000
82: [0m
83: [32m2026-02-25 22:22:29.718[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 1.0131, MAE(e): 50.5730, MAE(f): 50.7482, MAE(s): 0.0000, Time: 4.33s, lr: 0.00005000
84: [0m
85: [32m2026-02-25 22:22:29.881[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
86: [32m2026-02-25 22:22:32.273[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.4634, MAE(e): 4.7749, MAE(f): 41.5794, MAE(s): 0.0000, Time: 2.39s, lr: 0.00005000
87: [0m
88: [32m2026-02-25 22:22:37.250[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.7487, MAE(e): 29.2580, MAE(f): 45.6174, MAE(s): 0.0000, Time: 4.97s, lr: 0.00005000
89: [0m
90: [32m2026-02-25 22:22:37.479[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
91: [32m2026-02-25 22:22:40.153[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.3963, MAE(e): 3.4351, MAE(f): 36.2044, MAE(s): 0.0000, Time: 2.67s, lr: 0.00005000
92: [0m
93: [32m2026-02-25 22:22:44.052[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.5804, MAE(e): 17.1560, MAE(f): 40.8902, MAE(s): 0.0000, Time: 3.89s, lr: 0.00005000
94: [0m
95: [32m2026-02-25 22:22:44.224[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
96: [32m2026-02-25 22:22:46.575[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.3500, MAE(e): 2.7583, MAE(f): 32.2521, MAE(s): 0.0000, Time: 2.35s, lr: 0.00005000
97: [0m
98: [32m2026-02-25 22:22:49.425[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.4734, MAE(e): 10.4353, MAE(f): 36.9121, MAE(s): 0.0000, Time: 2.85s, lr: 0.00005000
99: [0m
100: [32m2026-02-25 22:22:49.582[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
101: [32m2026-02-25 22:22:52.186[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.3216, MAE(e): 2.7164, MAE(f): 29.4551, MAE(s): 0.0000, Time: 2.60s, lr: 0.00005000
102: [0m
103: [32m2026-02-25 22:22:55.044[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.4044, MAE(e): 6.7178, MAE(f): 33.7321, MAE(s): 0.0000, Time: 2.85s, lr: 0.00005000
104: [0m
105: [32m2026-02-25 22:22:55.205[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
106: [32m2026-02-25 22:22:57.246[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.3018, MAE(e): 2.7015, MAE(f): 27.4872, MAE(s): 0.0000, Time: 2.04s, lr: 0.00005000
107: [0m
108: [32m2026-02-25 22:23:00.039[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.3576, MAE(e): 4.4402, MAE(f): 31.3265, MAE(s): 0.0000, Time: 2.79s, lr: 0.00005000
109: [0m
110: [32m2026-02-25 22:23:00.204[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
111: [32m2026-02-25 22:23:02.784[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.2818, MAE(e): 2.1152, MAE(f): 26.0702, MAE(s): 0.0000, Time: 2.58s, lr: 0.00005000
112: [0m
113: [32m2026-02-25 22:23:07.677[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.3264, MAE(e): 3.1689, MAE(f): 29.4847, MAE(s): 0.0000, Time: 4.89s, lr: 0.00005000
114: [0m
115: [32m2026-02-25 22:23:07.832[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
116: [32m2026-02-25 22:23:10.840[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.2642, MAE(e): 1.6650, MAE(f): 24.7666, MAE(s): 0.0000, Time: 3.01s, lr: 0.00005000
117: [0m
118: [32m2026-02-25 22:23:15.153[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.3024, MAE(e): 2.3148, MAE(f): 27.9324, MAE(s): 0.0000, Time: 4.31s, lr: 0.00005000
119: [0m
120: [32m2026-02-25 22:23:15.374[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
121: [32m2026-02-25 22:23:18.345[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.2495, MAE(e): 1.6153, MAE(f): 23.3405, MAE(s): 0.0000, Time: 2.97s, lr: 0.00005000
122: [0m
123: [32m2026-02-25 22:23:22.631[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.2831, MAE(e): 1.8805, MAE(f): 26.4416, MAE(s): 0.0000, Time: 4.28s, lr: 0.00005000
124: [0m
125: [32m2026-02-25 22:23:22.801[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
126: [32m2026-02-25 22:23:25.949[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.2351, MAE(e): 1.2159, MAE(f): 22.3054, MAE(s): 0.0000, Time: 3.15s, lr: 0.00005000
127: [0m
128: [32m2026-02-25 22:23:30.781[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.2658, MAE(e): 1.5028, MAE(f): 25.0830, MAE(s): 0.0000, Time: 4.83s, lr: 0.00005000
129: [0m
130: [32m2026-02-25 22:23:30.943[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
131: [32m2026-02-25 22:23:33.445[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.2329, MAE(e): 1.4404, MAE(f): 21.8577, MAE(s): 0.0000, Time: 2.50s, lr: 0.00005000
132: [0m
133: [32m2026-02-25 22:23:36.137[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.2527, MAE(e): 1.3209, MAE(f): 23.9559, MAE(s): 0.0000, Time: 2.69s, lr: 0.00005000
134: [0m
