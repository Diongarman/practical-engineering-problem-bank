# PE48 · Recoverable streaming processing pipeline

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T12 · Integrated service exercises |
| Practice order | 48 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE30](../../../exercises/t08-streaming-and-incremental-parsing/pe30/README.md), [PE36](../../../exercises/t09-retries-and-failure-handling/pe36/README.md), [PE39](../../../exercises/t10-persistence-and-recovery/pe39/README.md), [PE43](../../../exercises/t11-testing-debugging-and-observability/pe43/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Combine an incremental JSON Lines reader, a bounded queue, worker pool, retry budget, dead-letter records, durable receipts and structured logs. Inject the processing function and storage failures. Support a clean stop and a simulated restart. Use idempotent task IDs to deduplicate successful effects.

## Acceptance checks

1. Chunked input produces the same records as whole input.
2. Queue and in-flight work remain within stated bounds.
3. One bad record or task does not silently lose other accepted work.
4. Permanent failures produce inspectable dead-letter records.
5. Restart does not repeat a committed idempotent effect.

## Python tools

codecs, queue, ThreadPoolExecutor, sqlite3, logging

## Optional follow-up

Provide a CLI and a benchmark report that identifies the next bottleneck.

## Reference

[Python reference](https://docs.python.org/3/library/concurrent.futures.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
