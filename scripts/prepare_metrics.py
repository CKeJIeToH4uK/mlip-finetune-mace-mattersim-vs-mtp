#!/usr/bin/env python3
"""List curated metric tables and their row counts."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
for path in sorted((ROOT / 'results').rglob('*.csv')):
    with path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    count = max(len(rows) - 1, 0)
    print(f"{path.relative_to(ROOT)}	{count} data rows")
