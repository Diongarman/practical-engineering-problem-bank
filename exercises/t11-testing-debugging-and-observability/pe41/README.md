# PE41 · Tests from a state-transition table

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T11 · Testing, debugging and observability |
| Practice order | 6 of 48 |
| Difficulty | Easy |
| Starter | Yes |
| Prerequisites | [PE04](../../../exercises/t01-api-design-and-state-machines/pe04/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Write a test suite for PE04 from its public contract. List each legal transition and each rejected operation before coding tests. Include unknown IDs, repeated acknowledgements, empty reserve and terminal-state behaviour. Add one deliberate defect and show the suite detects it.

## Acceptance checks

1. Every legal transition has an observable-behaviour test.
2. Rejected operations preserve prior state.
3. At least one realistic inserted defect is caught.
4. Tests avoid inspecting private containers to mirror implementation.

## Python tools

unittest, subTest, transition tables

## Optional follow-up

Generate operation sequences and compare outcomes with a small reference state model.

## Reference

[Python reference](https://docs.python.org/3/library/unittest.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
