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

Track status and attempts in [problems.csv](../../../data/problems.csv).

## Starting the exercise

Fill in `CommandAdapter.__init__` and `CommandAdapter.handle` in [src/solution.py](src/solution.py). Both currently raise `NotImplementedError`; no solution is provided. Create one adapter instance and call its `handle(command)` method for each command in a sequence.

The scaffold suggests an `op` field for the operation, plus `key` and (for `set`) `value`. This is a suggested command format; the workbook does not prescribe those field names. Document any remaining contract choices in your design note before testing them.

Write your own tests in `tests/test_solution.py`, importing `CommandAdapter` from `solution`. The acceptance checks above are requirements, not implemented tests. See the [test-writing guidance](../../../README.md#writing-your-own-tests).

From this **PE02 folder**, run your tests with:

```sh
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Until you add tests, this command will discover zero tests; that does not indicate a completed exercise.
