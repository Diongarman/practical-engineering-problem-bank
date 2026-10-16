# PE40 · Durable queue recovery

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T10 · Persistence and recovery |
| Practice order | 43 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE36](../../../exercises/t09-retries-and-failure-handling/pe36/README.md), [PE39](../../../exercises/t10-persistence-and-recovery/pe39/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Persist PE36's jobs and transitions in SQLite. Claims and acknowledgements use transactions. Store deadlines in an explicitly defined restart-stable time domain. Simulate a restart while jobs are pending, reserved, completed and dead-lettered. Resume expired reserved work within its remaining budget.

## Acceptance checks

1. Completed jobs never reappear after restart.
2. Attempt counts survive interruption.
3. Expired reservations recover or dead-letter correctly.
4. An old token cannot acknowledge a recovered claim.
5. A failed transaction leaves no partial state transition.

## Python tools

sqlite3, transactional updates, clocks, fault injection

## Optional follow-up

Allow two worker processes to claim work atomically and discuss clock assumptions.

## Reference

[Python reference](https://docs.python.org/3/library/sqlite3.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
