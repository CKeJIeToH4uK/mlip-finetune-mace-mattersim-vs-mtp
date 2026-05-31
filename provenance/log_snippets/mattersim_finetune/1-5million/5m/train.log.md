# Log Snippet: repo/coursework/mattersim_finetune/1-5million/5m/train.log

Original size: 320419 bytes. Full raw log not copied.

1: [rank0]:[W225 22:29:37.735417457 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a 
2: [32m2026-02-25 22:29:38.405[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m65[0m - [1mProcessing training datasets...[0m
29:            0.0000,    0.0000,    0.0000,    0.0000,    0.0000])
30: [32m2026-02-25 22:29:40.438[0m | [1mINFO    [0m | [36m__main__[0m:[36mmain[0m:[36m104[0m - [1mProcessing validation datasets...[0m
31: [32m2026-02-25 22:29:44.084[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mfrom_checkpoint[0m:[36m891[0m - [1mLoading the pre-trained mattersim-v1.0.0-5M.pth model[0m
32: [32m2026-02-25 22:29:44.998[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m237[0m - [1mNumber of trainable parameters: 4,548,930[0m
33: [32m2026-02-25 22:29:44.998[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 0 / 500[0m
34: /home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/torch/autograd/graph.py:823: UserWarning: Grad strides do not match bucket view strides. This may indicate grad was not created according to the gradient layout contract, or that the param's strides changed since DDP was constructed.  
35: grad.sizes() = [1, 256], strides() = [1, 1]
37:   return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
38: [32m2026-02-25 22:29:52.403[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0069, MAE(e): 0.0120, MAE(f): 0.6835, MAE(s): 0.0000, Time: 7.40s, lr: 0.00005000
39: [0m
40: [32m2026-02-25 22:29:56.625[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0069, MAE(e): 0.0050, MAE(f): 0.6917, MAE(s): 0.0000, Time: 4.22s, lr: 0.00005000
41: [0m
42: [32m2026-02-25 22:29:57.145[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 1 / 500[0m
43: [32m2026-02-25 22:30:00.847[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0068, MAE(e): 0.0053, MAE(f): 0.6784, MAE(s): 0.0000, Time: 3.70s, lr: 0.00005000
44: [0m
45: [32m2026-02-25 22:30:04.964[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0068, MAE(e): 0.0049, MAE(f): 0.6844, MAE(s): 0.0000, Time: 4.11s, lr: 0.00005000
46: [0m
47: [32m2026-02-25 22:30:05.384[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 2 / 500[0m
48: [32m2026-02-25 22:30:09.070[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0066, MAE(e): 0.0048, MAE(f): 0.6655, MAE(s): 0.0000, Time: 3.69s, lr: 0.00005000
49: [0m
50: [32m2026-02-25 22:30:12.917[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0067, MAE(e): 0.0046, MAE(f): 0.6715, MAE(s): 0.0000, Time: 3.84s, lr: 0.00005000
51: [0m
52: [32m2026-02-25 22:30:13.408[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 3 / 500[0m
53: [32m2026-02-25 22:30:17.073[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0063, MAE(e): 0.0044, MAE(f): 0.6350, MAE(s): 0.0000, Time: 3.67s, lr: 0.00005000
54: [0m
55: [32m2026-02-25 22:30:21.189[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0063, MAE(e): 0.0044, MAE(f): 0.6383, MAE(s): 0.0000, Time: 4.11s, lr: 0.00005000
56: [0m
57: [32m2026-02-25 22:30:21.603[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 4 / 500[0m
58: [32m2026-02-25 22:30:25.242[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0052, MAE(e): 0.0042, MAE(f): 0.5197, MAE(s): 0.0000, Time: 3.64s, lr: 0.00005000
59: [0m
60: [32m2026-02-25 22:30:29.418[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0052, MAE(e): 0.0036, MAE(f): 0.5210, MAE(s): 0.0000, Time: 4.17s, lr: 0.00005000
61: [0m
62: [32m2026-02-25 22:30:29.831[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 5 / 500[0m
63: [32m2026-02-25 22:30:33.434[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0033, MAE(e): 0.0056, MAE(f): 0.3293, MAE(s): 0.0000, Time: 3.60s, lr: 0.00005000
64: [0m
65: [32m2026-02-25 22:30:37.200[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0034, MAE(e): 0.0057, MAE(f): 0.3401, MAE(s): 0.0000, Time: 3.76s, lr: 0.00005000
66: [0m
67: [32m2026-02-25 22:30:37.614[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 6 / 500[0m
68: [32m2026-02-25 22:30:41.190[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0023, MAE(e): 0.0063, MAE(f): 0.2334, MAE(s): 0.0000, Time: 3.58s, lr: 0.00005000
69: [0m
70: [32m2026-02-25 22:30:45.147[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0024, MAE(e): 0.0039, MAE(f): 0.2449, MAE(s): 0.0000, Time: 3.95s, lr: 0.00005000
71: [0m
72: [32m2026-02-25 22:30:45.561[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 7 / 500[0m
73: [32m2026-02-25 22:30:49.191[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0018, MAE(e): 0.0049, MAE(f): 0.1862, MAE(s): 0.0000, Time: 3.63s, lr: 0.00005000
74: [0m
75: [32m2026-02-25 22:30:53.060[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0019, MAE(e): 0.0026, MAE(f): 0.1987, MAE(s): 0.0000, Time: 3.87s, lr: 0.00005000
76: [0m
77: [32m2026-02-25 22:30:53.474[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 8 / 500[0m
78: [32m2026-02-25 22:30:57.001[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0015, MAE(e): 0.0028, MAE(f): 0.1548, MAE(s): 0.0000, Time: 3.53s, lr: 0.00005000
79: [0m
80: [32m2026-02-25 22:31:00.880[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0016, MAE(e): 0.0022, MAE(f): 0.1665, MAE(s): 0.0000, Time: 3.88s, lr: 0.00005000
81: [0m
82: [32m2026-02-25 22:31:01.298[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 9 / 500[0m
83: [32m2026-02-25 22:31:04.870[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0013, MAE(e): 0.0032, MAE(f): 0.1349, MAE(s): 0.0000, Time: 3.57s, lr: 0.00005000
84: [0m
85: [32m2026-02-25 22:31:08.646[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0014, MAE(e): 0.0019, MAE(f): 0.1450, MAE(s): 0.0000, Time: 3.77s, lr: 0.00005000
86: [0m
87: [32m2026-02-25 22:31:09.058[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 10 / 500[0m
88: [32m2026-02-25 22:31:12.686[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0012, MAE(e): 0.0033, MAE(f): 0.1217, MAE(s): 0.0000, Time: 3.63s, lr: 0.00005000
89: [0m
90: [32m2026-02-25 22:31:16.487[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0013, MAE(e): 0.0018, MAE(f): 0.1304, MAE(s): 0.0000, Time: 3.80s, lr: 0.00005000
91: [0m
92: [32m2026-02-25 22:31:16.905[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 11 / 500[0m
93: [32m2026-02-25 22:31:20.486[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0011, MAE(e): 0.0042, MAE(f): 0.1120, MAE(s): 0.0000, Time: 3.58s, lr: 0.00005000
94: [0m
95: [32m2026-02-25 22:31:24.615[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0017, MAE(f): 0.1194, MAE(s): 0.0000, Time: 4.13s, lr: 0.00005000
96: [0m
97: [32m2026-02-25 22:31:25.033[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 12 / 500[0m
98: [32m2026-02-25 22:31:28.603[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0010, MAE(e): 0.0039, MAE(f): 0.1035, MAE(s): 0.0000, Time: 3.57s, lr: 0.00005000
99: [0m
100: [32m2026-02-25 22:31:32.387[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0011, MAE(e): 0.0016, MAE(f): 0.1100, MAE(s): 0.0000, Time: 3.78s, lr: 0.00005000
101: [0m
102: [32m2026-02-25 22:31:32.804[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 13 / 500[0m
103: [32m2026-02-25 22:31:36.389[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0009, MAE(e): 0.0034, MAE(f): 0.0934, MAE(s): 0.0000, Time: 3.58s, lr: 0.00005000
104: [0m
105: [32m2026-02-25 22:31:40.250[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0010, MAE(e): 0.0015, MAE(f): 0.1018, MAE(s): 0.0000, Time: 3.86s, lr: 0.00005000
106: [0m
107: [32m2026-02-25 22:31:40.673[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 14 / 500[0m
108: [32m2026-02-25 22:31:44.235[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0024, MAE(f): 0.0862, MAE(s): 0.0000, Time: 3.56s, lr: 0.00005000
109: [0m
110: [32m2026-02-25 22:31:48.007[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0009, MAE(e): 0.0014, MAE(f): 0.0941, MAE(s): 0.0000, Time: 3.77s, lr: 0.00005000
111: [0m
112: [32m2026-02-25 22:31:48.425[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 15 / 500[0m
113: [32m2026-02-25 22:31:51.979[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0008, MAE(e): 0.0025, MAE(f): 0.0797, MAE(s): 0.0000, Time: 3.55s, lr: 0.00005000
114: [0m
115: [32m2026-02-25 22:31:55.720[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0014, MAE(f): 0.0869, MAE(s): 0.0000, Time: 3.74s, lr: 0.00005000
116: [0m
117: [32m2026-02-25 22:31:56.137[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 16 / 500[0m
118: [32m2026-02-25 22:31:59.788[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0016, MAE(f): 0.0743, MAE(s): 0.0000, Time: 3.65s, lr: 0.00005000
119: [0m
120: [32m2026-02-25 22:32:03.609[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0008, MAE(e): 0.0013, MAE(f): 0.0809, MAE(s): 0.0000, Time: 3.82s, lr: 0.00005000
121: [0m
122: [32m2026-02-25 22:32:04.022[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 17 / 500[0m
123: [32m2026-02-25 22:32:07.594[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0007, MAE(e): 0.0023, MAE(f): 0.0706, MAE(s): 0.0000, Time: 3.57s, lr: 0.00005000
124: [0m
125: [32m2026-02-25 22:32:11.572[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0763, MAE(s): 0.0000, Time: 3.98s, lr: 0.00005000
126: [0m
127: [32m2026-02-25 22:32:11.988[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 18 / 500[0m
128: [32m2026-02-25 22:32:15.544[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0023, MAE(f): 0.0679, MAE(s): 0.0000, Time: 3.56s, lr: 0.00005000
129: [0m
130: [32m2026-02-25 22:32:19.324[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0729, MAE(s): 0.0000, Time: 3.78s, lr: 0.00005000
131: [0m
132: [32m2026-02-25 22:32:19.738[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 19 / 500[0m
133: [32m2026-02-25 22:32:23.322[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0016, MAE(f): 0.0656, MAE(s): 0.0000, Time: 3.58s, lr: 0.00005000
134: [0m
135: [32m2026-02-25 22:32:27.103[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0007, MAE(e): 0.0013, MAE(f): 0.0701, MAE(s): 0.0000, Time: 3.78s, lr: 0.00005000
136: [0m
137: [32m2026-02-25 22:32:27.518[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 20 / 500[0m
138: [32m2026-02-25 22:32:31.076[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0021, MAE(f): 0.0637, MAE(s): 0.0000, Time: 3.56s, lr: 0.00005000
139: [0m
140: [32m2026-02-25 22:32:34.898[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0012, MAE(f): 0.0679, MAE(s): 0.0000, Time: 3.82s, lr: 0.00005000
141: [0m
142: [32m2026-02-25 22:32:35.318[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 21 / 500[0m
143: [32m2026-02-25 22:32:38.867[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0014, MAE(f): 0.0619, MAE(s): 0.0000, Time: 3.55s, lr: 0.00005000
144: [0m
145: [32m2026-02-25 22:32:42.813[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0012, MAE(f): 0.0659, MAE(s): 0.0000, Time: 3.94s, lr: 0.00005000
146: [0m
147: [32m2026-02-25 22:32:43.282[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 22 / 500[0m
148: [32m2026-02-25 22:32:46.872[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0006, MAE(e): 0.0015, MAE(f): 0.0607, MAE(s): 0.0000, Time: 3.59s, lr: 0.00005000
149: [0m
150: [32m2026-02-25 22:32:50.860[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0012, MAE(f): 0.0642, MAE(s): 0.0000, Time: 3.98s, lr: 0.00005000
151: [0m
152: [32m2026-02-25 22:32:51.280[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 23 / 500[0m
153: [32m2026-02-25 22:32:54.961[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0005, MAE(e): 0.0015, MAE(f): 0.0591, MAE(s): 0.0000, Time: 3.68s, lr: 0.00005000
154: [0m
155: [32m2026-02-25 22:32:58.806[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0012, MAE(f): 0.0627, MAE(s): 0.0000, Time: 3.84s, lr: 0.00005000
156: [0m
157: [32m2026-02-25 22:32:59.273[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_model[0m:[36m241[0m - [1mEpoch: 24 / 500[0m
158: [32m2026-02-25 22:33:02.998[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mtrain: Loss: 0.0005, MAE(e): 0.0017, MAE(f): 0.0584, MAE(s): 0.0000, Time: 3.72s, lr: 0.00005000
159: [0m
160: [32m2026-02-25 22:33:06.821[0m | [1mINFO    [0m | [36mmattersim.forcefield.potential[0m:[36mtrain_one_epoch[0m:[36m618[0m - [1mval: Loss: 0.0006, MAE(e): 0.0011, MAE(f): 0.0613, MAE(s): 0.0000, Time: 3.82s, lr: 0.00005000
161: [0m
