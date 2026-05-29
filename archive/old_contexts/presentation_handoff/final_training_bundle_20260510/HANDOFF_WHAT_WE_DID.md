# Handoff: What We Did

## H2O
- The old H2O MTP run was mislabelled as mtp20, but the actual constructor used level=16.
- The old metrics.json also contains level=16, so old H2O MTP numbers are MTP-16.
- Created clean folder water/mtp_clean20_20260508.
- Trained clean MTP level 20 on H2O.
- Confirmed level=20 and n_params=450.
- Saved metrics_20_clean.json and metrics_20_clean.csv.

## Alloy MACE
- Old MACE alloy metrics looked suspiciously weak, especially energy.
- Initial hypothesis: lr=0.01 was too high.
- Ran lr=0.001 quick/fair runs.
- lr=0.001 improved forces but energy RMSE remained weak.
- Inspected MACE flags through sbatch/help context and found energy_weight/forces_weight.
- Launched EW10/EW50 normal runs to avoid gpu-ef-quick preemption.
- EW10/EW50 showed that energy-weighted loss strongly fixes energy RMSE.
- Best final candidate: MACE-EW50.

## Preemption
- gpu-ef-quick is preemptible.
- Some quick ablations were interrupted.
- Normal EW10/EW50 runs are preferred source-of-truth.
