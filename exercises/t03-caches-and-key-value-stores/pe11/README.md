# PE11 · 981. Time Based Key-Value Store

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T03 · Caches and key-value stores |
| Practice order | 19 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md) |
| Source | LeetCode |
| Platform rating | Medium |

## Task and interface

Implement set(key,value,timestamp) and get(key,timestamp). A read returns the value with the greatest stored timestamp at or before the requested time. Preserve the original guarantee that set timestamps increase.

## Acceptance checks

1. A query before the first timestamp has no value.
2. Exact timestamp and between-timestamp queries return correctly.
3. An unknown key returns the documented missing result.
4. A query after the latest write returns that latest value.

## Python tools

dict, timestamp/value lists, bisect

## Optional follow-up

Allow concurrent readers and writers. Define how duplicate or out-of-order timestamps are handled.

## Reference

[Problem statement](https://leetcode.com/problems/time-based-key-value-store/)

**Source note:** The original problem guarantees increasing set timestamps. Out-of-order writes are an optional extension.

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
