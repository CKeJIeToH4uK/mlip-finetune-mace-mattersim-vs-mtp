"""Helpers for listing curated metric tables without changing numbers."""
from pathlib import Path
import csv


def list_metric_tables(repo_root: Path):
    """Return CSV metric tables included in the curated repository."""
    return sorted((repo_root / "results").rglob("*.csv"))


def table_shape(path: Path):
    """Return (rows, columns) for a CSV table, excluding the header from rows."""
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        return 0, 0
    return max(len(rows) - 1, 0), len(rows[0])
