# Curated Coursework Repository

This repo is curated for report/review/provenance. It is a maximal curated clean repo: it keeps final verified metrics, selected supporting tables, provenance snapshots, curated helper scripts, figures, presentation artifacts, and archive context needed to review the coursework.

It does not include raw datasets, model weights, checkpoints, full retraining assets, heavy archives, local binaries, nested repositories, or build outputs. Excluded heavy and external artifacts are documented in `provenance/source_manifests/`.

Final numeric authority for the report is `external build-context `text_coursework/RESULTS_SOURCE_OF_TRUTH.md`` plus the system-specific verified CSV files in `results/verified_metrics/`: organic-датасет, H2O, and MoNbTaVW. Handoff tables under `provenance/handoff_tables/` are provenance/support material, not complete final source-of-truth.

Core systems and models represented here: organic-датасет, H2O, MoNbTaVW; MTP, MACE, MatterSim, and MoNbTaVW energy-weighted MACE protocol rows.

See also: `PROJECT_STRUCTURE.md` for layout and `REPRODUCIBILITY.md` for what can and cannot be reproduced from this clean repo.

## Quick Map

- `docs/`: curated Russian documentation for report writing and review.
- `results/`: system-specific verified metrics, supporting tables, figures, and sanity checks.
- `provenance/`: source chains, handoff tables, source mirror, log snippets, slurm scripts, manifests, and checksums.
- `src/mlip_benchmark/`: lightweight curated helper modules only.
- `scripts/`: validation and convenience scripts for this clean repo.
- `presentation_archive/`: final deck and selected presentation support material.
- `archive/`: old contexts and excluded branches kept away from final numeric authority.

## Validation

Run:

```bash
python scripts/validate_manifests.py
python scripts/validate_results.py
```

The scripts validate manifest coverage, excluded artifacts, required metric files, terminology guardrails, and checksum consistency for copied materials.
