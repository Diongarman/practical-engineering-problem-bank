# PE14 · 1797. Design Authentication Manager

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T04 · Time, expiry and rate limits |
| Practice order | 9 of 48 |
| Difficulty | Medium |
| Starter | Yes |
| Prerequisites | [PE13](../../../exercises/t04-time-expiry-and-rate-limits/pe13/README.md) |
| Source | LeetCode |
| Platform rating | Medium |

## Task and interface

Implement token generation, renewal and unexpired-token counting for a configurable TTL. Expiration takes precedence over any operation at the exact deadline. Follow the original strictly increasing currentTime inputs.

## Acceptance checks

1. A token generated at t expires at t + TTL.
2. Renewal at the expiry time is ignored.
3. Renewal before expiry extends the deadline.
4. Missing or expired tokens cannot be renewed.

## Python tools

dict, deadlines, explicit clock values

## Optional follow-up

Replace supplied times with an injected clock and add local concurrent renewal tests.

## Reference

[Problem statement](https://leetcode.com/problems/design-authentication-manager/)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
