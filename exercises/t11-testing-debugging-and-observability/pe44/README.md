# PE44 · Diagnose a serialised worker pool

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T11 · Testing, debugging and observability |
| Practice order | 44 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE21](../../../exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE42](../../../exercises/t11-testing-debugging-and-observability/pe42/README.md), [PE43](../../../exercises/t11-testing-debugging-and-observability/pe43/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Investigate this worker shape: with lock: result = fake_fetch(item); results.append(result). fake_fetch is blocking I/O. Reproduce the bottleneck, explain the lock scope, move I/O outside the lock, and bound future submission so a lazy input is not eagerly exhausted.

## Acceptance checks

1. A fixture demonstrates that the original serialises fake I/O.
2. The repair permits overlapping calls without exceeding worker limits.
3. Result updates remain safe.
4. Submission remains bounded and task errors are visible.
5. The report separates correctness evidence from timing observations.

## Python tools

ThreadPoolExecutor, cProfile, logging, Event/Barrier

## Optional follow-up

Diagnose a blocking function inside async code and replace it with appropriate nonblocking I/O or to_thread.

## Reference

[Python reference](https://docs.python.org/3/library/concurrent.futures.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
