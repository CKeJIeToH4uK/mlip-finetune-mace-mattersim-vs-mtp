# Source Manifests

The CSV files in this directory are canonical for clean repo provenance.

- `included_manifest.csv`: copied/generated clean repo artifacts, excluding control files that would create circular manifest semantics.
- `excluded_heavy_manifest.csv`: raw datasets, checkpoints, model weights, build outputs, binaries, and other heavy artifacts intentionally not copied physically.
- `archive_external_manifest.csv`: old contexts, external zones, education folders, archives, and reference-only materials not copied wholesale.

## Self-Reference Exceptions

Manifest CSV files may be absent from `included_manifest.csv`; this is intentional to avoid self-referential manifest rows. `checksums.sha256` intentionally excludes itself. It includes manifest CSVs and regular copied/generated artifacts.

## Canonical Schema

The current CSV headers are canonical for this clean repo. Earlier build-plan field names such as `kind`, `archive_status`, or `replacement_reference` are represented by the current `category`, `artifact_type`, `possible_relevance`, `reason_not_copied`, and `notes` columns where applicable.
