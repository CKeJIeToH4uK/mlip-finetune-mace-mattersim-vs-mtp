# Results Summary

This document maps where curated result materials live. It does not replace `external build-context `text_coursework/RESULTS_SOURCE_OF_TRUTH.md``.

## Numeric Authority

Final numeric authority for report writing is:

1. `external build-context `text_coursework/RESULTS_SOURCE_OF_TRUTH.md``;
2. system-specific verified CSV files in this clean repo:
   - `results/verified_metrics/organic_metrics_verified_20260511.csv`;
   - `results/verified_metrics/h2o_metrics_verified_20260511.csv`;
   - `results/verified_metrics/monbtavw_metrics_verified_20260511.csv`;
   - `results/verified_metrics/monbtavw_metrics_verified_20260511_annotated.csv` for row-level `metric_status` only.

## Handoff/Support Tables

`provenance/handoff_tables/final_metrics_long.csv` and `provenance/handoff_tables/final_metrics_wide.csv` are copied handoff/support tables from the final context. They are useful for provenance and cross-checking, but they are not complete final source-of-truth tables and should not override the system-specific verified CSV files.

## Sanity Checks

- `results/sanity_checks/ensemble_aggregates_verified_20260511.csv`: MTP ensemble sanity check for organic 300K only.

## Claim Discipline

Allowed claims are metric-specific and table-backed. Broad model-family generalizations, performance-cost claims, and long-trajectory stability claims are outside the clean repo source-of-truth.
