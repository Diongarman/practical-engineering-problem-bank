# PE33 · Idempotent command handler

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T09 · Retries and failure handling |
| Practice order | 15 of 48 |
| Difficulty | Easy |
| Starter | No |
| Prerequisites | [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement execute(request_id,payload,handler) for sequential callers. Remember a successful result under the request ID and a stable payload fingerprint. Return it on identical retries. Reject the same ID with different payload. Failed handlers may be retried and are not recorded as successes.

## Acceptance checks

1. Repeated successful calls execute the handler once.
2. A conflicting payload is rejected.
3. A failure followed by a retry invokes the handler again.
4. Payload dictionaries with reordered keys have the same fingerprint.

## Python tools

dict, json canonicalisation, exceptions

## Optional follow-up

Make registration thread-safe and define whether concurrent duplicate callers wait or receive an in-progress result.

## Reference

[Python reference](https://docs.python.org/3/tutorial/classes.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
