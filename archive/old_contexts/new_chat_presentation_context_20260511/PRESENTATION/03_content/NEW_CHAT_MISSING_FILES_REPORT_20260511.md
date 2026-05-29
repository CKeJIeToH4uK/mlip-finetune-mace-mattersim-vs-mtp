# NEW CHAT MISSING FILES REPORT 2026-05-11

This report records the files requested for the new-chat handoff and whether they were found locally on 2026-05-10. Missing entries are factual; no missing content was invented.

## Source archives

All three requested source archives were found and copied into `PRESENTATION/00_inbox/`:

- found: `presentation_full_context.zip`
- found: `final_training_bundle_20260510.zip`
- found: `protocols_eval_addendum_20260510.zip`

The archive filenames were checked for forbidden path patterns by listing their contents; no `.pt`, `.pth`, `.ckpt`, `.model`, `raw`, `checkpoint`, `__pycache__`, or `.DS_Store` entries were detected in those archive listings.

## Theory PDFs

All three requested theory PDFs were found and copied into `PRESENTATION/03_content/theory_pdfs/`:

- found: `mattersim.pdf`
- found: `m3gnet.pdf`
- found: `mace.ipynb.pdf`

## Final metrics / results source-of-truth files

Found and copied into `PRESENTATION/03_content/results_handoff/`:

- `final_metrics_long.csv`
- `final_metrics_wide.csv`
- `alloy_mace_ablation_table.md`
- `water_mtp_table.md`
- `FINAL_NUMBERS_TO_VERIFY.md`
- `FINAL_CLAIMS_AND_CAVEATS.md`
- `HANDOFF_WHAT_WE_DID.md`
- `README_BUNDLE.md`

Missing:

- `updated_final_metrics_summary_v2.md`
- `updated_final_tables_v2.md`
- `updated_claims_caveats_v2.md`
- `updated_figure_plan_v2.md`

## Architecture files

Found:

- `05_deck/main.tex`
- `05_deck/main_architecture_preview.tex`
- `05_deck/sections/03_methods_architecture.tex`
- `05_deck/sections/arch_01_ml_potential_task.tex`
- `05_deck/sections/arch_02_m3gnet_overview.tex`
- `05_deck/sections/arch_03_graph_featurizer.tex`
- `05_deck/sections/arch_04_three_body_block.tex`
- `05_deck/sections/arch_05_many_body_to_bond.tex`
- `05_deck/sections/arch_06_graph_convolution.tex`
- `05_deck/sections/arch_07_readout_energy_forces.tex`
- `05_deck/sections/arch_08_mattersim_pretraining_finetuning.tex`
- `05_deck/sections/arch_09_mattersim_local_protocol.tex`
- `05_deck/sections/arch_10_mace_equivariance.tex`
- `05_deck/sections/arch_11_mace_local_neighborhood.tex`
- `05_deck/sections/arch_12_mace_radial_spherical.tex`
- `05_deck/sections/arch_13_mace_spherical_harmonics_indices.tex`
- `05_deck/sections/arch_14_mace_equivariant_features.tex`
- `05_deck/sections/arch_15_mace_tensor_product.tex`
- `05_deck/sections/arch_16_mace_higher_order_messages.tex`
- `05_deck/sections/arch_17_mace_readout_energy_forces.tex`
- `05_deck/sections/arch_18_mace_finetuning_loss_weights.tex`
- `05_deck/sections/arch_19_mattersim_mace_comparison.tex`
- `05_deck/sections/arch_20_architecture_summary_before_experiments.tex`

Additional architecture source found:

- `05_deck/sections/arch_13_mace_equivariant_features.tex`

Missing:

- none for required `arch_01`-`arch_20` source files.

## Combined preview PDF/PNGs

Found:

- `06_build/main_architecture_preview.pdf`
- `06_build/architecture_preview/architecture-01.png` through `architecture-20.png`

Missing:

- none for combined architecture preview PDF/PNGs.

## Individual previews

Found:

- `06_build/main_arch_01_preview.pdf` through `main_arch_20_preview.pdf`
- `06_build/arch_01_preview/arch_01.png` through `arch_20_preview/arch_20.png`

Missing:

- none for individual architecture previews.

## Optional content docs

Found:

- `03_content/deck_status.md`
- `03_content/parallel_slide_workflow.md`
- `03_content/gpt_slide_handoff.md`
- `03_content/outline.md`
- `03_content/slides.md`
- `03_content/speaker_notes.md`
- `03_content/claims_to_verify.md`

Missing:

- none for the optional content docs that were present in the project.

## Assets folders

The requested asset folders exist:

- `04_assets/figures/`
- `04_assets/tables/`
- `04_assets/screenshots/`
- `04_assets/logos/`

No asset files were present in those folders at the time of packaging.

## Fonts

Binary font files are present locally in `PRESENTATION/02_template/hse_beamer/font/HSE_Sans/`, but they were intentionally excluded from the new-chat zip.

Added note:

- `PRESENTATION/02_template/hse_beamer/README_FONT_NOTE_FOR_NEW_CHAT.md`

Reason:

- binary font files should remain local for Codex/LaTeX builds on the user machine and should not be uploaded to the new chat handoff zip.

## Exclusions applied

The zip-building step excludes:

- raw datasets;
- checkpoints;
- model weights;
- `.pt`, `.pth`, `.ckpt`, `.model`;
- huge training folders;
- LaTeX aux/log/nav/toc/snm/out except needed PDFs/PNGs;
- binary font files (`.otf`, `.ttf`, `.woff`, `.woff2`);
- `.DS_Store`;
- `__pycache__`.
