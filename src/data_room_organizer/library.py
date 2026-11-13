"""The library: the plain folder structure a room starts as. Declared in phase 0,
built in phase 1."""

from __future__ import annotations

from pathlib import Path


def init_library(root: Path) -> Path:
    """Create a small library (shelves, Inbox, Archive) under `root`. Phase 1."""
    raise NotImplementedError("init lands in phase 1 (small data library)")
