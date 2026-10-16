# PE28 · Async single-flight cache

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T07 · Async I/O and cancellation |
| Practice order | 39 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE25](../../../exercises/t07-async-i-o-and-cancellation/pe25/README.md), [PE27](../../../exercises/t07-async-i-o-and-cancellation/pe27/README.md), [PE09](../../../exercises/t03-caches-and-key-value-stores/pe09/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement get_or_load(key, async_loader). Concurrent requests for the same missing key await one shared load. Different keys may load concurrently. Cache successful values only. One caller cancelling its wait must not cancel the shared load for other callers.

## Acceptance checks

1. Twenty callers for one key invoke the loader once.
2. Loader failure reaches every waiter and allows a later retry.
3. Cancellation of one waiter does not fail the others.
4. After completion, no in-flight entry leaks.

## Python tools

asyncio.Lock, Task/Future, shield, dict

## Optional follow-up

Add TTL and define the outcome when a cached value expires during a load.

## Reference

[Python reference](https://docs.python.org/3.11/library/asyncio-task.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
