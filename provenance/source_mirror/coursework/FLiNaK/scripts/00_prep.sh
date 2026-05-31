#!/bin/bash
# Стадия 0: конвертация train.json -> xyz + split 90/10.
# Запускать один раз локально или на кластере (GPU не нужен).
#
# Идемпотентно: при повторном запуске перезапишет xyz-файлы, ничего не сломает.
# Чистить ничего не надо даже при рестарте.

set -euo pipefail

BASE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE"

if [[ ! -f data/train.json ]]; then
  echo "ERROR: data/train.json не найден. Положи файл от Новикова в data/train.json"
  exit 1
fi

python3 scripts/json_to_xyz_split.py \
  --input data/train.json \
  --out-all data/train_all.xyz \
  --out-train data/train_90.xyz \
  --out-valid data/valid_10.xyz \
  --valid-fraction 0.10 \
  --seed 42

echo "OK: prep done"
