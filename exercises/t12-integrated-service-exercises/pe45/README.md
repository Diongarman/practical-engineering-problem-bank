# PE45 · Reservation service with an HTTP adapter

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T12 · Integrated service exercises |
| Practice order | 45 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md), [PE16](../../../exercises/t04-time-expiry-and-rate-limits/pe16/README.md), [PE19](../../../exercises/t05-thread-safety-and-coordination/pe19/README.md), [PE33](../../../exercises/t09-retries-and-failure-handling/pe33/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Build a local seat-reservation service with reserve, confirm, cancel and status endpoints. Use expiring holds with reservation tokens and idempotent request IDs. Keep allocation logic separate from HTTP parsing. Run competing requests locally and return consistent error responses.

## Acceptance checks

1. Competing requests cannot hold the same seat.
2. Confirmation after expiry is rejected.
3. Duplicate requests return the same reservation outcome.
4. Cancelling a confirmed booking follows a documented policy.
5. Invalid JSON and unknown IDs produce stable API errors.

## Python tools

http.server or familiar framework, Lock, lease manager, JSON

## Optional follow-up

Choose shared storage for two API processes and describe the necessary atomic claim operation.

## Reference

[Python reference](https://docs.python.org/3/library/http.server.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
