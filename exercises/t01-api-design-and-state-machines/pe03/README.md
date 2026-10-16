# PE03 · 1472. Design Browser History

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T01 · API design and state machines |
| Practice order | 17 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md) |
| Source | LeetCode |
| Platform rating | Medium |

## Task and interface

Implement a one-tab browser history with visit, back and forward. Visits from an older page discard the forward branch. Clamp navigation at the beginning and end.

## Acceptance checks

1. Back/forward beyond the available history stops at its boundary.
2. A new visit after going back removes forward history.
3. Navigation returns the current page.

## Python tools

list and cursor, classes, unittest

## Optional follow-up

Generalise the component to an undo/redo command history and document which state belongs in a snapshot.

## Reference

[Problem statement](https://leetcode.com/problems/design-browser-history/)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
