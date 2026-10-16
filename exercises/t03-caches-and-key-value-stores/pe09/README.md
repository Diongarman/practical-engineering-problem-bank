# PE09 · Bounded key-value cache

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T03 · Caches and key-value stores |
| Practice order | 7 of 48 |
| Difficulty | Easy |
| Starter | Yes |
| Prerequisites | [PE02](../../../exercises/t01-api-design-and-state-machines/pe02/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement get(key), put(key,value) and delete(key) with FIFO eviction and positive capacity. Missing keys raise KeyError. Reading or updating a key does not move it in FIFO order. Inserting a new key into a full cache evicts the earliest inserted remaining key.

## Acceptance checks

1. Overwriting a key preserves its FIFO position.
2. Reading a key does not protect it from FIFO eviction.
3. Capacity one behaves correctly.
4. Deleting a missing key has a documented outcome.

## Python tools

dict, OrderedDict, exceptions

## Optional follow-up

Separate the eviction policy from value storage so a second policy can be added.

## Reference

[Python reference](https://docs.python.org/3/library/collections.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
