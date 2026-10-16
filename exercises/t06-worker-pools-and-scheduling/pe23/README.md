# PE23 · Retrying task runner

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T06 · Worker pools and scheduling |
| Practice order | 30 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE21](../../../exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE34](../../../exercises/t09-retries-and-failure-handling/pe34/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Run tasks in a fixed worker pool. Retry declared transient exceptions up to max_attempts including the first attempt. Permanent errors stop immediately. Return a record with task ID, outcome, attempts and last error. Inject backoff waiting so tests need no real delay.

## Acceptance checks

1. Success after two failures records three attempts.
2. A permanent error is tried once.
3. Repeated transient failure stops at the attempt budget.
4. A failed task does not stop other tasks.

## Python tools

ThreadPoolExecutor, exceptions, fake wait, dataclasses

## Optional follow-up

Coordinate delayed retries without keeping a worker occupied during backoff.

## Reference

[Python reference](https://docs.python.org/3/library/concurrent.futures.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
