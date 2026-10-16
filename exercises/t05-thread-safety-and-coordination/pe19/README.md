# PE19 · Exercism Bank Account plus local concurrency tests

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T05 · Thread safety and coordination |
| Practice order | 21 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md) |
| Source | Exercism |
| Platform rating | Medium |

## Task and interface

Complete the original Python Bank Account exercise: open, close, read balance, deposit and withdraw, with its required validation errors. Then add local threaded tests and synchronise balance checks, updates and open/closed state.

## Acceptance checks

1. The source's sequential tests pass.
2. Concurrent deposits reconcile with the expected total.
3. Competing withdrawals cannot spend the same balance twice.
4. Operations after closure fail without modifying balance.

## Python tools

Lock, ValueError, unittest, Barrier

## Optional follow-up

Add transfer between two accounts using a stable lock order to avoid deadlock.

## Reference

[Problem statement](https://exercism.org/tracks/python/exercises/bank-account)

**Source note:** Exercism's Python track currently tests sequential operations. Threaded tests here are an explicit local extension.

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
