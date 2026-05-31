"""Repository path helpers."""
from pathlib import Path


def repo_root_from_file(path: Path) -> Path:
    """Find the clean repo root from a file located inside it."""
    path = path.resolve()
    for candidate in [path, *path.parents]:
        if (candidate / "README.md").exists() and (candidate / "provenance").exists():
            return candidate
    raise RuntimeError("clean repo root not found")
