from pathlib import Path
import re
from collections import Counter

def first_cfg_types(path):
    txt = Path(path).read_text(errors="ignore")
    # берём первый блок AtomData:
    m = re.search(r"AtomData:.*?\n(.*?)\n\s*END_CFG", txt, flags=re.S)
    block = m.group(1)
    types = []
    for line in block.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0].isdigit():
            types.append(int(parts[1]))
    return Counter(types)

def first_xyz_species(path):
    lines = Path(path).read_text(errors="ignore").splitlines()
    n = int(lines[0].strip())
    # в extxyz первый столбец обычно species
    species = [lines[2+i].split()[0] for i in range(n)]
    return Counter(species)

cfg_c = first_cfg_types("databases/train_300K.cfg")
xyz_c = first_xyz_species("databases/train_300K.xyz")
print("CFG type counts:", cfg_c)
print("XYZ species counts:", xyz_c)
