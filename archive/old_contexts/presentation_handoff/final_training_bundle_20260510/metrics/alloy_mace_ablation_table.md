# Alloy MACE Ablation Table

| run | protocol | valid E MAE | valid E RMSE | valid F MAE | valid F RMSE | interpretation |
|---|---|---:|---:|---:|---:|---|
| MACE-old-lr1e-2 | old default lr=0.01 | 34.744 | 64.448 | 70.603 | 123.247 | baseline: weak energy |
| MACE-lr1e-3-quick250 | lr=0.001 quick250 default loss | 23.599 | 73.004 | 62.264 | 114.517 | forces improve, energy still weak |
| MACE-lr1e-3-fair200 | fair200 default loss | 27.523 | 86.401 | 62.076 | 113.747 | fair comparison budget; energy still weak |
| MACE-EW10 | energy_weight=10 | 12.437 | 39.342 | 62.213 | 113.788 | large energy improvement, forces preserved |
| MACE-EW50 | energy_weight=50 | 11.868 | 32.623 | 62.867 | 113.900 | best completed MACE energy result |
