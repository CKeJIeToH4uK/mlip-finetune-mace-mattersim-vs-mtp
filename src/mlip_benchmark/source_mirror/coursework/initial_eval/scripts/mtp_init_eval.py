#!/usr/bin/env python
# coding: utf-8

import json
import numpy as np
from mpi4py import MPI
from mlip_4 import LossFunction, RadialBasisCinf, MTP

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

BASE = "~/coursework"
TRAIN_DB_PATH = f"{BASE}/databases/train_300K_from_xyz.json"
VALID_DB_PATH = f"{BASE}/databases/test_300K_from_xyz.json"

OUT_DIR = f"{BASE}/initial_eval/results/mtp_init"
OUT_JSON = f"{OUT_DIR}/mtp_init_eval.json"
OUT_POT = f"{OUT_DIR}/mtp_init_level20.json"

# ВАЖНО:
# если это тот же H/C/N/O датасет, оставляй [1, 6, 7, 8]
# если другой датасет, поменяй числа
species_order = [1, 6, 7, 8]

# ---------- load train ----------
train_bytes = b""
if rank == 0:
    with open(TRAIN_DB_PATH, "rb") as f:
        train_bytes = f.read()
train_bytes = comm.bcast(train_bytes, root=0)
loss_train = LossFunction.from_json_bytes(train_bytes, True)

# ---------- load valid ----------
valid_bytes = b""
if rank == 0:
    with open(VALID_DB_PATH, "rb") as f:
        valid_bytes = f.read()
valid_bytes = comm.bcast(valid_bytes, root=0)
loss_valid = LossFunction.from_json_bytes(valid_bytes, True)

# ---------- create random initial potential ----------
pot_bytes = b""
if rank == 0:
    np.random.seed(42)
    rb = RadialBasisCinf(size=8, min_dist=1.0, cutoff=5.0)
    pot = MTP(rb, species_order, level=20, jit=True)
    pot.params[:] = np.random.uniform(low=-1e-3, high=1e-3, size=len(pot.params))
    pot_bytes = pot.to_json_bytes()

    with open(OUT_POT, "wb") as f:
        f.write(pot_bytes)

pot_bytes = comm.bcast(pot_bytes, root=0)
pot = MTP.from_json_bytes(pot_bytes)

# ---------- errors: train ----------
loss_train.attach_pot(pot)
loss_train.calc()
train_errors = loss_train.calc_errors()

# ---------- errors: valid ----------
loss_valid.attach_pot(pot)
loss_valid.calc()
valid_errors = loss_valid.calc_errors()

if rank == 0:
    result = {
        "model": "MTP_init_random",
        "level": 20,
        "seed": 42,
        "species_order": species_order,
        "train_db": TRAIN_DB_PATH,
        "valid_db": VALID_DB_PATH,
        "train_errors": str(train_errors),
        "valid_errors": str(valid_errors),
        "potential_file": OUT_POT,
    }

    print("TRAIN:", train_errors)
    print("VALID:", valid_errors)

    with open(OUT_JSON, "w") as f:
        json.dump(result, f, indent=2)
