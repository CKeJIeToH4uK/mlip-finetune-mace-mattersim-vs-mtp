#!/usr/bin/env python
# coding: utf-8

import csv
import fnmatch
import hashlib
import json
import shutil
import zipfile
from pathlib import Path


COURSEWORK = Path(__file__).resolve().parents[1]
SOURCE = COURSEWORK / "new_datasets/alloy/mace_ablation_normal_protocols_20260509"
BUNDLE_NAME = "protocols_eval_addendum_20260510"
OUT_DIR = COURSEWORK / "presentation_handoff" / BUNDLE_NAME
ZIP_PATH = COURSEWORK / "presentation_handoff" / f"{BUNDLE_NAME}.zip"
SOURCE_PREFIX = Path("sources/mace_ablation_normal_protocols_20260509")

RUNS = {
    "stage2_normal": {
        "protocol": "stage-two/SWA energy convergence",
        "interpretation": "stage-two did not fix energy; energy metrics close to bad default/fair200.",
    },
    "lora_ew10_normal": {
        "protocol": "LoRA, energy_weight=10, forces_weight=100",
        "interpretation": "energy RMSE close to EW50, but forces much worse; good backup/tradeoff, not main.",
    },
    "freeze1_ew10_normal": {
        "protocol": "partial freeze=1, energy_weight=10, forces_weight=100",
        "interpretation": "close to EW10; good forces; does not beat EW50 on energy RMSE.",
    },
}

EXPECTED = {
    ("stage2_normal", "valid"): (38.751, 86.227, 63.911, 114.005),
    ("stage2_normal", "train"): (37.247, 87.967, 59.347, 86.017),
    ("lora_ew10_normal", "valid"): (17.339, 33.508, 81.404, 129.083),
    ("lora_ew10_normal", "train"): (18.013, 41.801, 78.906, 115.290),
    ("freeze1_ew10_normal", "valid"): (11.985, 38.468, 62.321, 114.110),
    ("freeze1_ew10_normal", "train"): (10.590, 36.187, 56.850, 82.480),
}

ROOT_PATTERNS = [
    "train_eval_protocols_normal.sbatch",
    "eval_mace_alloy.py",
    "collect_protocols_normal.py",
    "README_RUN.md",
    "run_status_*.tsv",
    "alloy_protocols_norm_*.out",
]

RUN_PATTERNS = [
    "eval_train.json",
    "eval_valid.json",
    "eval_metrics.csv",
    "train.log",
    "train_*.log",
    "eval_*.log",
    "resources_*.txt",
    "exact_command_*.txt",
    "logs/*.log",
    "results/*_train.txt",
]

FORBIDDEN_NAMES = {".DS_Store", "__MACOSX"}
FORBIDDEN_DIRS = {"checkpoints", "models", "__pycache__", "__MACOSX"}
FORBIDDEN_SUFFIXES = {".model", ".pt", ".pth", ".png", ".pyc", ".xyz"}
RAW_DATA_NAMES = {"train_alloy.xyz", "valid_alloy.xyz"}
MAX_COPY_BYTES = 5 * 1024 * 1024

manifest = []
missing = []
skipped = []


def rel_for_manifest(path):
    return path.as_posix()


def is_forbidden(path):
    if any(part in FORBIDDEN_DIRS for part in path.parts):
        return True
    if path.name in FORBIDDEN_NAMES or path.name in RAW_DATA_NAMES:
        return True
    if path.suffix in FORBIDDEN_SUFFIXES:
        return True
    return False


def copy_one(src, rel_dst, role):
    if not src.exists():
        missing.append(f"{src.relative_to(SOURCE)}")
        return
    if not src.is_file():
        return
    if is_forbidden(src):
        skipped.append(f"forbidden: {src.relative_to(SOURCE)}")
        return
    size = src.stat().st_size
    if size > MAX_COPY_BYTES:
        skipped.append(f"too large ({size} bytes): {src.relative_to(SOURCE)}")
        return

    dst = OUT_DIR / rel_dst
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    manifest.append(
        {
            "included_path": rel_for_manifest(rel_dst),
            "source_path": str(src),
            "size_bytes": size,
            "role": role,
        }
    )


def copy_matching(base, patterns, rel_base, role):
    for pattern in patterns:
        matches = sorted(base.glob(pattern))
        if not matches:
            missing.append(f"{base.relative_to(SOURCE) / pattern if base != SOURCE else pattern}")
        for src in matches:
            if src.is_file():
                rel_src = src.relative_to(SOURCE)
                copy_one(src, rel_base / rel_src, role)


def read_eval(run, split):
    path = SOURCE / run / f"eval_{split}.json"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def metric_tuple(d):
    return (
        float(d["mae_E_per_atom_meV"]),
        float(d["rmse_E_per_atom_meV"]),
        float(d["mae_F_meV_A"]),
        float(d["rmse_F_meV_A"]),
    )


def verify_note(run, split, d):
    expected = EXPECTED.get((run, split))
    if not expected or not d:
        return "no expected reference"
    actual = metric_tuple(d)
    diffs = [abs(a - e) for a, e in zip(actual, expected)]
    if max(diffs) <= 0.05:
        return "verified against expected rounded values"
    return "check: differs from expected rounded values"


def fmt(x):
    if x is None:
        return ""
    return f"{float(x):.3f}"


def add_generated(path, role):
    full = OUT_DIR / path
    manifest.append(
        {
            "included_path": rel_for_manifest(path),
            "source_path": "generated",
            "size_bytes": full.stat().st_size,
            "role": role,
        }
    )


def write_text(rel_path, text, role):
    path = OUT_DIR / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    add_generated(rel_path, role)


def collect_metrics():
    rows_long = []
    rows_wide = []
    parsed = {}

    for run in RUNS:
        parsed[run] = {}
        for split in ["train", "valid"]:
            d = read_eval(run, split)
            parsed[run][split] = d
            if d is None:
                missing.append(f"{run}/eval_{split}.json")
                continue

            source_rel = SOURCE_PREFIX / run / f"eval_{split}.json"
            notes = verify_note(run, split, d)
            e_mae, e_rmse, f_mae, f_rmse = metric_tuple(d)

            rows_long.append(
                {
                    "run": run,
                    "protocol": RUNS[run]["protocol"],
                    "split": split,
                    "metric": "energy",
                    "mae": e_mae,
                    "rmse": e_rmse,
                    "units": "meV/atom",
                    "source_file": rel_for_manifest(source_rel),
                    "notes": notes,
                }
            )
            rows_long.append(
                {
                    "run": run,
                    "protocol": RUNS[run]["protocol"],
                    "split": split,
                    "metric": "forces",
                    "mae": f_mae,
                    "rmse": f_rmse,
                    "units": "meV/Å",
                    "source_file": rel_for_manifest(source_rel),
                    "notes": notes,
                }
            )
            rows_wide.append(
                {
                    "run": run,
                    "protocol": RUNS[run]["protocol"],
                    "split": split,
                    "energy_mae_meV_atom": e_mae,
                    "energy_rmse_meV_atom": e_rmse,
                    "forces_mae_meV_A": f_mae,
                    "forces_rmse_meV_A": f_rmse,
                    "source_file": rel_for_manifest(source_rel),
                    "notes": notes,
                }
            )

    metrics_dir = OUT_DIR / "metrics"
    metrics_dir.mkdir(parents=True, exist_ok=True)

    long_path = metrics_dir / "protocols_metrics_long.csv"
    with open(long_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run",
                "protocol",
                "split",
                "metric",
                "mae",
                "rmse",
                "units",
                "source_file",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows_long)
    add_generated(Path("metrics/protocols_metrics_long.csv"), "generated metrics")

    wide_path = metrics_dir / "protocols_metrics_wide.csv"
    with open(wide_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run",
                "protocol",
                "split",
                "energy_mae_meV_atom",
                "energy_rmse_meV_atom",
                "forces_mae_meV_A",
                "forces_rmse_meV_A",
                "source_file",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows_wide)
    add_generated(Path("metrics/protocols_metrics_wide.csv"), "generated metrics")

    return parsed


def build_summary(parsed):
    def row(run, split):
        d = parsed.get(run, {}).get(split)
        if d is None:
            return f"| {run} | {RUNS[run]['protocol']} | missing | missing | missing | missing | {RUNS[run]['interpretation']} |"
        e_mae, e_rmse, f_mae, f_rmse = metric_tuple(d)
        return (
            f"| {run} | {RUNS[run]['protocol']} | {fmt(e_mae)} | {fmt(e_rmse)} | "
            f"{fmt(f_mae)} | {fmt(f_rmse)} | {RUNS[run]['interpretation']} |"
        )

    lines = [
        "# MACE Alloy Protocol Ablations Addendum",
        "",
        "Purpose: add completed normal-queue protocol ablations for MACE fine-tuning on MoNbTaVW/alloy.",
        "",
        "Reference completed main runs from the main bundle:",
        "- MACE-EW50 valid: E MAE ≈ 11.868, E RMSE ≈ 32.623, F MAE ≈ 62.867, F RMSE ≈ 113.900.",
        "- MACE-EW10 valid: E MAE ≈ 12.437, E RMSE ≈ 39.342, F MAE ≈ 62.213, F RMSE ≈ 113.788.",
        "",
        "## Valid Metrics",
        "",
        "| run | protocol | E MAE | E RMSE | F MAE | F RMSE | interpretation |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    lines.extend(row(run, "valid") for run in RUNS)
    lines.extend(
        [
            "",
            "## Train Metrics",
            "",
            "| run | protocol | E MAE | E RMSE | F MAE | F RMSE | interpretation |",
            "|---|---|---:|---:|---:|---:|---|",
        ]
    )
    lines.extend(row(run, "train") for run in RUNS)
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Additional protocol ablations do not overturn the main recommendation: MACE-EW50 remains the preferred completed MACE alloy row.",
            "- Stage-two/SWA does not fix the energy issue.",
            "- LoRA EW10 gives strong energy improvement versus default, but its force metrics are much worse.",
            "- Freeze1 EW10 is a useful backup with good forces, but it does not beat EW50 on validation energy RMSE.",
            "- The central finding remains that explicit energy weighting is the key improvement for MACE alloy.",
        ]
    )
    write_text(Path("PROTOCOLS_SUMMARY.md"), "\n".join(lines) + "\n", "generated summary")


def build_readme():
    text = """# Protocols Eval Addendum 20260510

This is a small supplement to `final_training_bundle_20260510.zip`.

It adds completed MACE alloy protocol ablations from the normal partition:
- `stage2_normal`
- `lora_ew10_normal`
- `freeze1_ew10_normal`

This archive should not replace the main bundle. It only adds protocol-ablation evidence for the presentation builder.

The archive intentionally excludes checkpoints, model files, raw datasets, image artifacts, Python caches, and other heavy files. Do not use checkpoints or models from this addendum; only use the included JSON/CSV metrics, logs, scripts, and summaries.

Final recommendation: keep the main MACE alloy row as MACE-EW50 unless the presentation author deliberately chooses a different framing. These protocol runs are best used as backup ablations showing that loss weighting is the central improvement.
"""
    write_text(Path("README_ADDENDUM.md"), text, "generated readme")


def build_claims():
    text = """# Protocols Claims and Caveats

## Main Conclusion

- Additional protocol ablations do not overturn the main recommendation.
- MACE-EW50 remains the best main MACE alloy row from completed runs.
- Loss weighting remains the key improvement.

## Details

- Stage2/SWA does not improve energy enough.
- LoRA EW10 improves energy compared to default but hurts forces significantly.
- Freeze1 EW10 is close to EW10 and has good force metrics, but does not beat EW50 on energy RMSE.
- These protocol runs are useful as backup ablations showing that energy weighting was the central factor.
"""
    write_text(Path("PROTOCOLS_CLAIMS_AND_CAVEATS.md"), text, "generated caveats")


def build_missing_report():
    critical_missing = []
    for run in RUNS:
        for split in ["train", "valid"]:
            p = SOURCE / run / f"eval_{split}.json"
            if not p.exists():
                critical_missing.append(f"{run}/eval_{split}.json")

    lines = ["# Missing Files Report", ""]
    if critical_missing:
        lines.append("Critical eval files missing:")
        lines.extend(f"- {p}" for p in critical_missing)
    else:
        lines.append("All critical eval files are present.")

    optional_missing = sorted(set(missing) - set(critical_missing))
    if optional_missing:
        lines.extend(["", "Missing optional expected files:"])
        lines.extend(f"- {p}" for p in optional_missing)
    else:
        lines.extend(["", "No expected allowed files are missing."])

    if skipped:
        lines.extend(["", "Skipped by safety rules:"])
        lines.extend(f"- {p}" for p in sorted(set(skipped)))

    write_text(Path("missing_files_report.md"), "\n".join(lines) + "\n", "generated report")


def build_manifest():
    manifest_path = OUT_DIR / "source_manifest.tsv"
    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["included_path", "source_path", "size_bytes", "role"],
            delimiter="\t",
        )
        writer.writeheader()
        writer.writerows(manifest)
    add_generated(Path("source_manifest.tsv"), "generated manifest")


def build_checksums():
    rows = []
    for path in sorted(OUT_DIR.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(OUT_DIR)
        if rel.as_posix() == "checksums_sha256.txt":
            continue
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        rows.append(f"{h.hexdigest()}  {rel.as_posix()}")

    checksum_path = OUT_DIR / "checksums_sha256.txt"
    checksum_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    add_generated(Path("checksums_sha256.txt"), "generated checksums")


def make_zip():
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(OUT_DIR.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(OUT_DIR)
            zf.write(path, Path(BUNDLE_NAME) / rel)


def main():
    if not SOURCE.exists():
        raise SystemExit(f"Source folder not found: {SOURCE}")

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    copy_matching(SOURCE, ROOT_PATTERNS, SOURCE_PREFIX, "source root context")
    for run in RUNS:
        copy_matching(SOURCE / run, RUN_PATTERNS, SOURCE_PREFIX, f"{run} context")

    parsed = collect_metrics()
    build_readme()
    build_summary(parsed)
    build_claims()
    build_missing_report()
    build_manifest()
    build_checksums()
    make_zip()

    print("Bundle:", OUT_DIR)
    print("Zip:", ZIP_PATH)
    print("Zip size bytes:", ZIP_PATH.stat().st_size)


if __name__ == "__main__":
    main()
