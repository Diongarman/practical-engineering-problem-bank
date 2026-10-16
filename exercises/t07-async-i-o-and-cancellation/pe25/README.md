# PE25 · Async fan-out over fake I/O

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T07 · Async I/O and cancellation |
| Practice order | 13 of 48 |
| Difficulty | Easy |
| Starter | No |
| Prerequisites | [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Write async fetch_all(ids, fetch) using an injected asynchronous fetch function. Start independent calls concurrently and return one outcome per input in input order. Preserve failures as explicit outcome records. Use local fake I/O.

## Acceptance checks

1. Completion order can differ from returned order.
2. One failure does not discard successful results.
3. Empty input returns immediately.
4. All created tasks are awaited.

## Python tools

async def, await, asyncio.gather, asyncio.run

## Optional follow-up

Add an asyncio.Semaphore to bound simultaneously active fetches.

## Reference

[Python reference](https://docs.python.org/3.11/library/asyncio-task.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
