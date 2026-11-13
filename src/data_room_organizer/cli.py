"""The `dataroom` command line. Phase 0 ships `version`, `fields` and `shelves`;
`init`, `classify`, `file`, `sync`, `model` and `hygiene` land with their phases."""

from __future__ import annotations

import typer

from data_room_organizer import __version__
from data_room_organizer.header import HEADER_FIELDS
from data_room_organizer.taxonomy import ARCHIVE, DEFAULT_SHELVES, INBOX

app = typer.Typer(
    help="dataroom: turn a pile of documents into an organized data room.",
    no_args_is_help=True,
)


@app.command()
def version() -> None:
    """Print the version."""
    typer.echo(__version__)


@app.command()
def fields() -> None:
    """List the self-addressing header fields."""
    for f in HEADER_FIELDS:
        typer.echo(f)


@app.command()
def shelves() -> None:
    """List the default shelves, then the Inbox and the Archive."""
    for s in (*DEFAULT_SHELVES, INBOX, ARCHIVE):
        typer.echo(s)
