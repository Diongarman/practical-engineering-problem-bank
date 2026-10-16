# PE43 · Instrument a worker pool

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T11 · Testing, debugging and observability |
| Practice order | 34 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE21](../../../exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE41](../../../exercises/t11-testing-debugging-and-observability/pe41/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Add structured lifecycle logs and a metrics snapshot to PE21 or PE23. Track submitted, running, succeeded and failed tasks, queue wait, and processing duration. Each record has task ID, event and time. Do not log full payloads by default. Keep counter updates thread-safe.

## Acceptance checks

1. Terminal counts reconcile with accepted tasks.
2. Running returns to zero after completion or failure.
3. Wait time and processing duration are separate.
4. Logs can be parsed as JSON and related to one task.

## Python tools

logging, json, monotonic, Lock, metrics snapshots

## Optional follow-up

Add latency histograms and explain why an average alone can hide slow requests.

## Reference

[Python reference](https://docs.python.org/3/library/logging.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
