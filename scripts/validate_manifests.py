#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'provenance' / 'source_manifests' / 'included_manifest.csv'
EXCLUDED = ROOT / 'provenance' / 'source_manifests' / 'excluded_heavy_manifest.csv'
ARCHIVE = ROOT / 'provenance' / 'source_manifests' / 'archive_external_manifest.csv'
CHECKSUMS = ROOT / 'provenance' / 'checksums' / 'checksums.sha256'

HEAVY_EXTS = {'.pth', '.pt', '.ckpt', '.model', '.pb'}
JUNK_NAMES = {'.DS_Store'}
JUNK_PARTS = {'__pycache__', '.ipynb_checkpoints', '.git'}
LOCAL_ONLY_PARTS = {'local_edit_logs'}
HEAVY_PARTS = {'checkpoints', 'build'}

def sha256_file(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def rows(path):
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    errors = []
    for path in [MANIFEST, EXCLUDED, ARCHIVE, CHECKSUMS]:
        if not path.exists():
            errors.append(f'missing required file: {path.relative_to(ROOT)}')

    included = rows(MANIFEST) if MANIFEST.exists() else []
    included_paths = {r['clean_path'] for r in included}

    for file in ROOT.rglob('*'):
        if not file.is_file():
            continue
        rel = file.relative_to(ROOT).as_posix()
        parts = set(file.relative_to(ROOT).parts)
        if '.git' in parts:
            continue
        if parts & LOCAL_ONLY_PARTS:
            continue
        if rel in {
            'provenance/source_manifests/included_manifest.csv',
            'provenance/source_manifests/excluded_heavy_manifest.csv',
            'provenance/source_manifests/archive_external_manifest.csv',
            'provenance/checksums/checksums.sha256',
        }:
            continue
        if rel not in included_paths:
            errors.append(f'file missing from included_manifest: {rel}')
        if file.suffix in HEAVY_EXTS:
            errors.append(f'heavy/model extension copied: {rel}')
        if file.name in JUNK_NAMES or parts & JUNK_PARTS:
            errors.append(f'junk/cache copied: {rel}')
        if parts & HEAVY_PARTS:
            errors.append(f'heavy/build directory copied: {rel}')

    for r in included:
        p = ROOT / r['clean_path']
        if not p.exists():
            errors.append(f'included_manifest path missing on disk: {r["clean_path"]}')
        elif r.get('sha256') and len(r['sha256']) == 64 and sha256_file(p) != r['sha256']:
            errors.append(f'sha mismatch for {r["clean_path"]}')
        if p.suffix == '.ipynb' and not r.get('notebook_role'):
            errors.append(f'notebook missing notebook_role: {r["clean_path"]}')

    local_path_patterns = [
        '/' + 'Users' + '/' + 'bulat',
        '/' + 'Users' + '/',
        '/' + 'home' + '/' + 'brmannanov',
    ]
    scan_roots = [ROOT/'README.md', ROOT/'PROJECT_STRUCTURE.md', ROOT/'REPRODUCIBILITY.md', ROOT/'docs', ROOT/'src', ROOT/'scripts']
    for base in scan_roots:
        paths = [base] if base.is_file() else list(base.rglob('*')) if base.exists() else []
        for p in paths:
            if p.is_file() and p.suffix.lower() in {'.md', '.py', '.sh', '.txt', '.sbatch'}:
                text = p.read_text(encoding='utf-8', errors='ignore')
                for pattern in local_path_patterns:
                    if pattern in text:
                        errors.append(f'hardcoded local path in runnable/docs: {p.relative_to(ROOT)}')
                        break

    if not rows(EXCLUDED):
        errors.append('excluded_heavy_manifest is empty')
    if not rows(ARCHIVE):
        errors.append('archive_external_manifest is empty')

    if errors:
        for e in errors:
            print('ERROR:', e)
        return 1
    print('validate_manifests: OK')
    return 0

if __name__ == '__main__':
    sys.exit(main())
