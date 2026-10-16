# PE05 · FIFO queue with explicit empty behaviour

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T02 · Queues and backpressure |
| Practice order | 3 of 48 |
| Difficulty | Easy |
| Starter | Yes |
| Prerequisites | None |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement put(item), get(), peek() and length for an unbounded FIFO queue using a deque. Let get and peek raise a custom EmptyQueue error when empty. Treat None as a valid item.

## Acceptance checks

1. Items leave in insertion order.
2. Empty get and peek raise the documented error.
3. Peeking does not remove an item.
4. A stored None is distinguishable from an empty queue.

## Python tools

collections.deque, exceptions, unittest

## Optional follow-up

Add a capacity limit that rejects insertion without silently discarding earlier items.

## Reference

[Python reference](https://docs.python.org/3/library/queue.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
