#!/usr/bin/env python3
"""
Стадия 3: собрать все eval-json'ы в одну табличку для отчёта Полине/Новикову.

Ищет json'ы в eval/, печатает таблицу, пишет eval/summary.md.
Запускать локально или на кластере в conda env — зависимостей нет, чистый stdlib.
"""
import argparse
import json
from pathlib import Path


def load(path: Path) -> dict | None:
    if not path.exists():
        return None
    with path.open() as f:
        return json.load(f)


def fmt(x: float | None, unit: str = "", digits: int = 2) -> str:
    if x is None:
        return "—"
    return f"{x:.{digits}f}{unit}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eval-dir", default="eval", type=Path,
                    help="папка с json-метриками (относительно --base)")
    ap.add_argument("--base", default=None, type=Path,
                    help="корень FLiNaK/ (по умолчанию — родитель scripts/)")
    args = ap.parse_args()

    base = args.base or Path(__file__).resolve().parent.parent
    ed = base / args.eval_dir

    runs = {
        "zero-shot on train_all": load(ed / "zero_shot_all.json"),
        "FT (variant A, all) on train_all": load(ed / "ft_all_on_all.json"),
        "FT (variant B, split) on train_90 (train)": load(ed / "ft_split_on_train.json"),
        "FT (variant B, split) on valid_10 (honest)": load(ed / "ft_split_on_valid.json"),
    }

    header = [
        "model / dataset",
        "n_cfg",
        "RMSE E/atom meV",
        "MAE E/atom meV",
        "RMSE F meV/Å",
        "MAE F meV/Å",
        "time s",
    ]

    rows = []
    for label, r in runs.items():
        if r is None:
            rows.append([label, "—", "—", "—", "—", "—", "—"])
            continue
        rows.append([
            label,
            str(r.get("n_cfg", "—")),
            fmt((r.get("rmse_E_per_atom_eV") or 0) * 1000),
            fmt((r.get("mae_E_per_atom_eV") or 0) * 1000),
            fmt(r.get("rmse_F_meV_A")),
            fmt(r.get("mae_F_meV_A")),
            fmt(r.get("time_sec_total"), digits=1),
        ])

    # печать в консоль
    widths = [max(len(h), max(len(row[i]) for row in rows)) for i, h in enumerate(header)]
    sep = "  "
    print(sep.join(h.ljust(widths[i]) for i, h in enumerate(header)))
    print(sep.join("-" * widths[i] for i in range(len(header))))
    for row in rows:
        print(sep.join(row[i].ljust(widths[i]) for i in range(len(header))))

    # markdown summary
    md = ["# FLiNaK MatterSim FT — summary", ""]
    md.append("| " + " | ".join(header) + " |")
    md.append("|" + "|".join(["---"] * len(header)) + "|")
    for row in rows:
        md.append("| " + " | ".join(row) + " |")
    out = ed / "summary.md"
    out.write_text("\n".join(md) + "\n")
    print(f"\nsummary -> {out}")


if __name__ == "__main__":
    main()
