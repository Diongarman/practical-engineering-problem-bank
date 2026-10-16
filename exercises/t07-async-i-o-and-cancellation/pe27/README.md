# PE27 · Async deadline and cancellation cleanup

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T07 · Async I/O and cancellation |
| Practice order | 26 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE25](../../../exercises/t07-async-i-o-and-cancellation/pe25/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement run_with_deadline(coro, timeout). On expiry, cancel and await the task, release any acquired semaphore permit and close fake resources in finally blocks. Preserve caller cancellation. Test both normal completion and timeout.

## Acceptance checks

1. Timeout produces the documented outcome.
2. A cancelled worker releases its permit.
3. External caller cancellation propagates after cleanup.
4. No task exception is left unobserved.

## Python tools

asyncio.timeout or wait_for, CancelledError, finally

## Optional follow-up

Distinguish the deadline for a whole request from separate deadlines for its stages.

## Reference

[Python reference](https://docs.python.org/3.11/library/asyncio-task.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
