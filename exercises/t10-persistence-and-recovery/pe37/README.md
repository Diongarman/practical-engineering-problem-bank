# PE37 · Recover a JSON Lines event log

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T10 · Persistence and recovery |
| Practice order | 16 of 48 |
| Difficulty | Easy |
| Starter | No |
| Prerequisites | [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Write append_event(event) and recover(path) for a single-writer JSON Lines log. Require each complete event to end in a newline. Replay complete valid events. Ignore an incomplete trailing fragment caused by interruption, but raise an error for a malformed complete record.

## Acceptance checks

1. A complete log round-trips its events.
2. An incomplete final fragment is not replayed.
3. Malformed data in the middle is reported with its record number.
4. A missing file has a documented empty-log outcome.

## Python tools

json, pathlib, text/bytes I/O

## Optional follow-up

Reconstruct a key-value store by replaying set and delete events.

## Reference

[Python reference](https://docs.python.org/3/library/json.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
