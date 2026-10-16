# PE06 · 622. Design Circular Queue

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T02 · Queues and backpressure |
| Practice order | 4 of 48 |
| Difficulty | Medium |
| Starter | Yes |
| Prerequisites | [PE05](../../../exercises/t02-queues-and-backpressure/pe05/README.md) |
| Source | LeetCode |
| Platform rating | Medium |

## Task and interface

Implement the original fixed-capacity circular queue API using a list and indices. Support enqueue, dequeue, front, rear, full and empty. Do not use a built-in queue to solve the baseline.

## Acceptance checks

1. Capacity one works correctly.
2. Full enqueue and empty dequeue return failure.
3. After removals, new entries reuse earlier array positions.
4. Front and rear remain correct across wraparound.

## Python tools

list, modular arithmetic, invariants

## Optional follow-up

Add a lock around compound operations and test two producers competing for one remaining slot.

## Reference

[Problem statement](https://leetcode.com/problems/design-circular-queue/)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
