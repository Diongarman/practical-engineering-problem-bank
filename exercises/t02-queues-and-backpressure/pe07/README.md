# PE07 · Bounded blocking queue

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T02 · Queues and backpressure |
| Practice order | 18 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE05](../../../exercises/t02-queues-and-backpressure/pe05/README.md), [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE18](../../../exercises/t05-thread-safety-and-coordination/pe18/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement put(item, timeout=None) and get(timeout=None) with a positive configurable capacity. Producers wait when full; consumers wait when empty. Use one lock and condition variables. Wait in predicate loops and calculate timeout against a deadline.

## Acceptance checks

1. A full queue blocks a producer until a consumer removes an item.
2. An empty queue blocks a consumer until insertion.
3. Timeout raises a documented error and does not consume a slot.
4. Multiple producers and consumers preserve all submitted items.

## Python tools

threading.Condition, Lock, deque, monotonic

## Optional follow-up

Add close() and specify how waiting callers are released.

## Reference

[Python reference](https://docs.python.org/3/library/threading.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
