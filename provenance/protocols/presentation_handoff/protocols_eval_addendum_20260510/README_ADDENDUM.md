# Protocols Eval Addendum 20260510

This is a small supplement to `final_training_bundle_20260510.zip`.

It adds completed MACE alloy protocol ablations from the normal partition:
- `stage2_normal`
- `lora_ew10_normal`
- `freeze1_ew10_normal`

This archive should not replace the main bundle. It only adds protocol-ablation evidence for the presentation builder.

The archive intentionally excludes checkpoints, model files, raw datasets, image artifacts, Python caches, and other heavy files. Do not use checkpoints or models from this addendum; only use the included JSON/CSV metrics, logs, scripts, and summaries.

Final recommendation: keep the main MACE alloy row as MACE-EW50 unless the presentation author explicitly chooses a different framing. Use these protocol runs as backup ablations for the loss-weighting discussion.
