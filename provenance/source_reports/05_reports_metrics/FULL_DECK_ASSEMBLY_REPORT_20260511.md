# Full Deck Assembly Report — 2026-05-11

## 1. Block list

| order | block | source |
|---:|---|---|
| 1 | Pre-architecture | `PRESENTATION/05_deck/sections/00_prearchitecture.tex` |
| 2 | Architecture | `PRESENTATION/05_deck/sections/03_methods_architecture.tex` |
| 3 | Results intro | `PRESENTATION/05_deck/sections/04_results_intro.tex` |
| 4 | Organic | `PRESENTATION/05_deck/sections/05_organic_results.tex` |
| 5 | H2O | `PRESENTATION/05_deck/sections/06_h2o_results.tex` |
| 6 | MoNbTaVW | `PRESENTATION/05_deck/sections/07_monbtavw_results.tex` |
| 7 | Summary / Q&A | `PRESENTATION/05_deck/sections/08_summary_closing.tex` |
| 8 | Backup / Appendix | `PRESENTATION/05_deck/sections/09_backup_appendix.tex` |

## 2. Expected page count by block

| block | expected pages |
|---|---:|
| Pre-architecture | 2 |
| Architecture | 20 |
| Results intro | 1 |
| Organic | 4 |
| H2O | 3 |
| MoNbTaVW | 5 |
| Summary / Q&A | 3 |
| Backup / Appendix | 5 |
| **Total** | **43** |

## 3. Missing files

None. All required block files exist.

Recursive section precheck covered 51 `.tex` files included by the requested blocks.

## 4. Missing figures

None. All 21 detected `\includegraphics{...}` references in the requested block tree resolve to existing files.

## 5. Build can proceed

Yes. No required block, recursive input, or referenced figure is missing.

## 6. Build result

Build status: PASS.

Created:

- `PRESENTATION/05_deck/main_full_deck_preview.tex`
- `PRESENTATION/06_build/main_full_deck_preview.pdf`
- `PRESENTATION/06_build/full_deck_preview/full_deck-01.png` ... `full_deck-43.png`

Actual page count: 43.

| block | expected pages | actual pages | page range | status |
|---|---:|---:|---|---|
| Pre-architecture | 2 | 2 | 1-2 | PASS |
| Architecture | 20 | 20 | 3-22 | PASS |
| Results intro | 1 | 1 | 23 | PASS |
| Organic | 4 | 4 | 24-27 | PASS |
| H2O | 3 | 3 | 28-30 | PASS |
| MoNbTaVW | 5 | 5 | 31-35 | PASS |
| Summary / Q&A | 3 | 3 | 36-38 | PASS |
| Backup / Appendix | 5 | 5 | 39-43 | PASS |
| **Total** | **43** | **43** | 1-43 | **PASS** |

No page-count discrepancy was found.

## 7. Integration fixes applied

- Added `booktabs` to the separate full preview source so accepted backup tables using `\toprule` build inside the full deck.
- Rebuilt backup B1 image as a sanitized workflow map after Round 1 compliance review flagged visible slash-delimited path strings.
- Applied terminology-only Round 1 text fixes for visible `MoNbTaVW` / `MACE default` wording and summary language. No data, result values, raw datasets, checkpoints, model weights, source archives, or `results_handoff/*` files were modified.
- Removed the manual `23.` prefix from the results intro title after final numbering review. The footer remains the source of actual slide/page numbering.
