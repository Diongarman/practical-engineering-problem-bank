# PE24 · Dynamic graph crawler with reliable completion

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T06 · Worker pools and scheduling |
| Practice order | 38 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE21](../../../exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE22](../../../exercises/t06-worker-pools-and-scheduling/pe22/README.md), [PE23](../../../exercises/t06-worker-pools-and-scheduling/pe23/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Crawl a fake URL graph using a worker pool and injected fetch(url). Restrict to the start URL's hostname, atomically deduplicate discovered URLs, cap in-flight work, and record fetch failures. A transient fetch may retry under a fixed budget. Return only when no queued or running work remains.

## Acceptance checks

1. A diamond-shaped graph fetches each successfully visited URL once.
2. Cycles terminate and other hostnames are skipped.
3. Children discovered by the last running task are still processed.
4. Failures do not strand the completion tracker.

## Python tools

ThreadPoolExecutor, Lock, Condition, urllib.parse

## Optional follow-up

Add cancellation and report processed, pending and failed URLs consistently.

## Reference

[Python reference](https://docs.python.org/3/library/concurrent.futures.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
