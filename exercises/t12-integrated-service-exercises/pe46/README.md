# PE46 · Configurable loading cache

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T12 · Integrated service exercises |
| Practice order | 46 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE12](../../../exercises/t03-caches-and-key-value-stores/pe12/README.md), [PE22](../../../exercises/t06-worker-pools-and-scheduling/pe22/README.md), [PE43](../../../exercises/t11-testing-debugging-and-observability/pe43/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Build a cache with FIFO or LRU policy selected at construction, TTL, thread-safe get_or_load and single-flight loading for each missing key. Invoke loaders outside the global state lock. Expose hit, miss, load and eviction metrics. Define how capacity applies to cached versus in-flight entries.

## Acceptance checks

1. Different policies produce their documented eviction choices.
2. Twenty concurrent misses for one key trigger one load.
3. A slow load for one key does not block hits for another.
4. Loader failure is visible to all waiters and does not poison future loads.
5. Expired generations cannot remove newer values.

## Python tools

Lock, Future, OrderedDict, injected clock, logging

## Optional follow-up

Compare cache-policy hit rates on the same reproducible access trace.

## Reference

[Python reference](https://docs.python.org/3/library/collections.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
