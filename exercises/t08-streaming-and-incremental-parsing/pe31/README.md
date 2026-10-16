# PE31 · Ordered results from an out-of-order stream

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T08 · Streaming and incremental parsing |
| Practice order | 28 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE05](../../../exercises/t02-queues-and-backpressure/pe05/README.md), [PE21](../../../exercises/t06-worker-pools-and-scheduling/pe21/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Build an assembler for results labelled with unique sequence numbers starting at zero. Emit each contiguous ready prefix in order. Buffer later results up to max_buffered; signal backpressure on overflow. finish reports missing sequence numbers instead of silently skipping them.

## Acceptance checks

1. Arrival order 2,0,1 emits 0, then 1 and 2.
2. Duplicate sequence numbers are rejected.
3. Buffer occupancy stays within the configured bound.
4. End of stream exposes gaps.

## Python tools

dict, generators, bounded buffers

## Optional follow-up

Integrate admission control so the buffer cannot deadlock behind an unscheduled early task.

## Reference

[Python reference](https://docs.python.org/3/library/collections.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
