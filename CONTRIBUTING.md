# Contributing

## Setup

```bash
python -m venv .venv && . .venv/bin/activate
make install
make check           # lint, strict types, tests with coverage (must stay >= 90%)
```

## The rules for changes

1. **Non-destructive.** No code path may move, rename or delete anything in the source
   pile. The room is built from copies.
2. **Never delete in the room.** Superseded files are dated and moved to the Archive.
3. **Never guess a home.** A document that does not resolve goes to the Inbox, flagged.
4. **The header is an instruction, not a fact.** When a header disagrees with its file,
   flag it; never pick a winner silently.
5. **Generic only.** The shipped taxonomy is a standard, public structure; any private
   layout is supplied at run time and never committed.
6. **Every bug gets a regression test first**, in `tests/regression/`, named after it.
7. **Keep the public API typed.** `mypy --strict` must pass.

## Pull requests

- One topic per PR, with a test that fails before the change and passes after.
- Update `CHANGELOG.md` and tick the phase in `ROADMAP.md` when it is complete.

## Fixtures

Sample documents are synthetic. Do not add real contracts, financials or personal data.
