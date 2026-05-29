# Coursework Context Bundle (20260511)

Sanitized lightweight context collected for pipeline/Q&A from `repo/coursework` plus existing small `for_gpt` summaries.

## Contents

- `directory_tree/`: 1 files
- `log_snippets/`: 160 files
- `metrics/`: 183 files
- `notebooks_or_exports/`: 2 files
- `scripts/`: 50 files
- `slurm/`: 43 files
- `summaries/`: 6 files

## Safety Rules Applied

- Did not copy raw structure/data/model/checkpoint extensions: `.xyz`, `.cfg`, `.extxyz`, `.traj`, `.db`, `.pt`, `.pth`, `.ckpt`, `.model`, checkpoint/best-model names.
- Did not copy raw logs wholesale; generated short markdown snippets in `log_snippets/`.
- Replaced local home-directory prefixes with `<USER_HOME>` in copied/generated text where parsed.
- Replaced obvious SLURM account directives with `<SLURM_ACCOUNT>`.
- Directory tree uses relative paths only, depth <= 4, excluding raw/heavy/cache paths.

See `COURSEWORK_CONTEXT_MANIFEST_20260511.md` and `COURSEWORK_CONTEXT_EXCLUDED_FILES_20260511.md` for audit details.
