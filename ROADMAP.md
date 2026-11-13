# Roadmap

data-room-organizer is built in small phases. Each lands as its own pull request with
tests, and CI stays green on every commit. It starts as a plain library and grows into a
modeled data room.

0. [x] **Skeleton.** Package, header field standard, default generic shelves, the
   `dataroom` command line, CI on Python 3.11 to 3.13.
1. [ ] **Small data library (walking skeleton).** `dataroom init` makes a plain folder
   structure; one sample document lands on a shelf end to end. Snapshot test.
2. [ ] **Taxonomy and header standard.** Load and validate a taxonomy file; parse a
   document header and read its `path`; report a malformed or missing header instead of
   guessing.
3. [ ] **Labeler.** Classify a document against the taxonomy: read its header if present,
   derive one if not; return a resolved shelf or "unresolved", never a guess.
4. [ ] **Intake.** Event-driven intake: a published document is picked up and routed to
   the labeler and filer. Ordering and at-least-once tests.
5. [ ] **Filer.** Shelve a copy at its `path`; unresolved documents go to the Inbox with
   a flag; a header that disagrees with its file is flagged, not trusted; re-running
   changes nothing; the source is never touched.
6. [ ] **Index and shelving log.** A catalog of every shelved document and an append-only
   log with exactly one row per move.
7. [ ] **Google Drive connector.** Pull documents from a Drive folder into intake (a test
   Drive only), then push the organized room back in a later increment. Idempotent
   re-sync.
8. [ ] **Data room modeler.** For a room type (a VC raise first), recommend the structure
   and name the documents a reviewer will ask for that are missing.
9. [ ] **Hygiene.** Find duplicates, stale files and superseded versions; date them and
   move them to the Archive. Nothing is deleted.

Stretch: ask the room a question (search and retrieval), after phase 9.

## Never

- Changing what is inside a document.
- Moving or deleting anything in the source pile.
- Deleting anything in the room: superseded files are archived, dated.
