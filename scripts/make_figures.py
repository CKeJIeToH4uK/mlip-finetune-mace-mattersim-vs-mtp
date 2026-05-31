#!/usr/bin/env python3
"""List curated figure assets for report selection without regenerating plots."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for path in sorted((ROOT / 'report_assets' / 'figures').glob('*')):
    if path.is_file():
        print(path.relative_to(ROOT))
