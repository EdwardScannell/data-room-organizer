"""The self-addressing header standard.

A document can open with a small metadata block that says what it is and where it
belongs. `path` is the routing field the filer reads. The header is an instruction,
not a fact: where it disagrees with the file itself, the filer yields and flags; it
never picks a winner.

Phase 0 fixes the field set and the status vocabulary. Parsing lands in phase 2.
"""

from __future__ import annotations

from enum import StrEnum

ROUTING_FIELD = "path"

REQUIRED_FIELDS: tuple[str, ...] = ("author", "topic", "summary", "timedate", "path")
SUPERSESSION_FIELDS: tuple[str, ...] = ("supersedes", "superseded_by", "status")
HEADER_FIELDS: tuple[str, ...] = REQUIRED_FIELDS + SUPERSESSION_FIELDS


class Status(StrEnum):
    """Where a document stands in its version chain."""

    CURRENT = "current"
    SUPERSEDED = "superseded"
    DRAFT = "draft"
