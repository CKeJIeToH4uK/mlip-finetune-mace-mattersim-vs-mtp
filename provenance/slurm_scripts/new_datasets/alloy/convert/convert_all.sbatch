#!/bin/bash
#SBATCH -J alloy_convert
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=00:30:00
#SBATCH -o %x_%j.out

set -euo pipefail

source ~/mlip4_env.sh

BASE="/home/brmannanov/coursework/new_datasets"
DATA="$BASE/data"
OUT="$BASE/alloy/convert"

# 1) Fix types: remap 0-4 -> atomic numbers (for MTP)
echo "=== fix types ==="
python "$BASE/alloy/convert/fix_types.py" \
  "$DATA/MoNbTaVW_train.json" "$OUT/train_alloy.json"
python "$BASE/alloy/convert/fix_types.py" \
  "$DATA/MoNbTaVW_valid.json" "$OUT/valid_alloy.json"

# 2) json -> xyz (for MACE / MatterSim)
# type mapping: 0=V(23), 1=Nb(41), 2=Mo(42), 3=Ta(73), 4=W(74)
echo "=== json -> xyz ==="
python "$BASE/alloy/convert/mtp_json_to_xyz.py" \
  "$DATA/MoNbTaVW_train.json" "$OUT/train_alloy.xyz"
python "$BASE/alloy/convert/mtp_json_to_xyz.py" \
  "$DATA/MoNbTaVW_valid.json" "$OUT/valid_alloy.xyz"

echo "=== Done ==="
ls -lh "$OUT"/*.xyz
