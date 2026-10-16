# PE08 · Queue shutdown without lost work

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T02 · Queues and backpressure |
| Practice order | 35 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE07](../../../exercises/t02-queues-and-backpressure/pe07/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Extend PE07 with close(drain=True). Closing rejects new puts and wakes waiting callers. Consumers drain accepted items, then receive QueueClosed. For drain=False, discard waiting items and report the discarded count. Work already returned to a consumer is outside the buffer.

## Acceptance checks

1. A blocked producer wakes and receives QueueClosed.
2. Drain mode returns every accepted buffered item once.
3. Discard mode reports the exact buffered count.
4. All waiting consumers eventually terminate.

## Python tools

Condition, Event, queue lifecycle, thread joins

## Optional follow-up

Add task_done and join-style unfinished-work accounting, including a documented discard rule.

## Reference

[Python reference](https://docs.python.org/3/library/queue.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
