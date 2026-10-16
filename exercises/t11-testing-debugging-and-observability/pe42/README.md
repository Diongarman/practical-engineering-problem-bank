# PE42 · Deterministic race reproduction

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T11 · Testing, debugging and observability |
| Practice order | 33 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE41](../../../exercises/t11-testing-debugging-and-observability/pe41/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Create a deliberately broken single-resource claim: read availability, then update it without a lock. Add a test-only hook after the read and use a Barrier to force two readers through it before either updates. Demonstrate duplicate claims, then fix the component and add a one-winner regression test.

## Acceptance checks

1. The arranged broken interleaving produces two successful claims.
2. The fixed version admits one valid claim.
3. The fixed test never waits at a barrier while holding the claim lock.
4. Tests use bounded joins and no sleep-based correctness assertion.

## Python tools

Barrier, Event, Lock, unittest.mock

## Optional follow-up

Apply the same method to a duplicate-work scheduler or stale reservation acknowledgement.

## Reference

[Python reference](https://docs.python.org/3/library/threading.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
