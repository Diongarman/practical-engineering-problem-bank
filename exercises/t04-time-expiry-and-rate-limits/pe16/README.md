# PE16 · Lease manager with renewal and stale tokens

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T04 · Time, expiry and rate limits |
| Practice order | 37 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE14](../../../exercises/t04-time-expiry-and-rate-limits/pe14/README.md), [PE17](../../../exercises/t05-thread-safety-and-coordination/pe17/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement claim(resource), renew(resource,token), release(resource,token) and expire_due(now). A claim returns a fresh token and deadline or None if occupied. Only a current unexpired token can renew or release. Expiration frees the resource. Renewal extends from the current time.

## Acceptance checks

1. A live lease excludes another claim.
2. A lease expires at its deadline.
3. An old token cannot release or renew a newer claim.
4. Repeated renewal does not let an older heap entry expire the new deadline.

## Python tools

Lock, dict, monotonic clock, uuid, optional heapq

## Optional follow-up

Add maximum total lease duration and explain how renewal interacts with the limit.

## Reference

[Python reference](https://docs.python.org/3/library/time.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
