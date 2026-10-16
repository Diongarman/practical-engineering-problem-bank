# PE04 · Job lifecycle manager

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T01 · API design and state machines |
| Practice order | 5 of 48 |
| Difficulty | Medium |
| Starter | Yes |
| Prerequisites | [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md), [PE05](../../../exercises/t02-queues-and-backpressure/pe05/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement submit(payload), reserve(), complete(job_id), fail(job_id) for a sequential queue. Use pending, reserved, completed and failed states. Reserve returns the oldest pending ID or None. Only reserved jobs can complete or fail. Failure is terminal in this first version.

## Acceptance checks

1. Submitting starts a job as pending.
2. Completing a pending job is rejected without changing it.
3. A reserved job reaches one terminal state and never returns from reserve.
4. Duplicate terminal acknowledgements have no further effect.

## Python tools

Enum, dataclasses, dict, deque

## Optional follow-up

Draw the transition table and add a new cancellation operation with an explicit contract.

## Reference

[Python reference](https://docs.python.org/3/tutorial/classes.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
