# Log Snippet: repo/coursework/mattersim_finetune/sweep_lr_bs/runs/lr5e-5_bs8/train.log

Original size: 320375 bytes. Full raw log not copied.

1: [rank0]:[W225 16:25:05.631883528 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 16:25:06.951[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 16:25:11.026[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 16:25:14.118[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m877[0m - [1mLoading the pre-trained mattersim-v1.0.0-1M.pth model[0m
32: [32m2026-02-25 16:25:16.226[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 890,034[0m
33: [32m2026-02-25 16:25:16.227[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 128], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 16:25:35.740[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0069, MAE(f): 0.6785, MAE(s): 0.0000, Time: 19.51s, lr: 0.00005000
39: [0m
40: [32m2026-02-25 16:25:44.321[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0046, MAE(f): 0.6760, MAE(s): 0.0000, Time: 8.58s, lr: 0.00005000
41: [0m
42: [32m2026-02-25 16:25:44.327[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 16:25:50.296[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0055, MAE(e): 0.0053, MAE(f): 0.5577, MAE(s): 0.0000, Time: 5.97s, lr: 0.00005000
44: [0m
45: [32m2026-02-25 16:25:59.410[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0044, MAE(e): 0.0039, MAE(f): 0.4476, MAE(s): 0.0000, Time: 9.11s, lr: 0.00005000
46: [0m
47: [32m2026-02-25 16:25:59.416[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 16:26:06.352[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0027, MAE(e): 0.0066, MAE(f): 0.2736, MAE(s): 0.0000, Time: 6.94s, lr: 0.00005000
49: [0m
50: [32m2026-02-25 16:26:13.921[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0024, MAE(e): 0.0036, MAE(f): 0.2470, MAE(s): 0.0000, Time: 7.57s, lr: 0.00005000
51: [0m
52: [32m2026-02-25 16:26:13.926[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 16:26:19.740[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0019, MAE(e): 0.0049, MAE(f): 0.1944, MAE(s): 0.0000, Time: 5.81s, lr: 0.00005000
54: [0m
55: [32m2026-02-25 16:26:27.303[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0018, MAE(e): 0.0033, MAE(f): 0.1868, MAE(s): 0.0000, Time: 7.56s, lr: 0.00005000
56: [0m
57: [32m2026-02-25 16:26:27.308[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 16:26:33.037[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0044, MAE(f): 0.1522, MAE(s): 0.0000, Time: 5.73s, lr: 0.00005000
59: [0m
60: [32m2026-02-25 16:26:40.569[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0015, MAE(e): 0.0027, MAE(f): 0.1510, MAE(s): 0.0000, Time: 7.53s, lr: 0.00005000
61: [0m
62: [32m2026-02-25 16:26:40.574[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 16:26:46.320[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0036, MAE(f): 0.1251, MAE(s): 0.0000, Time: 5.75s, lr: 0.00005000
64: [0m
65: [32m2026-02-25 16:26:53.952[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0012, MAE(e): 0.0022, MAE(f): 0.1262, MAE(s): 0.0000, Time: 7.63s, lr: 0.00005000
66: [0m
67: [32m2026-02-25 16:26:53.957[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 16:26:59.684[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0030, MAE(f): 0.1083, MAE(s): 0.0000, Time: 5.73s, lr: 0.00005000
69: [0m
70: [32m2026-02-25 16:27:07.234[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0019, MAE(f): 0.1102, MAE(s): 0.0000, Time: 7.55s, lr: 0.00005000
71: [0m
72: [32m2026-02-25 16:27:07.239[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 16:27:12.990[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0027, MAE(f): 0.0999, MAE(s): 0.0000, Time: 5.75s, lr: 0.00005000
74: [0m
75: [32m2026-02-25 16:27:20.624[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0018, MAE(f): 0.1009, MAE(s): 0.0000, Time: 7.63s, lr: 0.00005000
76: [0m
77: [32m2026-02-25 16:27:20.628[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 16:27:26.359[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0028, MAE(f): 0.0935, MAE(s): 0.0000, Time: 5.73s, lr: 0.00005000
79: [0m
80: [32m2026-02-25 16:27:33.938[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0016, MAE(f): 0.0948, MAE(s): 0.0000, Time: 7.58s, lr: 0.00005000
81: [0m
82: [32m2026-02-25 16:27:33.942[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 16:27:40.566[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0028, MAE(f): 0.0884, MAE(s): 0.0000, Time: 6.62s, lr: 0.00005000
84: [0m
85: [32m2026-02-25 16:27:49.530[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0016, MAE(f): 0.0900, MAE(s): 0.0000, Time: 8.96s, lr: 0.00005000
86: [0m
87: [32m2026-02-25 16:27:49.535[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 16:27:57.334[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0027, MAE(f): 0.0839, MAE(s): 0.0000, Time: 7.80s, lr: 0.00005000
89: [0m
90: [32m2026-02-25 16:28:06.275[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0015, MAE(f): 0.0860, MAE(s): 0.0000, Time: 8.94s, lr: 0.00005000
91: [0m
92: [32m2026-02-25 16:28:06.280[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 16:28:14.129[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0022, MAE(f): 0.0807, MAE(s): 0.0000, Time: 7.85s, lr: 0.00005000
94: [0m
95: [32m2026-02-25 16:28:23.557[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0014, MAE(f): 0.0827, MAE(s): 0.0000, Time: 9.42s, lr: 0.00005000
96: [0m
97: [32m2026-02-25 16:28:23.562[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 16:28:31.288[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0020, MAE(f): 0.0774, MAE(s): 0.0000, Time: 7.73s, lr: 0.00005000
99: [0m
100: [32m2026-02-25 16:28:40.339[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0014, MAE(f): 0.0797, MAE(s): 0.0000, Time: 9.05s, lr: 0.00005000
101: [0m
102: [32m2026-02-25 16:28:40.344[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 16:28:46.615[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0020, MAE(f): 0.0746, MAE(s): 0.0000, Time: 6.27s, lr: 0.00005000
104: [0m
105: [32m2026-02-25 16:28:54.668[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0771, MAE(s): 0.0000, Time: 8.05s, lr: 0.00005000
106: [0m
107: [32m2026-02-25 16:28:54.674[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 16:29:00.553[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0020, MAE(f): 0.0725, MAE(s): 0.0000, Time: 5.88s, lr: 0.00005000
109: [0m
110: [32m2026-02-25 16:29:08.121[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0747, MAE(s): 0.0000, Time: 7.57s, lr: 0.00005000
111: [0m
112: [32m2026-02-25 16:29:08.126[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 16:29:13.839[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0020, MAE(f): 0.0707, MAE(s): 0.0000, Time: 5.71s, lr: 0.00005000
114: [0m
115: [32m2026-02-25 16:29:21.422[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0012, MAE(f): 0.0724, MAE(s): 0.0000, Time: 7.58s, lr: 0.00005000
116: [0m
117: [32m2026-02-25 16:29:21.425[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 16:29:27.218[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0028, MAE(f): 0.0688, MAE(s): 0.0000, Time: 5.79s, lr: 0.00005000
119: [0m
120: [32m2026-02-25 16:29:34.786[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0012, MAE(f): 0.0704, MAE(s): 0.0000, Time: 7.57s, lr: 0.00005000
121: [0m
122: [32m2026-02-25 16:29:34.791[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 16:29:40.728[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0023, MAE(f): 0.0666, MAE(s): 0.0000, Time: 5.94s, lr: 0.00005000
124: [0m
125: [32m2026-02-25 16:29:48.317[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0011, MAE(f): 0.0685, MAE(s): 0.0000, Time: 7.59s, lr: 0.00005000
126: [0m
127: [32m2026-02-25 16:29:48.322[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 16:29:54.218[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0020, MAE(f): 0.0658, MAE(s): 0.0000, Time: 5.90s, lr: 0.00005000
129: [0m
130: [32m2026-02-25 16:30:01.829[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0011, MAE(f): 0.0669, MAE(s): 0.0000, Time: 7.61s, lr: 0.00005000
131: [0m
132: [32m2026-02-25 16:30:01.834[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 16:30:07.678[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0018, MAE(f): 0.0640, MAE(s): 0.0000, Time: 5.84s, lr: 0.00005000
134: [0m
135: [32m2026-02-25 16:30:15.235[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0011, MAE(f): 0.0654, MAE(s): 0.0000, Time: 7.55s, lr: 0.00005000
136: [0m
137: [32m2026-02-25 16:30:15.240[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 16:30:21.028[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0022, MAE(f): 0.0631, MAE(s): 0.0000, Time: 5.79s, lr: 0.00005000
139: [0m
140: [32m2026-02-25 16:30:28.693[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0640, MAE(s): 0.0000, Time: 7.66s, lr: 0.00005000
141: [0m
142: [32m2026-02-25 16:30:28.697[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 16:30:34.499[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0026, MAE(f): 0.0616, MAE(s): 0.0000, Time: 5.80s, lr: 0.00005000
144: [0m
145: [32m2026-02-25 16:30:42.245[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0628, MAE(s): 0.0000, Time: 7.74s, lr: 0.00005000
146: [0m
147: [32m2026-02-25 16:30:42.250[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 16:30:47.987[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0016, MAE(f): 0.0605, MAE(s): 0.0000, Time: 5.74s, lr: 0.00005000
149: [0m
150: [32m2026-02-25 16:30:55.648[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0617, MAE(s): 0.0000, Time: 7.66s, lr: 0.00005000
151: [0m
152: [32m2026-02-25 16:30:55.653[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 16:31:01.445[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0005, MAE(e): 0.0018, MAE(f): 0.0594, MAE(s): 0.0000, Time: 5.79s, lr: 0.00005000
154: [0m
155: [32m2026-02-25 16:31:09.057[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0010, MAE(f): 0.0606, MAE(s): 0.0000, Time: 7.61s, lr: 0.00005000
156: [0m
157: [32m2026-02-25 16:31:09.062[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 16:31:14.911[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0005, MAE(e): 0.0019, MAE(f): 0.0583, MAE(s): 0.0000, Time: 5.85s, lr: 0.00005000
159: [0m
160: [32m2026-02-25 16:31:22.523[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0005, MAE(e): 0.0010, MAE(f): 0.0596, MAE(s): 0.0000, Time: 7.61s, lr: 0.00005000
161: [0m
