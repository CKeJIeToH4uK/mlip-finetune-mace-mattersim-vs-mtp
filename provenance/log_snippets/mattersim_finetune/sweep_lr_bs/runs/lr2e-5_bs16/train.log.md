# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr2e-5_bs16/train.log

Original size: 320454 bytes. Full raw log not copied.

1: [rank0]:[W225 17:47:28.683954088 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 17:47:29.348[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 17:47:32.454[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 17:47:37.785[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 17:47:38.498[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 17:47:38.498[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 17:47:51.139[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0148, MAE(f): 0.6851, MAE(s): 0.0000, Time: 12.64s, lr: 0.00002000
39: [0m
40: [32m2026-02-25 17:48:01.446[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0075, MAE(f): 0.6938, MAE(s): 0.0000, Time: 10.30s, lr: 0.00002000
41: [0m
42: [32m2026-02-25 17:48:01.453[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 17:48:07.555[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6821, MAE(s): 0.0000, Time: 6.10s, lr: 0.00002000
44: [0m
45: [32m2026-02-25 17:48:14.871[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0047, MAE(f): 0.6911, MAE(s): 0.0000, Time: 7.31s, lr: 0.00002000
46: [0m
47: [32m2026-02-25 17:48:14.877[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 17:48:20.437[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6778, MAE(s): 0.0000, Time: 5.56s, lr: 0.00002000
49: [0m
50: [32m2026-02-25 17:48:30.775[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6860, MAE(s): 0.0000, Time: 10.33s, lr: 0.00002000
51: [0m
52: [32m2026-02-25 17:48:30.783[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 17:48:36.708[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6708, MAE(s): 0.0000, Time: 5.92s, lr: 0.00002000
54: [0m
55: [32m2026-02-25 17:48:44.217[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6786, MAE(s): 0.0000, Time: 7.51s, lr: 0.00002000
56: [0m
57: [32m2026-02-25 17:48:44.228[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 17:48:49.987[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0047, MAE(f): 0.6564, MAE(s): 0.0000, Time: 5.76s, lr: 0.00002000
59: [0m
60: [32m2026-02-25 17:48:57.460[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6659, MAE(s): 0.0000, Time: 7.47s, lr: 0.00002000
61: [0m
62: [32m2026-02-25 17:48:57.468[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 17:49:03.102[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0062, MAE(e): 0.0045, MAE(f): 0.6265, MAE(s): 0.0000, Time: 5.63s, lr: 0.00002000
64: [0m
65: [32m2026-02-25 17:49:13.523[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0064, MAE(e): 0.0044, MAE(f): 0.6396, MAE(s): 0.0000, Time: 10.42s, lr: 0.00002000
66: [0m
67: [32m2026-02-25 17:49:13.529[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 17:49:19.264[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0053, MAE(e): 0.0042, MAE(f): 0.5335, MAE(s): 0.0000, Time: 5.73s, lr: 0.00002000
69: [0m
70: [32m2026-02-25 17:49:27.868[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0056, MAE(e): 0.0039, MAE(f): 0.5663, MAE(s): 0.0000, Time: 8.60s, lr: 0.00002000
71: [0m
72: [32m2026-02-25 17:49:27.880[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 17:49:33.695[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0039, MAE(e): 0.0052, MAE(f): 0.3945, MAE(s): 0.0000, Time: 5.81s, lr: 0.00002000
74: [0m
75: [32m2026-02-25 17:49:42.065[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0043, MAE(e): 0.0039, MAE(f): 0.4382, MAE(s): 0.0000, Time: 8.37s, lr: 0.00002000
76: [0m
77: [32m2026-02-25 17:49:42.072[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 17:49:47.786[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0031, MAE(e): 0.0052, MAE(f): 0.3134, MAE(s): 0.0000, Time: 5.71s, lr: 0.00002000
79: [0m
80: [32m2026-02-25 17:49:56.668[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0035, MAE(e): 0.0044, MAE(f): 0.3486, MAE(s): 0.0000, Time: 8.88s, lr: 0.00002000
81: [0m
82: [32m2026-02-25 17:49:56.675[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 17:50:02.435[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0039, MAE(f): 0.2703, MAE(s): 0.0000, Time: 5.76s, lr: 0.00002000
84: [0m
85: [32m2026-02-25 17:50:10.285[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0029, MAE(e): 0.0039, MAE(f): 0.2955, MAE(s): 0.0000, Time: 7.84s, lr: 0.00002000
86: [0m
87: [32m2026-02-25 17:50:10.298[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 17:50:16.227[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0024, MAE(e): 0.0043, MAE(f): 0.2438, MAE(s): 0.0000, Time: 5.93s, lr: 0.00002000
89: [0m
90: [32m2026-02-25 17:50:23.251[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0026, MAE(e): 0.0035, MAE(f): 0.2633, MAE(s): 0.0000, Time: 7.02s, lr: 0.00002000
91: [0m
92: [32m2026-02-25 17:50:23.261[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 17:50:29.055[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0022, MAE(e): 0.0038, MAE(f): 0.2238, MAE(s): 0.0000, Time: 5.79s, lr: 0.00002000
94: [0m
95: [32m2026-02-25 17:50:35.927[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0024, MAE(e): 0.0034, MAE(f): 0.2403, MAE(s): 0.0000, Time: 6.87s, lr: 0.00002000
96: [0m
97: [32m2026-02-25 17:50:35.938[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 17:50:41.675[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0020, MAE(e): 0.0039, MAE(f): 0.2051, MAE(s): 0.0000, Time: 5.74s, lr: 0.00002000
99: [0m
100: [32m2026-02-25 17:50:51.197[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0022, MAE(e): 0.0033, MAE(f): 0.2220, MAE(s): 0.0000, Time: 9.52s, lr: 0.00002000
101: [0m
102: [32m2026-02-25 17:50:51.209[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 17:50:57.061[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0036, MAE(f): 0.1912, MAE(s): 0.0000, Time: 5.85s, lr: 0.00002000
104: [0m
105: [32m2026-02-25 17:51:05.205[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0020, MAE(e): 0.0032, MAE(f): 0.2066, MAE(s): 0.0000, Time: 8.14s, lr: 0.00002000
106: [0m
107: [32m2026-02-25 17:51:05.210[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 17:51:10.938[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0017, MAE(e): 0.0040, MAE(f): 0.1784, MAE(s): 0.0000, Time: 5.73s, lr: 0.00002000
109: [0m
110: [32m2026-02-25 17:51:20.057[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0019, MAE(e): 0.0031, MAE(f): 0.1935, MAE(s): 0.0000, Time: 9.11s, lr: 0.00002000
111: [0m
112: [32m2026-02-25 17:51:20.068[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 17:51:26.647[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0016, MAE(e): 0.0036, MAE(f): 0.1680, MAE(s): 0.0000, Time: 6.58s, lr: 0.00002000
114: [0m
115: [32m2026-02-25 17:51:34.648[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0018, MAE(e): 0.0029, MAE(f): 0.1821, MAE(s): 0.0000, Time: 7.99s, lr: 0.00002000
116: [0m
117: [32m2026-02-25 17:51:34.655[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 17:51:40.525[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0036, MAE(f): 0.1581, MAE(s): 0.0000, Time: 5.87s, lr: 0.00002000
119: [0m
120: [32m2026-02-25 17:51:48.771[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0017, MAE(e): 0.0028, MAE(f): 0.1721, MAE(s): 0.0000, Time: 8.24s, lr: 0.00002000
121: [0m
122: [32m2026-02-25 17:51:48.783[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 17:51:54.628[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0032, MAE(f): 0.1498, MAE(s): 0.0000, Time: 5.84s, lr: 0.00002000
124: [0m
125: [32m2026-02-25 17:52:03.588[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0016, MAE(e): 0.0027, MAE(f): 0.1631, MAE(s): 0.0000, Time: 8.96s, lr: 0.00002000
126: [0m
127: [32m2026-02-25 17:52:03.595[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 17:52:08.942[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0014, MAE(e): 0.0030, MAE(f): 0.1419, MAE(s): 0.0000, Time: 5.35s, lr: 0.00002000
129: [0m
130: [32m2026-02-25 17:52:17.694[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0026, MAE(f): 0.1551, MAE(s): 0.0000, Time: 8.75s, lr: 0.00002000
131: [0m
132: [32m2026-02-25 17:52:17.705[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 17:52:23.433[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0031, MAE(f): 0.1350, MAE(s): 0.0000, Time: 5.73s, lr: 0.00002000
134: [0m
135: [32m2026-02-25 17:52:29.633[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0024, MAE(f): 0.1478, MAE(s): 0.0000, Time: 6.20s, lr: 0.00002000
136: [0m
137: [32m2026-02-25 17:52:29.640[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 17:52:35.367[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0025, MAE(f): 0.1293, MAE(s): 0.0000, Time: 5.73s, lr: 0.00002000
139: [0m
140: [32m2026-02-25 17:52:47.282[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0023, MAE(f): 0.1412, MAE(s): 0.0000, Time: 11.91s, lr: 0.00002000
141: [0m
142: [32m2026-02-25 17:52:47.294[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 17:52:53.996[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0026, MAE(f): 0.1229, MAE(s): 0.0000, Time: 6.70s, lr: 0.00002000
144: [0m
145: [32m2026-02-25 17:53:03.349[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0023, MAE(f): 0.1350, MAE(s): 0.0000, Time: 9.35s, lr: 0.00002000
146: [0m
147: [32m2026-02-25 17:53:03.365[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 17:53:11.004[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0028, MAE(f): 0.1178, MAE(s): 0.0000, Time: 7.64s, lr: 0.00002000
149: [0m
150: [32m2026-02-25 17:53:22.063[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0022, MAE(f): 0.1292, MAE(s): 0.0000, Time: 11.05s, lr: 0.00002000
151: [0m
152: [32m2026-02-25 17:53:22.069[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 17:53:29.293[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0026, MAE(f): 0.1129, MAE(s): 0.0000, Time: 7.22s, lr: 0.00002000
154: [0m
155: [32m2026-02-25 17:53:38.912[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0021, MAE(f): 0.1239, MAE(s): 0.0000, Time: 9.61s, lr: 0.00002000
156: [0m
157: [32m2026-02-25 17:53:38.923[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 17:53:45.421[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0026, MAE(f): 0.1091, MAE(s): 0.0000, Time: 6.50s, lr: 0.00002000
159: [0m
160: [32m2026-02-25 17:53:56.066[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0020, MAE(f): 0.1192, MAE(s): 0.0000, Time: 10.64s, lr: 0.00002000
161: [0m
