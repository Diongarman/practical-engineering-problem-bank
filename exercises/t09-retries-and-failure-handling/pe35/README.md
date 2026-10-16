# PE35 · Concurrent circuit breaker

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T09 · Retries and failure handling |
| Practice order | 41 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE14](../../../exercises/t04-time-expiry-and-rate-limits/pe14/README.md), [PE34](../../../exercises/t09-retries-and-failure-handling/pe34/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Wrap an injected dependency with closed, open and half-open states. Consecutive failures open the breaker at a threshold. After a cooldown, admit exactly one probe while other callers fail fast. Probe success closes it; failure reopens it. Keep dependency execution outside the state lock.

## Acceptance checks

1. Calls during cooldown never invoke the dependency.
2. Only one concurrent half-open probe is admitted.
3. A successful probe resets failure state.
4. Failures and timeout policy follow one documented transition table.

## Python tools

Lock, injected clock, exceptions, state machine

## Optional follow-up

Record the state generation so an older in-flight result cannot overwrite a newer breaker state.

## Reference

[Python reference](https://docs.python.org/3/library/threading.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
