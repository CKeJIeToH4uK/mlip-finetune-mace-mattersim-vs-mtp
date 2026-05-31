# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr2e-5_bs64/train.log

Original size: 320369 bytes. Full raw log not copied.

1: [rank0]:[W225 18:25:06.731050880 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 18:25:07.289[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 18:25:09.008[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 18:25:12.141[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 18:25:12.314[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 18:25:12.314[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 18:25:16.582[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0070, MAE(e): 0.0221, MAE(f): 0.6854, MAE(s): 0.0000, Time: 4.27s, lr: 0.00002000
39: [0m
40: [32m2026-02-25 18:25:18.232[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0071, MAE(e): 0.0204, MAE(f): 0.6950, MAE(s): 0.0000, Time: 1.65s, lr: 0.00002000
41: [0m
42: [32m2026-02-25 18:25:18.235[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 18:25:19.475[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0171, MAE(f): 0.6854, MAE(s): 0.0000, Time: 1.24s, lr: 0.00002000
44: [0m
45: [32m2026-02-25 18:25:21.121[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0070, MAE(e): 0.0158, MAE(f): 0.6949, MAE(s): 0.0000, Time: 1.64s, lr: 0.00002000
46: [0m
47: [32m2026-02-25 18:25:21.129[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 18:25:22.342[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0120, MAE(f): 0.6851, MAE(s): 0.0000, Time: 1.21s, lr: 0.00002000
49: [0m
50: [32m2026-02-25 18:25:24.029[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0070, MAE(e): 0.0113, MAE(f): 0.6949, MAE(s): 0.0000, Time: 1.68s, lr: 0.00002000
51: [0m
52: [32m2026-02-25 18:25:24.033[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 18:25:25.318[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0078, MAE(f): 0.6851, MAE(s): 0.0000, Time: 1.29s, lr: 0.00002000
54: [0m
55: [32m2026-02-25 18:25:27.017[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0076, MAE(f): 0.6948, MAE(s): 0.0000, Time: 1.70s, lr: 0.00002000
56: [0m
57: [32m2026-02-25 18:25:27.022[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 18:25:28.296[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0054, MAE(f): 0.6845, MAE(s): 0.0000, Time: 1.27s, lr: 0.00002000
59: [0m
60: [32m2026-02-25 18:25:30.052[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0055, MAE(f): 0.6944, MAE(s): 0.0000, Time: 1.75s, lr: 0.00002000
61: [0m
62: [32m2026-02-25 18:25:30.058[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 18:25:31.349[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6840, MAE(s): 0.0000, Time: 1.29s, lr: 0.00002000
64: [0m
65: [32m2026-02-25 18:25:33.049[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0049, MAE(f): 0.6938, MAE(s): 0.0000, Time: 1.70s, lr: 0.00002000
66: [0m
67: [32m2026-02-25 18:25:33.054[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 18:25:34.311[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6830, MAE(s): 0.0000, Time: 1.26s, lr: 0.00002000
69: [0m
70: [32m2026-02-25 18:25:36.067[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6929, MAE(s): 0.0000, Time: 1.75s, lr: 0.00002000
71: [0m
72: [32m2026-02-25 18:25:36.072[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 18:25:37.343[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6818, MAE(s): 0.0000, Time: 1.27s, lr: 0.00002000
74: [0m
75: [32m2026-02-25 18:25:39.086[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6918, MAE(s): 0.0000, Time: 1.74s, lr: 0.00002000
76: [0m
77: [32m2026-02-25 18:25:39.092[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 18:25:40.347[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0047, MAE(f): 0.6804, MAE(s): 0.0000, Time: 1.25s, lr: 0.00002000
79: [0m
80: [32m2026-02-25 18:25:42.076[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0048, MAE(f): 0.6906, MAE(s): 0.0000, Time: 1.73s, lr: 0.00002000
81: [0m
82: [32m2026-02-25 18:25:42.080[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 18:25:43.324[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6792, MAE(s): 0.0000, Time: 1.24s, lr: 0.00002000
84: [0m
85: [32m2026-02-25 18:25:45.043[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0049, MAE(f): 0.6893, MAE(s): 0.0000, Time: 1.72s, lr: 0.00002000
86: [0m
87: [32m2026-02-25 18:25:45.048[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 18:25:46.269[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6770, MAE(s): 0.0000, Time: 1.22s, lr: 0.00002000
89: [0m
90: [32m2026-02-25 18:25:48.380[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0049, MAE(f): 0.6879, MAE(s): 0.0000, Time: 2.11s, lr: 0.00002000
91: [0m
92: [32m2026-02-25 18:25:48.384[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 18:25:49.693[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6751, MAE(s): 0.0000, Time: 1.31s, lr: 0.00002000
94: [0m
95: [32m2026-02-25 18:25:51.406[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0049, MAE(f): 0.6864, MAE(s): 0.0000, Time: 1.71s, lr: 0.00002000
96: [0m
97: [32m2026-02-25 18:25:51.409[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 18:25:52.703[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6733, MAE(s): 0.0000, Time: 1.29s, lr: 0.00002000
99: [0m
100: [32m2026-02-25 18:25:54.932[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6848, MAE(s): 0.0000, Time: 2.23s, lr: 0.00002000
101: [0m
102: [32m2026-02-25 18:25:54.935[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 18:25:56.110[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6708, MAE(s): 0.0000, Time: 1.17s, lr: 0.00002000
104: [0m
105: [32m2026-02-25 18:25:57.883[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6829, MAE(s): 0.0000, Time: 1.77s, lr: 0.00002000
106: [0m
107: [32m2026-02-25 18:25:57.887[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 18:25:59.187[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6682, MAE(s): 0.0000, Time: 1.30s, lr: 0.00002000
109: [0m
110: [32m2026-02-25 18:26:01.052[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0048, MAE(f): 0.6807, MAE(s): 0.0000, Time: 1.86s, lr: 0.00002000
111: [0m
112: [32m2026-02-25 18:26:01.059[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 18:26:02.401[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6654, MAE(s): 0.0000, Time: 1.34s, lr: 0.00002000
114: [0m
115: [32m2026-02-25 18:26:04.032[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6782, MAE(s): 0.0000, Time: 1.63s, lr: 0.00002000
116: [0m
117: [32m2026-02-25 18:26:04.035[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 18:26:05.308[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0046, MAE(f): 0.6612, MAE(s): 0.0000, Time: 1.27s, lr: 0.00002000
119: [0m
120: [32m2026-02-25 18:26:07.370[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0048, MAE(f): 0.6753, MAE(s): 0.0000, Time: 2.06s, lr: 0.00002000
121: [0m
122: [32m2026-02-25 18:26:07.375[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 18:26:08.698[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0046, MAE(f): 0.6568, MAE(s): 0.0000, Time: 1.32s, lr: 0.00002000
124: [0m
125: [32m2026-02-25 18:26:10.840[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0047, MAE(f): 0.6720, MAE(s): 0.0000, Time: 2.14s, lr: 0.00002000
126: [0m
127: [32m2026-02-25 18:26:10.845[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 18:26:12.206[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0065, MAE(e): 0.0046, MAE(f): 0.6514, MAE(s): 0.0000, Time: 1.36s, lr: 0.00002000
129: [0m
130: [32m2026-02-25 18:26:14.097[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0066, MAE(e): 0.0047, MAE(f): 0.6680, MAE(s): 0.0000, Time: 1.89s, lr: 0.00002000
131: [0m
132: [32m2026-02-25 18:26:14.101[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 18:26:15.418[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0064, MAE(e): 0.0045, MAE(f): 0.6443, MAE(s): 0.0000, Time: 1.32s, lr: 0.00002000
134: [0m
135: [32m2026-02-25 18:26:17.510[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0066, MAE(e): 0.0047, MAE(f): 0.6632, MAE(s): 0.0000, Time: 2.09s, lr: 0.00002000
136: [0m
137: [32m2026-02-25 18:26:17.515[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 18:26:18.637[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0063, MAE(e): 0.0044, MAE(f): 0.6346, MAE(s): 0.0000, Time: 1.12s, lr: 0.00002000
139: [0m
140: [32m2026-02-25 18:26:20.434[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0065, MAE(e): 0.0046, MAE(f): 0.6573, MAE(s): 0.0000, Time: 1.80s, lr: 0.00002000
141: [0m
142: [32m2026-02-25 18:26:20.438[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 18:26:21.743[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0062, MAE(e): 0.0044, MAE(f): 0.6227, MAE(s): 0.0000, Time: 1.31s, lr: 0.00002000
144: [0m
145: [32m2026-02-25 18:26:23.778[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0065, MAE(e): 0.0045, MAE(f): 0.6500, MAE(s): 0.0000, Time: 2.03s, lr: 0.00002000
146: [0m
147: [32m2026-02-25 18:26:23.783[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 18:26:25.038[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0060, MAE(e): 0.0043, MAE(f): 0.6058, MAE(s): 0.0000, Time: 1.26s, lr: 0.00002000
149: [0m
150: [32m2026-02-25 18:26:26.582[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0064, MAE(e): 0.0044, MAE(f): 0.6405, MAE(s): 0.0000, Time: 1.54s, lr: 0.00002000
151: [0m
152: [32m2026-02-25 18:26:26.587[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 18:26:27.732[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0058, MAE(e): 0.0042, MAE(f): 0.5814, MAE(s): 0.0000, Time: 1.14s, lr: 0.00002000
154: [0m
155: [32m2026-02-25 18:26:29.490[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0062, MAE(e): 0.0043, MAE(f): 0.6279, MAE(s): 0.0000, Time: 1.76s, lr: 0.00002000
156: [0m
157: [32m2026-02-25 18:26:29.495[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 18:26:30.784[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0054, MAE(e): 0.0041, MAE(f): 0.5454, MAE(s): 0.0000, Time: 1.29s, lr: 0.00002000
159: [0m
160: [32m2026-02-25 18:26:32.548[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0061, MAE(e): 0.0042, MAE(f): 0.6107, MAE(s): 0.0000, Time: 1.76s, lr: 0.00002000
161: [0m
