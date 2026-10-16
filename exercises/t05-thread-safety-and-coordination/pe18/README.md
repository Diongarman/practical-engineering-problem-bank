# PE18 · 1114. Print in Order

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T05 · Thread safety and coordination |
| Practice order | 11 of 48 |
| Difficulty | Easy |
| Starter | Yes |
| Prerequisites | [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md) |
| Source | LeetCode |
| Platform rating | Easy |

## Task and interface

Implement the original three-method coordination problem so first, second and third callbacks run in that order regardless of thread launch order. Use signalling rather than timing assumptions.

## Acceptance checks

1. Launch threads in each of the six permutations.
2. Every run produces first-second-third callback order.
3. All threads terminate within the test's join timeout.

## Python tools

threading.Event or semaphores, Thread.join

## Optional follow-up

Extend from a one-shot ordering to a reusable three-stage cycle and define reset behaviour.

## Reference

[Problem statement](https://leetcode.com/problems/print-in-order/)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
