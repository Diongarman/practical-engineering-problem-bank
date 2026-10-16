# PE22 · Atomic duplicate-work scheduler

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T06 · Worker pools and scheduling |
| Practice order | 24 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE21](../../../exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE33](../../../exercises/t09-retries-and-failure-handling/pe33/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement submit(task_id,payload) so repeated submissions with the same ID share one Future. Reject reuse of an ID with different payload. Reserve the ID atomically before scheduling. Keep the ID-to-Future mapping for the scheduler's lifetime.

## Acceptance checks

1. Twenty concurrent identical submissions execute one task.
2. All callers receive the same result or failure.
3. Conflicting payload reuse is rejected.
4. Scheduling failure removes the incomplete registration safely.

## Python tools

Lock, Future, ThreadPoolExecutor, payload fingerprint

## Optional follow-up

Add a retention policy and distinguish deduplicating pending tasks from completed-result caching.

## Reference

[Python reference](https://docs.python.org/3/library/concurrent.futures.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
