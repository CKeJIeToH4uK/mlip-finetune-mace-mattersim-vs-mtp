#!/usr/bin/env python3
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'results/verified_metrics/organic_metrics_verified_20260511.csv',
    'results/verified_metrics/h2o_metrics_verified_20260511.csv',
    'results/verified_metrics/monbtavw_metrics_verified_20260511.csv',
    'results/verified_metrics/final_metrics_long.csv',
    'results/verified_metrics/final_metrics_wide.csv',
    'results/sanity_checks/ensemble_aggregates_verified_20260511.csv',
]

def read_text(path):
    return path.read_text(encoding='utf-8', errors='ignore')

def main():
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f'missing required metric table: {rel}')

    for rel in ['results/verified_metrics/h2o_metrics_verified_20260511.csv', 'results/verified_metrics/monbtavw_metrics_verified_20260511.csv']:
        path = ROOT / rel
        if path.exists():
            text = read_text(path)
            if re.search(r'(^|[,;\s])test([,;\s]|$)', text, re.IGNORECASE):
                errors.append(f'validation table uses reserved split wording: {rel}')

    summary = ROOT / 'docs' / 'results_summary.md'
    if summary.exists():
        text = read_text(summary)
        guarded = [
            'универсальные модели всегда ' + 'лучше',
            'cost-' + 'efficiency',
            'run' + 'time',
            '3' + 'BPA',
            'MTP-' + '24',
            'QM' + '7b',
            'ET' + 'N',
        ]
        for term in guarded:
            if term in text:
                errors.append(f'guarded phrase appears in results summary: {term}')

    if errors:
        for e in errors:
            print('ERROR:', e)
        return 1
    print('validate_results: OK')
    return 0

if __name__ == '__main__':
    sys.exit(main())
