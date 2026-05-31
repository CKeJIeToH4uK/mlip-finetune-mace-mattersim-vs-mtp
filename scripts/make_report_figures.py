#!/usr/bin/env python3
"""Generate final report figures from verified CSV files."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results" / "verified_metrics"
FIGURES = ROOT / "text_coursework" / "final_report_work" / "figures"

ORGANIC = DATA / "organic_metrics_verified_20260511.csv"
H2O = DATA / "h2o_metrics_verified_20260511.csv"
MONBTAVW = DATA / "monbtavw_metrics_verified_20260511.csv"

TEMPS = ["300K", "600K", "1200K"]
ORGANIC_MODELS = ["MatterSim", "MACE", "MTP-16", "MTP-20"]
MAIN_MODELS = ["MatterSim", "MACE", "MTP-16", "MTP-20"]
MONBTAVW_MAIN = ["MatterSim", "MACE default", "MACE-EW50", "MTP-16", "MTP-20"]

COLORS = {
    "MatterSim": "#1f77b4",
    "MACE": "#2ca02c",
    "MACE default": "#2ca02c",
    "MACE-EW50": "#17becf",
    "MTP-16": "#d62728",
    "MTP-20": "#ff7f0e",
}
MARKERS = {
    "MatterSim": "o",
    "MACE": "s",
    "MACE default": "s",
    "MACE-EW50": "D",
    "MTP-16": "^",
    "MTP-20": "d",
}


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.edgecolor": "#555555",
            "axes.linewidth": 0.8,
            "axes.grid": True,
            "grid.color": "#dddddd",
            "grid.linewidth": 0.6,
            "grid.alpha": 0.9,
            "legend.frameon": False,
            "xtick.direction": "out",
            "ytick.direction": "out",
        }
    )


def save(fig: plt.Figure, output_name: str) -> Path:
    FIGURES.mkdir(parents=True, exist_ok=True)
    output = FIGURES / f"{output_name}.pdf"
    fig.savefig(output, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    return output


def organic_line(metric: str, ylabel: str, output_name: str) -> Path:
    df = pd.read_csv(ORGANIC)
    fig, ax = plt.subplots(figsize=(6.9, 3.7))
    for model in ORGANIC_MODELS:
        part = (
            df[df["model_label"] == model]
            .set_index("test_temperature")
            .loc[TEMPS]
            .reset_index()
        )
        ax.plot(
            TEMPS,
            part[metric],
            label=model,
            color=COLORS[model],
            marker=MARKERS[model],
            linewidth=1.8,
            markersize=5,
        )
    ax.set_xlabel("Температура тестового разбиения")
    ax.set_ylabel(ylabel)
    ax.legend(loc="upper left")
    ax.margins(x=0.08)
    fig.tight_layout()
    return save(fig, output_name)


def organic_relative_forces() -> Path:
    df = pd.read_csv(ORGANIC)
    base = (
        df[df["model_label"] == "MTP-20"]
        .set_index("test_temperature")
        .loc[TEMPS]["forces_mae_meV_A"]
    )
    fig, ax = plt.subplots(figsize=(6.9, 3.7))
    for model in ["MatterSim", "MACE"]:
        values = (
            df[df["model_label"] == model]
            .set_index("test_temperature")
            .loc[TEMPS]["forces_mae_meV_A"]
            / base
        )
        ax.plot(
            TEMPS,
            values,
            label=model,
            color=COLORS[model],
            marker=MARKERS[model],
            linewidth=1.8,
            markersize=5,
        )
    ax.axhline(
        1.0,
        color="#777777",
        linestyle=(0, (4, 4)),
        linewidth=1.2,
        zorder=0,
    )
    ax.set_xlabel("Температура тестового разбиения")
    ax.set_ylabel("Относительная MAE по силам")
    ax.set_ylim(0.0, 1.05)
    ax.text(
        0.98,
        0.95,
        "MTP-20 = 1",
        transform=ax.transAxes,
        ha="right",
        va="top",
        color="#555555",
        fontsize=10,
    )
    ax.legend(loc="upper left")
    ax.margins(x=0.08)
    fig.tight_layout()
    return save(fig, "results_organic_forces_mae_relative_mtp20")


def two_panel_bars(csv_path: Path, metrics: tuple[str, str], ylabels: tuple[str, str], output_name: str) -> Path:
    df = pd.read_csv(csv_path).set_index("model_label").loc[MAIN_MODELS].reset_index()
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.6))
    for ax, metric, ylabel in zip(axes, metrics, ylabels, strict=True):
        colors = [COLORS[m] for m in df["model_label"]]
        ax.bar(df["model_label"], df[metric], color=colors, width=0.62)
        ax.set_ylabel(ylabel)
        ax.tick_params(axis="x", rotation=25)
        ax.set_axisbelow(True)
    fig.tight_layout(w_pad=2.0)
    return save(fig, output_name)


def monbtavw_bar(metric: str, ylabel: str, output_name: str) -> Path:
    df = pd.read_csv(MONBTAVW).set_index("model_label").loc[MONBTAVW_MAIN].reset_index()
    fig, ax = plt.subplots(figsize=(6.9, 3.7))
    colors = [COLORS[m] for m in df["model_label"]]
    ax.bar(df["model_label"], df[metric], color=colors, width=0.62)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=20)
    ax.set_axisbelow(True)
    fig.tight_layout()
    return save(fig, output_name)


FIGURE_BUILDERS = {
    "results_organic_energy_mae": (
        ORGANIC,
        lambda: organic_line("energy_mae_meV_atom", "MAE по энергии, meV/atom", "results_organic_energy_mae"),
    ),
    "results_organic_forces_mae": (
        ORGANIC,
        lambda: organic_line("forces_mae_meV_A", "MAE по силам, meV/Å", "results_organic_forces_mae"),
    ),
    "results_organic_forces_mae_relative_mtp20": (
        ORGANIC,
        organic_relative_forces,
    ),
    "results_h2o_mae_bars": (
        H2O,
        lambda: two_panel_bars(
            H2O,
            ("energy_mae_meV_atom", "forces_mae_meV_A"),
            ("Energy MAE, meV/atom", "Forces MAE, meV/Å"),
            "results_h2o_mae_bars",
        ),
    ),
    "results_monbtavw_energy_mae": (
        MONBTAVW,
        lambda: monbtavw_bar("energy_mae_meV_atom", "Energy MAE, meV/atom", "results_monbtavw_energy_mae"),
    ),
    "results_monbtavw_forces_mae": (
        MONBTAVW,
        lambda: monbtavw_bar("forces_mae_meV_A", "Forces MAE, meV/Å", "results_monbtavw_forces_mae"),
    ),
    "appendix_organic_energy_rmse": (
        ORGANIC,
        lambda: organic_line("energy_rmse_meV_atom", "Energy RMSE, meV/atom", "appendix_organic_energy_rmse"),
    ),
    "appendix_organic_forces_rmse": (
        ORGANIC,
        lambda: organic_line("forces_rmse_meV_A", "Forces RMSE, meV/Å", "appendix_organic_forces_rmse"),
    ),
    "appendix_h2o_rmse_bars": (
        H2O,
        lambda: two_panel_bars(
            H2O,
            ("energy_rmse_meV_atom", "forces_rmse_meV_A"),
            ("Energy RMSE, meV/atom", "Forces RMSE, meV/Å"),
            "appendix_h2o_rmse_bars",
        ),
    ),
    "appendix_monbtavw_energy_rmse": (
        MONBTAVW,
        lambda: monbtavw_bar("energy_rmse_meV_atom", "Energy RMSE, meV/atom", "appendix_monbtavw_energy_rmse"),
    ),
    "appendix_monbtavw_forces_rmse": (
        MONBTAVW,
        lambda: monbtavw_bar("forces_rmse_meV_A", "Forces RMSE, meV/Å", "appendix_monbtavw_forces_rmse"),
    ),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("figure", choices=sorted(FIGURE_BUILDERS))
    args = parser.parse_args()
    setup_style()
    source, builder = FIGURE_BUILDERS[args.figure]
    output = builder()
    print(f"{args.figure}: source={source.relative_to(ROOT)} output={output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
