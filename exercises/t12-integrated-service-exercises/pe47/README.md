# PE47 · Streaming inference request batcher

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T12 · Integrated service exercises |
| Practice order | 47 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE26](../../../exercises/t07-async-i-o-and-cancellation/pe26/README.md), [PE27](../../../exercises/t07-async-i-o-and-cancellation/pe27/README.md), [PE15](../../../exercises/t04-time-expiry-and-rate-limits/pe15/README.md), [PE43](../../../exercises/t11-testing-debugging-and-observability/pe43/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Build an async request batcher around an injected fake model. Each request has an ID and a Future. Flush when max_batch_size is reached or max_wait expires from the first waiting request. Bound pending work. Preserve per-request results, cancellation and clean shutdown without using a real model or GPU.

## Acceptance checks

1. A full batch flushes before the wait deadline.
2. A partial batch flushes when its deadline arrives.
3. Cancelled queued requests are not sent to the model.
4. A failed model call resolves every affected Future with an error.
5. Shutdown drains or cancels pending work according to one policy.

## Python tools

asyncio.Queue, Future, timeout, fake model, metrics

## Optional follow-up

Measure throughput versus waiting latency under different batch sizes using a repeatable simulated workload.

## Reference

[Python reference](https://docs.python.org/3.11/library/asyncio-task.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
