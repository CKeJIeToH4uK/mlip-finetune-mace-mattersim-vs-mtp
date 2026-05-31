"""List curated figure assets without regenerating plots."""
from pathlib import Path


def list_figures(repo_root: Path):
    return sorted((repo_root / "report_assets" / "figures").glob("*"))
