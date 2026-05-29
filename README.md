# Curated Coursework Repository

This repo is curated for report/review/provenance. It is a maximal curated clean repo: it keeps final verified metrics, selected supporting tables, provenance snapshots, useful scripts, figures, presentation artifacts, and archive context needed to review the coursework.

It does not include raw datasets, model weights, checkpoints, full retraining assets, heavy archives, local binaries, nested repositories, or build outputs. Excluded heavy and external artifacts are documented in `provenance/source_manifests/`.

Final numeric authority for the report is represented by the verified CSV files in `results/verified_metrics/` and by the curated summary in `docs/results_summary.md`. Older contexts are stored only as archive/provenance material.

## Quick Map

- `docs/`: curated Russian documentation for report writing and review.
- `results/`: verified metrics, supporting tables, figures, and sanity checks.
- `provenance/`: source chains, log snippets, slurm scripts, manifests, and checksums.
- `src/mlip_benchmark/`: lightweight curated helpers plus `source_mirror/` with provenance-oriented coursework scripts.
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
