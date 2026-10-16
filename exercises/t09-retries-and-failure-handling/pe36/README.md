# PE36 · Robust work queue with retries and dead letters

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T09 · Retries and failure handling |
| Practice order | 42 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE04](../../../exercises/t01-api-design-and-state-machines/pe04/README.md), [PE07](../../../exercises/t02-queues-and-backpressure/pe07/README.md), [PE16](../../../exercises/t04-time-expiry-and-rate-limits/pe16/README.md), [PE34](../../../exercises/t09-retries-and-failure-handling/pe34/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement submit, reserve, complete(job_id,token), fail(job_id,token) and dead_letters. Reservations expire after a configurable timeout. Count attempts on reservation; max_retries counts retries after the first. Atomically transition state and reject expired or stale tokens. Capacity counts pending plus reserved work.

## Acceptance checks

1. Multiple workers receive at most one valid reservation for a job.
2. Timeout and explicit failure consume the same attempt budget.
3. A completed job is never reserved again.
4. A late acknowledgement cannot affect a newer reservation.
5. Final failure or timeout moves the job to the dead-letter collection once.

## Python tools

Lock, deque, dict, monotonic, uuid, dataclasses

## Optional follow-up

Add delayed backoff and explain how duplicate task side effects are handled.

## Reference

[Python reference](https://docs.python.org/3/library/queue.html)

**Source note:** Original expanded exercise based on the work-queue prompt supplied in this conversation.

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
