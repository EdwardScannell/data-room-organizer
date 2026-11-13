"""Phase 0: the header standard and the default taxonomy are fixed."""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

import data_room_organizer
from data_room_organizer.cli import app
from data_room_organizer.header import (
    HEADER_FIELDS,
    REQUIRED_FIELDS,
    ROUTING_FIELD,
    SUPERSESSION_FIELDS,
    Status,
)
from data_room_organizer.library import init_library
from data_room_organizer.taxonomy import ARCHIVE, DEFAULT_SHELVES, INBOX


def test_version() -> None:
    assert data_room_organizer.__version__ == "0.0.1"


def test_header_fields() -> None:
    assert ROUTING_FIELD == "path"
    assert ROUTING_FIELD in REQUIRED_FIELDS
    assert SUPERSESSION_FIELDS == ("supersedes", "superseded_by", "status")
    assert HEADER_FIELDS == REQUIRED_FIELDS + SUPERSESSION_FIELDS
    assert [s.value for s in Status] == ["current", "superseded", "draft"]


def test_default_taxonomy_is_generic_and_complete() -> None:
    assert len(DEFAULT_SHELVES) == 8
    assert "Cap Table" in DEFAULT_SHELVES
    assert INBOX not in DEFAULT_SHELVES and ARCHIVE not in DEFAULT_SHELVES


def test_init_is_declared_but_not_built_yet(tmp_path: Path) -> None:
    with pytest.raises(NotImplementedError, match="phase 1"):
        init_library(tmp_path)


def test_cli_commands() -> None:
    runner = CliRunner()
    assert runner.invoke(app, ["version"]).output.strip() == "0.0.1"
    assert runner.invoke(app, ["fields"]).output.split()[4] == "path"
    out = runner.invoke(app, ["shelves"]).output.strip().splitlines()
    assert out[0] == "Corporate" and out[-2:] == ["Inbox", "Archive"]
