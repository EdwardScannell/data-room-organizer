"""The default taxonomy: a generic, publicly known diligence structure.

The organizer is layout-agnostic: it files to whatever taxonomy it is given. This
default ships so the tool works out of the box; any other layout is just an input.
Loading and validating a taxonomy file lands in phase 2.
"""

from __future__ import annotations

DEFAULT_SHELVES: tuple[str, ...] = (
    "Corporate",
    "Financials",
    "Cap Table",
    "IP",
    "Legal",
    "Commercial",
    "Team",
    "Product",
)

INBOX = "Inbox"  # documents that do not resolve to a shelf, flagged for a person
ARCHIVE = "Archive"  # superseded versions, dated; nothing is ever deleted
