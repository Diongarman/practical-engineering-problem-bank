# PE21 · Bounded parallel map

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T06 · Worker pools and scheduling |
| Practice order | 23 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE05](../../../exercises/t02-queues-and-backpressure/pe05/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement parallel_map(fn, items, max_workers, max_in_flight). Items may be a lazy generator. Return results in input order, allow at most max_in_flight submitted-but-uncollected futures, and represent task exceptions per item without aborting unrelated work.

## Acceptance checks

1. Out-of-order finishes still produce input-ordered results.
2. An instrumented generator proves the submission bound.
3. Active functions never exceed max_workers.
4. A failure in one task does not lose other results.

## Python tools

ThreadPoolExecutor, Future, wait/as_completed

## Optional follow-up

Add fail-fast mode and explain why cancelling a running thread future does not stop its function.

## Reference

[Python reference](https://docs.python.org/3/library/concurrent.futures.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
