#!/usr/bin/env python3
"""Create lightweight Markdown previews from curated CSV tables."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIRS = [ROOT / 'report_assets' / 'tables', ROOT / 'results' / 'tables']
for out_dir in OUTPUT_DIRS:
    out_dir.mkdir(parents=True, exist_ok=True)

for path in sorted((ROOT / 'results' / 'verified_metrics').glob('*.csv')):
    with path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    preview = rows[:8]
    if not preview:
        continue
    md = [
        '| ' + ' | '.join(preview[0]) + ' |',
        '| ' + ' | '.join(['---'] * len(preview[0])) + ' |',
    ]
    for row in preview[1:]:
        md.append('| ' + ' | '.join(row) + ' |')
    content = '\n'.join(md) + '\n'
    for out_dir in OUTPUT_DIRS:
        target = out_dir / (path.stem + '.md')
        target.write_text(content, encoding='utf-8')
        print(f'wrote {target.relative_to(ROOT)}')
