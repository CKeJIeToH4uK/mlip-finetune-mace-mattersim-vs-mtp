# Log Snippet: repo/coursework/FLiNaK/scripts/logs/ms_flinak_split_3909462.out

Original size: 320196 bytes. Full raw log not copied.

1: [rank0]:[W422 18:42:01.677405770 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-04-22 18:42:02.869[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
25:          0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000])
26: [32m2026-04-22 18:42:10.970[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
27: [32m2026-04-22 18:42:11.450[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
28: [32m2026-04-22 18:42:13.616[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
29: [32m2026-04-22 18:42:13.616[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
30: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
31: grad.sizes() = [1, 128], strides() = [1, 1]
33:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
34: [32m2026-04-22 18:42:35.711[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0048, MAE(e): 0.0497, MAE(f): 0.4449, MAE(s): 0.0000, Time: 22.09s, lr: 0.00005000
35: [0m
36: [32m2026-04-22 18:42:36.310[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0050, MAE(e): 0.0553, MAE(f): 0.4526, MAE(s): 0.0000, Time: 0.59s, lr: 0.00005000
37: [0m
38: [32m2026-04-22 18:42:36.750[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
39: [32m2026-04-22 18:42:42.274[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0048, MAE(e): 0.0497, MAE(f): 0.4418, MAE(s): 0.0000, Time: 5.52s, lr: 0.00005000
40: [0m
41: [32m2026-04-22 18:42:42.607[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0050, MAE(e): 0.0550, MAE(f): 0.4509, MAE(s): 0.0000, Time: 0.33s, lr: 0.00005000
42: [0m
43: [32m2026-04-22 18:42:42.779[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
44: [32m2026-04-22 18:42:48.665[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0048, MAE(e): 0.0487, MAE(f): 0.4382, MAE(s): 0.0000, Time: 5.89s, lr: 0.00005000
45: [0m
46: [32m2026-04-22 18:42:48.972[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0049, MAE(e): 0.0541, MAE(f): 0.4471, MAE(s): 0.0000, Time: 0.30s, lr: 0.00005000
47: [0m
48: [32m2026-04-22 18:42:49.179[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
49: [32m2026-04-22 18:42:54.744[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0046, MAE(e): 0.0472, MAE(f): 0.4244, MAE(s): 0.0000, Time: 5.56s, lr: 0.00005000
50: [0m
51: [32m2026-04-22 18:42:55.010[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0047, MAE(e): 0.0499, MAE(f): 0.4318, MAE(s): 0.0000, Time: 0.26s, lr: 0.00005000
52: [0m
53: [32m2026-04-22 18:42:55.181[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
54: [32m2026-04-22 18:43:00.728[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0040, MAE(e): 0.0397, MAE(f): 0.3711, MAE(s): 0.0000, Time: 5.55s, lr: 0.00005000
55: [0m
56: [32m2026-04-22 18:43:01.056[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0041, MAE(e): 0.0395, MAE(f): 0.3835, MAE(s): 0.0000, Time: 0.32s, lr: 0.00005000
57: [0m
58: [32m2026-04-22 18:43:01.250[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
59: [32m2026-04-22 18:43:06.924[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0032, MAE(e): 0.0325, MAE(f): 0.3012, MAE(s): 0.0000, Time: 5.67s, lr: 0.00005000
60: [0m
61: [32m2026-04-22 18:43:07.199[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0033, MAE(e): 0.0281, MAE(f): 0.3137, MAE(s): 0.0000, Time: 0.27s, lr: 0.00005000
62: [0m
63: [32m2026-04-22 18:43:07.382[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
64: [32m2026-04-22 18:43:12.950[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0026, MAE(e): 0.0246, MAE(f): 0.2478, MAE(s): 0.0000, Time: 5.57s, lr: 0.00005000
65: [0m
66: [32m2026-04-22 18:43:13.226[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0027, MAE(e): 0.0203, MAE(f): 0.2635, MAE(s): 0.0000, Time: 0.27s, lr: 0.00005000
67: [0m
68: [32m2026-04-22 18:43:13.406[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
69: [32m2026-04-22 18:43:18.934[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0022, MAE(e): 0.0149, MAE(f): 0.2172, MAE(s): 0.0000, Time: 5.53s, lr: 0.00005000
70: [0m
71: [32m2026-04-22 18:43:19.206[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0024, MAE(e): 0.0148, MAE(f): 0.2320, MAE(s): 0.0000, Time: 0.27s, lr: 0.00005000
72: [0m
73: [32m2026-04-22 18:43:19.383[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
74: [32m2026-04-22 18:43:24.952[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0107, MAE(f): 0.1911, MAE(s): 0.0000, Time: 5.57s, lr: 0.00005000
75: [0m
76: [32m2026-04-22 18:43:25.266[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0021, MAE(e): 0.0113, MAE(f): 0.2081, MAE(s): 0.0000, Time: 0.31s, lr: 0.00005000
77: [0m
78: [32m2026-04-22 18:43:25.471[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
79: [32m2026-04-22 18:43:30.999[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0017, MAE(e): 0.0095, MAE(f): 0.1711, MAE(s): 0.0000, Time: 5.53s, lr: 0.00005000
80: [0m
81: [32m2026-04-22 18:43:31.278[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0019, MAE(e): 0.0097, MAE(f): 0.1889, MAE(s): 0.0000, Time: 0.28s, lr: 0.00005000
82: [0m
83: [32m2026-04-22 18:43:31.488[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
84: [32m2026-04-22 18:43:37.369[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0016, MAE(e): 0.0086, MAE(f): 0.1563, MAE(s): 0.0000, Time: 5.88s, lr: 0.00005000
85: [0m
86: [32m2026-04-22 18:43:37.727[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0017, MAE(e): 0.0093, MAE(f): 0.1734, MAE(s): 0.0000, Time: 0.35s, lr: 0.00005000
87: [0m
88: [32m2026-04-22 18:43:37.952[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
89: [32m2026-04-22 18:43:43.597[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0014, MAE(e): 0.0080, MAE(f): 0.1428, MAE(s): 0.0000, Time: 5.64s, lr: 0.00005000
90: [0m
91: [32m2026-04-22 18:43:43.879[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0016, MAE(e): 0.0091, MAE(f): 0.1605, MAE(s): 0.0000, Time: 0.28s, lr: 0.00005000
92: [0m
93: [32m2026-04-22 18:43:44.051[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
94: [32m2026-04-22 18:43:49.491[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0080, MAE(f): 0.1301, MAE(s): 0.0000, Time: 5.44s, lr: 0.00005000
95: [0m
96: [32m2026-04-22 18:43:49.787[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0089, MAE(f): 0.1490, MAE(s): 0.0000, Time: 0.29s, lr: 0.00005000
97: [0m
98: [32m2026-04-22 18:43:49.999[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
99: [32m2026-04-22 18:43:55.626[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0075, MAE(f): 0.1206, MAE(s): 0.0000, Time: 5.63s, lr: 0.00005000
100: [0m
101: [32m2026-04-22 18:43:55.904[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0084, MAE(f): 0.1390, MAE(s): 0.0000, Time: 0.27s, lr: 0.00005000
102: [0m
103: [32m2026-04-22 18:43:56.090[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
104: [32m2026-04-22 18:44:01.631[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0067, MAE(f): 0.1134, MAE(s): 0.0000, Time: 5.54s, lr: 0.00005000
105: [0m
106: [32m2026-04-22 18:44:01.908[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0080, MAE(f): 0.1300, MAE(s): 0.0000, Time: 0.27s, lr: 0.00005000
107: [0m
108: [32m2026-04-22 18:44:02.091[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
109: [32m2026-04-22 18:44:07.612[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0060, MAE(f): 0.1052, MAE(s): 0.0000, Time: 5.52s, lr: 0.00005000
110: [0m
111: [32m2026-04-22 18:44:07.918[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0075, MAE(f): 0.1223, MAE(s): 0.0000, Time: 0.30s, lr: 0.00005000
112: [0m
113: [32m2026-04-22 18:44:08.151[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
114: [32m2026-04-22 18:44:13.595[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0064, MAE(f): 0.0994, MAE(s): 0.0000, Time: 5.44s, lr: 0.00005000
115: [0m
116: [32m2026-04-22 18:44:13.865[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0070, MAE(f): 0.1154, MAE(s): 0.0000, Time: 0.27s, lr: 0.00005000
117: [0m
118: [32m2026-04-22 18:44:14.047[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
119: [32m2026-04-22 18:44:20.055[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0054, MAE(f): 0.0939, MAE(s): 0.0000, Time: 6.01s, lr: 0.00005000
120: [0m
121: [32m2026-04-22 18:44:20.352[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0065, MAE(f): 0.1095, MAE(s): 0.0000, Time: 0.29s, lr: 0.00005000
122: [0m
123: [32m2026-04-22 18:44:20.545[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
124: [32m2026-04-22 18:44:26.004[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0050, MAE(f): 0.0895, MAE(s): 0.0000, Time: 5.46s, lr: 0.00005000
125: [0m
126: [32m2026-04-22 18:44:26.276[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0061, MAE(f): 0.1044, MAE(s): 0.0000, Time: 0.27s, lr: 0.00005000
127: [0m
128: [32m2026-04-22 18:44:26.454[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
129: [32m2026-04-22 18:44:31.893[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0056, MAE(f): 0.0852, MAE(s): 0.0000, Time: 5.44s, lr: 0.00005000
130: [0m
131: [32m2026-04-22 18:44:32.207[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0058, MAE(f): 0.0997, MAE(s): 0.0000, Time: 0.31s, lr: 0.00005000
132: [0m
133: [32m2026-04-22 18:44:32.413[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
134: [32m2026-04-22 18:44:38.071[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0063, MAE(f): 0.0818, MAE(s): 0.0000, Time: 5.66s, lr: 0.00005000
135: [0m
136: [32m2026-04-22 18:44:38.378[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0055, MAE(f): 0.0956, MAE(s): 0.0000, Time: 0.30s, lr: 0.00005000
137: [0m
138: [32m2026-04-22 18:44:38.567[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
139: [32m2026-04-22 18:44:44.139[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0044, MAE(f): 0.0781, MAE(s): 0.0000, Time: 5.57s, lr: 0.00005000
140: [0m
141: [32m2026-04-22 18:44:44.424[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0052, MAE(f): 0.0918, MAE(s): 0.0000, Time: 0.28s, lr: 0.00005000
142: [0m
143: [32m2026-04-22 18:44:44.605[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
144: [32m2026-04-22 18:44:50.178[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0042, MAE(f): 0.0753, MAE(s): 0.0000, Time: 5.57s, lr: 0.00005000
145: [0m
146: [32m2026-04-22 18:44:50.462[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0049, MAE(f): 0.0884, MAE(s): 0.0000, Time: 0.28s, lr: 0.00005000
147: [0m
148: [32m2026-04-22 18:44:50.641[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
149: [32m2026-04-22 18:44:56.163[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0044, MAE(f): 0.0727, MAE(s): 0.0000, Time: 5.52s, lr: 0.00005000
150: [0m
151: [32m2026-04-22 18:44:56.437[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0047, MAE(f): 0.0853, MAE(s): 0.0000, Time: 0.27s, lr: 0.00005000
152: [0m
153: [32m2026-04-22 18:44:56.620[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
154: [32m2026-04-22 18:45:02.378[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0046, MAE(f): 0.0709, MAE(s): 0.0000, Time: 5.76s, lr: 0.00005000
155: [0m
156: [32m2026-04-22 18:45:02.704[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0045, MAE(f): 0.0825, MAE(s): 0.0000, Time: 0.32s, lr: 0.00005000
157: [0m
