# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr5e-5_bs16/train.log

Original size: 320370 bytes. Full raw log not copied.

1: [rank0]:[W225 16:41:26.196017851 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 16:41:27.102[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 16:41:29.567[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 16:41:34.242[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 16:41:34.516[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 16:41:34.516[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 16:41:45.414[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0089, MAE(f): 0.6840, MAE(s): 0.0000, Time: 10.90s, lr: 0.00005000
39: [0m
40: [32m2026-02-25 16:41:51.978[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6899, MAE(s): 0.0000, Time: 6.56s, lr: 0.00005000
41: [0m
42: [32m2026-02-25 16:41:51.985[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 16:41:56.963[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6704, MAE(s): 0.0000, Time: 4.98s, lr: 0.00005000
44: [0m
45: [32m2026-02-25 16:42:04.092[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0046, MAE(f): 0.6744, MAE(s): 0.0000, Time: 7.12s, lr: 0.00005000
46: [0m
47: [32m2026-02-25 16:42:04.098[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 16:42:09.605[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0062, MAE(e): 0.0046, MAE(f): 0.6270, MAE(s): 0.0000, Time: 5.51s, lr: 0.00005000
49: [0m
50: [32m2026-02-25 16:42:18.473[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0062, MAE(e): 0.0042, MAE(f): 0.6200, MAE(s): 0.0000, Time: 8.86s, lr: 0.00005000
51: [0m
52: [32m2026-02-25 16:42:18.482[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 16:42:23.876[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0043, MAE(e): 0.0046, MAE(f): 0.4297, MAE(s): 0.0000, Time: 5.39s, lr: 0.00005000
54: [0m
55: [32m2026-02-25 16:42:29.310[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0039, MAE(e): 0.0054, MAE(f): 0.3970, MAE(s): 0.0000, Time: 5.43s, lr: 0.00005000
56: [0m
57: [32m2026-02-25 16:42:29.315[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 16:42:34.390[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0054, MAE(f): 0.2684, MAE(s): 0.0000, Time: 5.07s, lr: 0.00005000
59: [0m
60: [32m2026-02-25 16:42:39.861[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0026, MAE(e): 0.0042, MAE(f): 0.2670, MAE(s): 0.0000, Time: 5.47s, lr: 0.00005000
61: [0m
62: [32m2026-02-25 16:42:39.867[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 16:42:44.202[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0021, MAE(e): 0.0060, MAE(f): 0.2122, MAE(s): 0.0000, Time: 4.33s, lr: 0.00005000
64: [0m
65: [32m2026-02-25 16:42:49.478[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0021, MAE(e): 0.0035, MAE(f): 0.2168, MAE(s): 0.0000, Time: 5.27s, lr: 0.00005000
66: [0m
67: [32m2026-02-25 16:42:49.483[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 16:42:54.639[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0018, MAE(e): 0.0064, MAE(f): 0.1787, MAE(s): 0.0000, Time: 5.16s, lr: 0.00005000
69: [0m
70: [32m2026-02-25 16:42:59.811[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0018, MAE(e): 0.0032, MAE(f): 0.1848, MAE(s): 0.0000, Time: 5.17s, lr: 0.00005000
71: [0m
72: [32m2026-02-25 16:42:59.816[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 16:43:04.807[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0031, MAE(f): 0.1558, MAE(s): 0.0000, Time: 4.99s, lr: 0.00005000
74: [0m
75: [32m2026-02-25 16:43:11.297[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0016, MAE(e): 0.0029, MAE(f): 0.1623, MAE(s): 0.0000, Time: 6.49s, lr: 0.00005000
76: [0m
77: [32m2026-02-25 16:43:11.304[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 16:43:16.481[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0038, MAE(f): 0.1383, MAE(s): 0.0000, Time: 5.18s, lr: 0.00005000
79: [0m
80: [32m2026-02-25 16:43:22.368[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0025, MAE(f): 0.1449, MAE(s): 0.0000, Time: 5.88s, lr: 0.00005000
81: [0m
82: [32m2026-02-25 16:43:22.374[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 16:43:27.126[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0030, MAE(f): 0.1240, MAE(s): 0.0000, Time: 4.75s, lr: 0.00005000
84: [0m
85: [32m2026-02-25 16:43:32.321[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0023, MAE(f): 0.1309, MAE(s): 0.0000, Time: 5.19s, lr: 0.00005000
86: [0m
87: [32m2026-02-25 16:43:32.326[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 16:43:37.517[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0033, MAE(f): 0.1131, MAE(s): 0.0000, Time: 5.19s, lr: 0.00005000
89: [0m
90: [32m2026-02-25 16:43:42.745[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0021, MAE(f): 0.1194, MAE(s): 0.0000, Time: 5.22s, lr: 0.00005000
91: [0m
92: [32m2026-02-25 16:43:42.750[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 16:43:47.502[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0030, MAE(f): 0.1054, MAE(s): 0.0000, Time: 4.75s, lr: 0.00005000
94: [0m
95: [32m2026-02-25 16:43:53.529[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0019, MAE(f): 0.1108, MAE(s): 0.0000, Time: 6.02s, lr: 0.00005000
96: [0m
97: [32m2026-02-25 16:43:53.534[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 16:43:58.312[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0031, MAE(f): 0.1002, MAE(s): 0.0000, Time: 4.78s, lr: 0.00005000
99: [0m
100: [32m2026-02-25 16:44:04.477[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0018, MAE(f): 0.1045, MAE(s): 0.0000, Time: 6.16s, lr: 0.00005000
101: [0m
102: [32m2026-02-25 16:44:04.482[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 16:44:09.429[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0035, MAE(f): 0.0955, MAE(s): 0.0000, Time: 4.95s, lr: 0.00005000
104: [0m
105: [32m2026-02-25 16:44:15.836[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0017, MAE(f): 0.0999, MAE(s): 0.0000, Time: 6.40s, lr: 0.00005000
106: [0m
107: [32m2026-02-25 16:44:15.840[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 16:44:20.699[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0025, MAE(f): 0.0930, MAE(s): 0.0000, Time: 4.86s, lr: 0.00005000
109: [0m
110: [32m2026-02-25 16:44:25.990[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0016, MAE(f): 0.0962, MAE(s): 0.0000, Time: 5.29s, lr: 0.00005000
111: [0m
112: [32m2026-02-25 16:44:25.995[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 16:44:30.805[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0018, MAE(f): 0.0891, MAE(s): 0.0000, Time: 4.81s, lr: 0.00005000
114: [0m
115: [32m2026-02-25 16:44:38.275[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0016, MAE(f): 0.0930, MAE(s): 0.0000, Time: 7.47s, lr: 0.00005000
116: [0m
117: [32m2026-02-25 16:44:38.280[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 16:44:43.071[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0022, MAE(f): 0.0861, MAE(s): 0.0000, Time: 4.79s, lr: 0.00005000
119: [0m
120: [32m2026-02-25 16:44:49.466[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0015, MAE(f): 0.0902, MAE(s): 0.0000, Time: 6.39s, lr: 0.00005000
121: [0m
122: [32m2026-02-25 16:44:49.470[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 16:44:54.389[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0024, MAE(f): 0.0840, MAE(s): 0.0000, Time: 4.92s, lr: 0.00005000
124: [0m
125: [32m2026-02-25 16:44:59.532[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0015, MAE(f): 0.0876, MAE(s): 0.0000, Time: 5.14s, lr: 0.00005000
126: [0m
127: [32m2026-02-25 16:44:59.538[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 16:45:04.337[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0023, MAE(f): 0.0816, MAE(s): 0.0000, Time: 4.80s, lr: 0.00005000
129: [0m
130: [32m2026-02-25 16:45:09.346[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0015, MAE(f): 0.0854, MAE(s): 0.0000, Time: 5.00s, lr: 0.00005000
131: [0m
132: [32m2026-02-25 16:45:09.350[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 16:45:13.947[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0028, MAE(f): 0.0797, MAE(s): 0.0000, Time: 4.60s, lr: 0.00005000
134: [0m
135: [32m2026-02-25 16:45:19.227[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0014, MAE(f): 0.0833, MAE(s): 0.0000, Time: 5.28s, lr: 0.00005000
136: [0m
137: [32m2026-02-25 16:45:19.234[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 16:45:23.977[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0026, MAE(f): 0.0776, MAE(s): 0.0000, Time: 4.74s, lr: 0.00005000
139: [0m
140: [32m2026-02-25 16:45:29.025[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0014, MAE(f): 0.0813, MAE(s): 0.0000, Time: 5.05s, lr: 0.00005000
141: [0m
142: [32m2026-02-25 16:45:29.030[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 16:45:33.690[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0027, MAE(f): 0.0763, MAE(s): 0.0000, Time: 4.66s, lr: 0.00005000
144: [0m
145: [32m2026-02-25 16:45:38.863[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0014, MAE(f): 0.0796, MAE(s): 0.0000, Time: 5.17s, lr: 0.00005000
146: [0m
147: [32m2026-02-25 16:45:38.868[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 16:45:43.547[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0020, MAE(f): 0.0747, MAE(s): 0.0000, Time: 4.68s, lr: 0.00005000
149: [0m
150: [32m2026-02-25 16:45:48.856[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0779, MAE(s): 0.0000, Time: 5.30s, lr: 0.00005000
151: [0m
152: [32m2026-02-25 16:45:48.861[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 16:45:53.862[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0022, MAE(f): 0.0728, MAE(s): 0.0000, Time: 5.00s, lr: 0.00005000
154: [0m
155: [32m2026-02-25 16:45:59.647[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0764, MAE(s): 0.0000, Time: 5.78s, lr: 0.00005000
156: [0m
157: [32m2026-02-25 16:45:59.652[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 16:46:04.527[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0016, MAE(f): 0.0716, MAE(s): 0.0000, Time: 4.87s, lr: 0.00005000
159: [0m
160: [32m2026-02-25 16:46:09.713[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0751, MAE(s): 0.0000, Time: 5.18s, lr: 0.00005000
161: [0m
