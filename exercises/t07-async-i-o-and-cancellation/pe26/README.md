# PE26 · Bounded asynchronous processing pipeline

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T07 · Async I/O and cancellation |
| Practice order | 25 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE25](../../../exercises/t07-async-i-o-and-cancellation/pe25/README.md), [PE05](../../../exercises/t02-queues-and-backpressure/pe05/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Connect a lazy producer, a bounded asyncio.Queue and N workers. Process each accepted item, record success or failure, and drain cleanly at end of input. Call task_done in cleanup paths. Keep the producer from enqueueing the entire input at once.

## Acceptance checks

1. Queue occupancy never exceeds capacity.
2. A failed item does not hang queue.join.
3. End of input terminates every worker.
4. No accepted item disappears from the outcome records.

## Python tools

asyncio.Queue, TaskGroup or tasks, task_done/join

## Optional follow-up

Add per-item retry without deadlocking workers that try to refill a full input queue.

## Reference

[Python reference](https://docs.python.org/3.11/library/asyncio-queue.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
