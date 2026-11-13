# data-room-organizer

**Point it at a pile of documents and it hands you back a data room: classified,
shelved, indexed, and told what you are still missing.**

[![CI](https://github.com/EdwardScannell/data-room-organizer/actions/workflows/ci.yml/badge.svg)](https://github.com/EdwardScannell/data-room-organizer/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)

## Why

Every organization accumulates a document pile: contracts, decks, financials, specs,
notes, scattered across folders and drives and findable only by whoever remembers where
they put them. When that pile has to become a data room (for a raise, a sale, an audit
or a diligence request) someone spends hours sorting, naming and gap-checking it by hand,
under deadline.

File storage holds documents; it does not arrange them into a business view or tell you
what is absent. data-room-organizer does: it reads each document, decides where it
belongs, shelves a copy, catalogs it, and lists the documents a reviewer will ask for
that are not there.

## What it is (and is not)

It **is** a filer with principles: it starts as a small, plain library you drop files
into and grows into a modeled data room with a gap list. It **is not** an editor (it
never changes what is inside a file), a deletion tool (superseded files are dated and
archived), or an access-control system.

| Principle | What it means |
|---|---|
| Non-destructive | The source pile is only read and copied; the room sits alongside it |
| Read from disk, not memory | Every action and report re-reads the files first |
| Idempotent | A file already on its correct shelf is left alone |
| Never guess a home | A document that does not resolve goes to the Inbox, flagged |
| Date and archive, never delete | Superseded versions move to the Archive, dated |
| Self-addressing files | A document's header can carry its own shelf address |
| Everything is logged | Every move is one row in an append-only log |
| The header is an instruction, not a fact | When a header and its file disagree, the filer flags it and picks no winner |

## Install

```bash
pip install -e ".[dev]"     # from a clone
make check                  # lint, strict types, tests with coverage
```

## Quick start

Phase 0 fixes the header standard and the default shelves; `dataroom init` lands in
phase 1.

```bash
dataroom version
dataroom fields     # author topic summary timedate path supersedes superseded_by status
dataroom shelves    # Corporate Financials Cap Table IP Legal Commercial Team Product Inbox Archive
```

## The model in one page

**The header.** A document can open with a small metadata block:

```
---
author:        who or what produced it
topic:         one line: what this file is
summary:       2-4 lines: contents and why it exists
timedate:      YYYY-MM-DD HH:MM
path:          the destination shelf (the routing field the filer reads)
supersedes:    prior version's file name, if any          (optional)
superseded_by: newer version's file name, if retired      (optional)
status:        current | superseded | draft               (optional)
---
```

No header, no `path`, or an ambiguous `path` sends the document to the Inbox with a flag.

**The room.** A business-view folder tree built from a taxonomy. The default is a
generic diligence structure: Corporate, Financials, Cap Table, IP, Legal, Commercial,
Team, Product, plus an Inbox and an Archive. The organizer is layout-agnostic: any other
taxonomy is just an input.

**The index and the log.** A catalog of every shelved document (address, date, source)
and an append-only JSONL log with one row per move.

**The modeler.** For a given room type (a VC raise first), the recommended structure
and the named list of documents that are missing.

## Layout

```
src/data_room_organizer/
  header.py     the header fields and status vocabulary (phase 0); parsing (phase 2)
  taxonomy.py   the default generic shelves, Inbox and Archive
  library.py    init (phase 1)
  cli.py        the `dataroom` command line
tests/
  unit/         one test file per rule
  regression/   real bugs, each a permanent test
  fixtures/     synthetic sample documents
```

## Development

```bash
make check      # ruff, mypy --strict, pytest with coverage
```

The work ahead is in [`ROADMAP.md`](ROADMAP.md) and the repository's issues.
Contributions: see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

## About

Built in small phases, thinnest end-to-end slice first: a plain library that files one
document, then the taxonomy, labeler, intake, filer, index and log, a Google Drive
connector, and finally the modeler that turns the library into a data room.
