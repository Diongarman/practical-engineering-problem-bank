# PE12 · Thread-safe LRU cache with expiry

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T03 · Caches and key-value stores |
| Practice order | 36 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE10](../../../exercises/t03-caches-and-key-value-stores/pe10/README.md), [PE14](../../../exercises/t04-time-expiry-and-rate-limits/pe14/README.md), [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Extend PE10 with per-entry TTL and an injected monotonic clock. Expired entries are misses and must not displace valid entries during admission. Synchronise lookup, expiry, recency and eviction. Increment hit/miss/eviction counters once per operation.

## Acceptance checks

1. An entry is expired at now >= deadline.
2. Expiring an old generation does not delete a later replacement.
3. Concurrent access never exceeds capacity or corrupts recency.
4. Counters reconcile with the recorded operations.

## Python tools

Lock, OrderedDict, injected clock, unittest

## Optional follow-up

Compare a full expiry scan with a deadline heap containing versioned entries.

## Reference

[Python reference](https://docs.python.org/3/library/time.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
