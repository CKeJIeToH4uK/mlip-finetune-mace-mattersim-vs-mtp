# Training Figures Index

| path | likely content | source confirmed? | usable for final talk | notes |
|---|---|---|---|---|
| `repo/coursework/new_datasets/figures/loss_mace.png` | MACE H2O/alloy validation RMSE curves with MTP reference lines | yes: analysis_v2.ipynb cells 21-22 parse water/mace/train.log and alloy/mace/train.log | yes, with caveats | MACE curves use RMSE; MTP references use RMSE; H2O reference uses current MTP lv16 naming caveat; alloy MACE metrics are suspicious and marked TODO; dimensions=2076 x 1474; bytes=278239 |
| `repo/coursework/new_datasets/figures/loss_mattersim.png` | MatterSim H2O/alloy train/valid MAE curves with MTP reference lines | yes: analysis_v2.ipynb cells 21 and 24 parse water/mattersim/train.log and alloy/mattersim/train.log | backup / replot before main deck | Notebook plots MatterSim MAE curves but MTP reference lines come from RMSE values; metric mismatch should be fixed or footnoted before main-deck use; dimensions=2076 x 1474; bytes=218537 |
| `19.03.26/training_curves_comparison.png` | Organic 300K MACE vs MatterSim training curves | yes: 19.03.26/analysis.ipynb cells 3-7 parse epoch_vs_err_25_mace results/train.txt and epoch_vs_err_mattersim/train.log | yes | Source notebook was inspected as code/metadata only; figure compares MAE(F), MAE(E/atom), and loss on log scale; dimensions=2681 x 1481; bytes=392529 |
