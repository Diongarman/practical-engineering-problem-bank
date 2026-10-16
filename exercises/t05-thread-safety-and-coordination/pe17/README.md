# PE17 · Thread-safe counter

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T05 · Thread safety and coordination |
| Practice order | 10 of 48 |
| Difficulty | Easy |
| Starter | Yes |
| Prerequisites | None |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement Counter.increment(amount=1) and Counter.value(). Protect all shared accesses with the same lock. Launch multiple threads against one instance and join them before reading the final value.

## Acceptance checks

1. Eight threads adding 1000 each produce 8000.
2. Negative increments follow the documented policy.
3. Reading does not mutate the counter.
4. Exceptions do not leave the lock acquired.

## Python tools

threading.Thread, Lock, start, join

## Optional follow-up

Write an explicit lost-update interleaving rather than assuming removing the lock will fail on every run.

## Reference

[Python reference](https://docs.python.org/3/library/threading.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
