# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr1e-5_bs32/train.log

Original size: 320370 bytes. Full raw log not copied.

1: [rank0]:[W225 19:47:59.834644543 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 19:48:00.230[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 19:48:03.907[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 19:48:07.781[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 19:48:08.720[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 19:48:08.721[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 19:48:20.186[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0070, MAE(e): 0.0219, MAE(f): 0.6856, MAE(s): 0.0000, Time: 11.46s, lr: 0.00001000
39: [0m
40: [32m2026-02-25 19:48:23.651[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0070, MAE(e): 0.0202, MAE(f): 0.6943, MAE(s): 0.0000, Time: 3.46s, lr: 0.00001000
41: [0m
42: [32m2026-02-25 19:48:23.658[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 19:48:26.024[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0169, MAE(f): 0.6849, MAE(s): 0.0000, Time: 2.37s, lr: 0.00001000
44: [0m
45: [32m2026-02-25 19:48:29.357[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0070, MAE(e): 0.0157, MAE(f): 0.6943, MAE(s): 0.0000, Time: 3.33s, lr: 0.00001000
46: [0m
47: [32m2026-02-25 19:48:29.365[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 19:48:32.054[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0119, MAE(f): 0.6846, MAE(s): 0.0000, Time: 2.69s, lr: 0.00001000
49: [0m
50: [32m2026-02-25 19:48:34.891[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0070, MAE(e): 0.0114, MAE(f): 0.6942, MAE(s): 0.0000, Time: 2.83s, lr: 0.00001000
51: [0m
52: [32m2026-02-25 19:48:34.896[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 19:48:37.002[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0080, MAE(f): 0.6851, MAE(s): 0.0000, Time: 2.11s, lr: 0.00001000
54: [0m
55: [32m2026-02-25 19:48:39.941[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0078, MAE(f): 0.6940, MAE(s): 0.0000, Time: 2.94s, lr: 0.00001000
56: [0m
57: [32m2026-02-25 19:48:39.947[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 19:48:42.435[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0057, MAE(f): 0.6838, MAE(s): 0.0000, Time: 2.49s, lr: 0.00001000
59: [0m
60: [32m2026-02-25 19:48:45.377[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0059, MAE(f): 0.6935, MAE(s): 0.0000, Time: 2.94s, lr: 0.00001000
61: [0m
62: [32m2026-02-25 19:48:45.382[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 19:48:47.801[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0050, MAE(f): 0.6837, MAE(s): 0.0000, Time: 2.42s, lr: 0.00001000
64: [0m
65: [32m2026-02-25 19:48:50.772[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0052, MAE(f): 0.6928, MAE(s): 0.0000, Time: 2.97s, lr: 0.00001000
66: [0m
67: [32m2026-02-25 19:48:50.778[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 19:48:53.200[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6824, MAE(s): 0.0000, Time: 2.42s, lr: 0.00001000
69: [0m
70: [32m2026-02-25 19:48:55.938[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0050, MAE(f): 0.6918, MAE(s): 0.0000, Time: 2.74s, lr: 0.00001000
71: [0m
72: [32m2026-02-25 19:48:55.943[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 19:48:57.871[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6810, MAE(s): 0.0000, Time: 1.93s, lr: 0.00001000
74: [0m
75: [32m2026-02-25 19:49:00.613[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0049, MAE(f): 0.6907, MAE(s): 0.0000, Time: 2.74s, lr: 0.00001000
76: [0m
77: [32m2026-02-25 19:49:00.618[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 19:49:02.804[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6796, MAE(s): 0.0000, Time: 2.19s, lr: 0.00001000
79: [0m
80: [32m2026-02-25 19:49:05.679[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0049, MAE(f): 0.6894, MAE(s): 0.0000, Time: 2.87s, lr: 0.00001000
81: [0m
82: [32m2026-02-25 19:49:05.684[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 19:49:07.685[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6784, MAE(s): 0.0000, Time: 2.00s, lr: 0.00001000
84: [0m
85: [32m2026-02-25 19:49:10.883[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0049, MAE(f): 0.6881, MAE(s): 0.0000, Time: 3.19s, lr: 0.00001000
86: [0m
87: [32m2026-02-25 19:49:10.888[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 19:49:13.162[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6764, MAE(s): 0.0000, Time: 2.27s, lr: 0.00001000
89: [0m
90: [32m2026-02-25 19:49:15.847[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6866, MAE(s): 0.0000, Time: 2.68s, lr: 0.00001000
91: [0m
92: [32m2026-02-25 19:49:15.852[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 19:49:18.348[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6742, MAE(s): 0.0000, Time: 2.50s, lr: 0.00001000
94: [0m
95: [32m2026-02-25 19:49:21.835[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6849, MAE(s): 0.0000, Time: 3.48s, lr: 0.00001000
96: [0m
97: [32m2026-02-25 19:49:21.841[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 19:49:24.546[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6718, MAE(s): 0.0000, Time: 2.70s, lr: 0.00001000
99: [0m
100: [32m2026-02-25 19:49:27.685[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6830, MAE(s): 0.0000, Time: 3.13s, lr: 0.00001000
101: [0m
102: [32m2026-02-25 19:49:27.690[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 19:49:30.013[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6686, MAE(s): 0.0000, Time: 2.32s, lr: 0.00001000
104: [0m
105: [32m2026-02-25 19:49:32.930[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6808, MAE(s): 0.0000, Time: 2.91s, lr: 0.00001000
106: [0m
107: [32m2026-02-25 19:49:32.936[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 19:49:35.312[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0047, MAE(f): 0.6657, MAE(s): 0.0000, Time: 2.38s, lr: 0.00001000
109: [0m
110: [32m2026-02-25 19:49:39.000[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6783, MAE(s): 0.0000, Time: 3.68s, lr: 0.00001000
111: [0m
112: [32m2026-02-25 19:49:39.005[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 19:49:41.361[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6619, MAE(s): 0.0000, Time: 2.36s, lr: 0.00001000
114: [0m
115: [32m2026-02-25 19:49:44.327[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6753, MAE(s): 0.0000, Time: 2.96s, lr: 0.00001000
116: [0m
117: [32m2026-02-25 19:49:44.332[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 19:49:47.088[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0047, MAE(f): 0.6569, MAE(s): 0.0000, Time: 2.76s, lr: 0.00001000
119: [0m
120: [32m2026-02-25 19:49:50.789[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6718, MAE(s): 0.0000, Time: 3.70s, lr: 0.00001000
121: [0m
122: [32m2026-02-25 19:49:50.795[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 19:49:53.542[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0046, MAE(f): 0.6519, MAE(s): 0.0000, Time: 2.75s, lr: 0.00001000
124: [0m
125: [32m2026-02-25 19:49:56.767[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0066, MAE(e): 0.0047, MAE(f): 0.6676, MAE(s): 0.0000, Time: 3.22s, lr: 0.00001000
126: [0m
127: [32m2026-02-25 19:49:56.771[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 19:49:59.256[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0064, MAE(e): 0.0046, MAE(f): 0.6442, MAE(s): 0.0000, Time: 2.48s, lr: 0.00001000
129: [0m
130: [32m2026-02-25 19:50:02.352[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6625, MAE(s): 0.0000, Time: 3.09s, lr: 0.00001000
131: [0m
132: [32m2026-02-25 19:50:02.357[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 19:50:04.728[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0063, MAE(e): 0.0045, MAE(f): 0.6336, MAE(s): 0.0000, Time: 2.37s, lr: 0.00001000
134: [0m
135: [32m2026-02-25 19:50:07.737[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0065, MAE(e): 0.0046, MAE(f): 0.6561, MAE(s): 0.0000, Time: 3.00s, lr: 0.00001000
136: [0m
137: [32m2026-02-25 19:50:07.746[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 19:50:10.442[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0062, MAE(e): 0.0043, MAE(f): 0.6186, MAE(s): 0.0000, Time: 2.70s, lr: 0.00001000
139: [0m
140: [32m2026-02-25 19:50:13.519[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0064, MAE(e): 0.0045, MAE(f): 0.6478, MAE(s): 0.0000, Time: 3.07s, lr: 0.00001000
141: [0m
142: [32m2026-02-25 19:50:13.524[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 19:50:15.969[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0059, MAE(e): 0.0043, MAE(f): 0.5982, MAE(s): 0.0000, Time: 2.44s, lr: 0.00001000
144: [0m
145: [32m2026-02-25 19:50:18.598[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0063, MAE(e): 0.0044, MAE(f): 0.6367, MAE(s): 0.0000, Time: 2.62s, lr: 0.00001000
146: [0m
147: [32m2026-02-25 19:50:18.602[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 19:50:21.128[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0056, MAE(e): 0.0042, MAE(f): 0.5653, MAE(s): 0.0000, Time: 2.53s, lr: 0.00001000
149: [0m
150: [32m2026-02-25 19:50:23.987[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0062, MAE(e): 0.0043, MAE(f): 0.6212, MAE(s): 0.0000, Time: 2.85s, lr: 0.00001000
151: [0m
152: [32m2026-02-25 19:50:23.992[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 19:50:26.421[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0052, MAE(e): 0.0039, MAE(f): 0.5190, MAE(s): 0.0000, Time: 2.43s, lr: 0.00001000
154: [0m
155: [32m2026-02-25 19:50:29.388[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0060, MAE(e): 0.0040, MAE(f): 0.5990, MAE(s): 0.0000, Time: 2.96s, lr: 0.00001000
156: [0m
157: [32m2026-02-25 19:50:29.393[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 19:50:31.715[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0046, MAE(e): 0.0037, MAE(f): 0.4682, MAE(s): 0.0000, Time: 2.32s, lr: 0.00001000
159: [0m
160: [32m2026-02-25 19:50:35.150[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0056, MAE(e): 0.0039, MAE(f): 0.5686, MAE(s): 0.0000, Time: 3.43s, lr: 0.00001000
161: [0m
