# PE34 · Retry wrapper with backoff

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T09 · Retries and failure handling |
| Practice order | 29 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE13](../../../exercises/t04-time-expiry-and-rate-limits/pe13/README.md), [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement call_with_retry(fn,max_attempts,base_delay,cap_delay,wait,rng). Retry only TransientError. Delay after failed attempt i by min(cap_delay, base_delay * 2^(i-1)) plus documented bounded jitter. Do not wait after the final failure. Inject wait and randomness.

## Acceptance checks

1. A permanent failure is propagated immediately.
2. Attempt count includes the initial call.
3. The delay schedule matches the configured cap.
4. Seeded randomness makes the test schedule repeatable.

## Python tools

exceptions, random.Random, dependency injection

## Optional follow-up

Add a total deadline that can stop retries before the attempt budget is exhausted.

## Reference

[Python reference](https://docs.python.org/3/library/time.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
