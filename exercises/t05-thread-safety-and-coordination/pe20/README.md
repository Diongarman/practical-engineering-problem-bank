# PE20 · 1115. Print FooBar Alternately

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T05 · Thread safety and coordination |
| Practice order | 22 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE18](../../../exercises/t05-thread-safety-and-coordination/pe18/README.md) |
| Source | LeetCode |
| Platform rating | Medium |

## Task and interface

Implement the original two-thread coordination task. One thread prints foo and the other bar, producing n complete alternating pairs without busy waiting.

## Acceptance checks

1. n=1 produces one complete pair.
2. Starting the bar thread first still produces foo first.
3. Larger n preserves exact alternation.
4. Both threads terminate and emit no extra callbacks.

## Python tools

Condition, Semaphore or Event, signalling

## Optional follow-up

Add a stop signal and specify whether stopping can leave an incomplete pair.

## Reference

[Problem statement](https://leetcode.com/problems/print-foobar-alternately/)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
