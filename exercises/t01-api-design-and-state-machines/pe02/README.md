# PE02 · JSON command adapter for a key-value store

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T01 · API design and state machines |
| Practice order | 2 of 48 |
| Difficulty | Easy |
| Starter | Yes |
| Prerequisites | None |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Build handle(command: dict) -> dict around an in-memory store. Support set(key,value), get(key), delete(key). Responses have ok, value and error fields. Missing keys produce a NOT_FOUND error; malformed or unknown operations produce INVALID_COMMAND. A failed command must not change the store.

## Acceptance checks

1. Set, overwrite, read and delete a key.
2. Missing key and unknown operation return distinct errors.
3. Malformed commands leave state unchanged.

## Python tools

dict, dataclasses, exceptions, json

## Optional follow-up

Expose the same handler through a small CLI or HTTP adapter. Keep transport code separate from store logic.

## Reference

[Python reference](https://docs.python.org/3/tutorial/classes.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
