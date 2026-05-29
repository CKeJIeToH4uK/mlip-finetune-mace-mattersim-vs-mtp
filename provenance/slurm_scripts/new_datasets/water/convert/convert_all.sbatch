#!/bin/bash
#SBATCH -J water_convert
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=01:00:00
#SBATCH -o %x_%j.out

set -euo pipefail

source ~/mlip4_env.sh

BASE="/home/brmannanov/coursework/new_datasets"
DATA="$BASE/data"
SCRIPTS="$BASE/water/convert"
OUT="$BASE/water/convert"

# 1) cfg -> xyz (for MACE / MatterSim)
echo "=== cfg -> xyz ==="
python "$SCRIPTS/cfg_to_xyz.py" \
  "$DATA/train_H2O.cfg" "$OUT/train_H2O.xyz" \
  --type2z "0:1,1:8"

python "$SCRIPTS/cfg_to_xyz.py" \
  "$DATA/valid_H2O.cfg" "$OUT/valid_H2O.xyz" \
  --type2z "0:1,1:8"

# 2) xyz -> mlip-4 json (for MTP)
echo "=== xyz -> mtp json ==="
python "$SCRIPTS/xyz_to_mtp_json.py" \
  --input_xyz "$OUT/train_H2O.xyz" \
  --output_json "$OUT/train_H2O.json"

python "$SCRIPTS/xyz_to_mtp_json.py" \
  --input_xyz "$OUT/valid_H2O.xyz" \
  --output_json "$OUT/valid_H2O.json"

echo "=== Done ==="
ls -lh "$OUT"/train_H2O.* "$OUT"/valid_H2O.*
