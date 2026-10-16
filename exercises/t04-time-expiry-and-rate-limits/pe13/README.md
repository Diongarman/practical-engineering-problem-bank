# PE13 · 933. Number of Recent Calls

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T04 · Time, expiry and rate limits |
| Practice order | 8 of 48 |
| Difficulty | Easy |
| Starter | Yes |
| Prerequisites | [PE05](../../../exercises/t02-queues-and-backpressure/pe05/README.md) |
| Source | LeetCode |
| Platform rating | Easy |

## Task and interface

Implement RecentCounter.ping(t) for the original inclusive 3000 ms window. Keep only timestamps in the current window and return the number of retained requests. Use the supplied increasing timestamps.

## Acceptance checks

1. Include a request exactly 3000 ms old.
2. Remove a request older than the lower boundary.
3. Every ping counts the newly added request.
4. Old timestamps do not accumulate indefinitely.

## Python tools

deque, boundary tests, amortised complexity

## Optional follow-up

Make the window configurable. For concurrent use, define clock ordering and protect eviction plus insertion plus counting.

## Reference

[Problem statement](https://leetcode.com/problems/number-of-recent-calls/)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
