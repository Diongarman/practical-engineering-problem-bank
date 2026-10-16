# PE15 · Per-client sliding-window rate limiter

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T04 · Time, expiry and rate limits |
| Practice order | 20 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE13](../../../exercises/t04-time-expiry-and-rate-limits/pe13/README.md), [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement allow(client_id, now) for a limit N in window W. Retain accepted requests in the interval (now-W, now]. Reject a request if accepting it would exceed N. Rejected calls do not consume quota. Calls use nondecreasing time; protect check-and-record with one lock.

## Acceptance checks

1. Two clients have independent budgets.
2. A request exactly W old no longer counts.
3. Repeated rejection does not delay future eligibility.
4. Two callers competing for the final permit produce one success.

## Python tools

dict of deques, Lock, fake clock

## Optional follow-up

Return retry_after and clean up idle client records without losing active history.

## Reference

[Python reference](https://docs.python.org/3/library/time.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
