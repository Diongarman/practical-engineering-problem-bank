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

## Exact contract for this repository

The workbook leaves some interface details open. The rules below make those details explicit for this version of PE02, so you can write tests with unambiguous expected results.

Create a `CommandAdapter()` with an initially empty store, then call `adapter.handle(command)` for each operation. State persists between calls on the same adapter. A new adapter has its own independent, empty store. You are working with **Python dictionaries**, not parsing JSON text; a CLI or HTTP transport is an optional follow-up.

### Input

| Operation | Required dictionary fields | Meaning |
| --- | --- | --- |
| `set` | `op`, `key`, `value` | Create or overwrite the value at this key. |
| `get` | `op`, `key` | Read an existing value. |
| `delete` | `op`, `key` | Remove an existing key and its value. |

- `op` must be exactly `"set"`, `"get"`, or `"delete"` (case-sensitive).
- `key` must be a non-empty string. Do not trim or otherwise normalise it; `"Name"` and `"name"` are different keys.
- Reject missing fields and extra fields. For example, `get` must not include a `value` field.
- A `set` command must include `value`, even when its value is `None`. Assume supplied values are JSON-compatible Python values: strings, numbers, booleans, `None`, lists, or dictionaries. Recursive JSON validation and defensive copying of mutable values are outside this baseline; callers will not mutate stored lists/dictionaries through external references.
- A non-dictionary command is invalid. Invalid commands return an error response rather than raising an exception for the caller.

### Output

Return a dictionary with **exactly these three fields** every time:

| Outcome | Expected response |
| --- | --- |
| Successful `set` | `{"ok": True, "value": None, "error": None}` |
| Successful `get` | `{"ok": True, "value": <stored value>, "error": None}` |
| Successful `delete` | `{"ok": True, "value": None, "error": None}` |
| Valid `get` or `delete` for an absent key | `{"ok": False, "value": None, "error": "NOT_FOUND"}` |
| Malformed command or unknown operation | `{"ok": False, "value": None, "error": "INVALID_COMMAND"}` |

`<stored value>` is a placeholder in the table, not literal Python syntax. All other responses shown are literal Python dictionaries. In JSON text, Python's `True`, `False`, and `None` would appear as `true`, `false`, and `null`.

Validate the command's shape before considering whether its key exists: a malformed `get` for an absent key still returns `INVALID_COMMAND`. Every failed operation must leave the entire store unchanged.

## Example 1: create, read, overwrite, and delete

Start with a fresh adapter. **Run these calls in order on that same instance.** The output of one call does not become the input to the next.

| Step | Input to `adapter.handle(...)` | Expected return value |
| ---: | --- | --- |
| 1 | `{"op": "set", "key": "colour", "value": "blue"}` | `{"ok": True, "value": None, "error": None}` |
| 2 | `{"op": "get", "key": "colour"}` | `{"ok": True, "value": "blue", "error": None}` |
| 3 | `{"op": "set", "key": "colour", "value": "green"}` | `{"ok": True, "value": None, "error": None}` |
| 4 | `{"op": "get", "key": "colour"}` | `{"ok": True, "value": "green", "error": None}` |
| 5 | `{"op": "delete", "key": "colour"}` | `{"ok": True, "value": None, "error": None}` |
| 6 | `{"op": "get", "key": "colour"}` | `{"ok": False, "value": None, "error": "NOT_FOUND"}` |
| 7 | `{"op": "delete", "key": "colour"}` | `{"ok": False, "value": None, "error": "NOT_FOUND"}` |

## Example 2: errors do not change existing data

Use another fresh adapter and run these calls in order:

| Step | Input to `adapter.handle(...)` | Expected return value |
| ---: | --- | --- |
| 1 | `{"op": "set", "key": "score", "value": 10}` | `{"ok": True, "value": None, "error": None}` |
| 2 | `{"op": "set", "key": "score"}` | `{"ok": False, "value": None, "error": "INVALID_COMMAND"}` |
| 3 | `{"op": "get", "key": "score"}` | `{"ok": True, "value": 10, "error": None}` |
| 4 | `{"op": "clear", "key": "score"}` | `{"ok": False, "value": None, "error": "INVALID_COMMAND"}` |
| 5 | `{"op": "delete", "key": "score", "extra": True}` | `{"ok": False, "value": None, "error": "INVALID_COMMAND"}` |
| 6 | `{"op": "get", "key": "score"}` | `{"ok": True, "value": 10, "error": None}` |
| 7 | `{"op": "get", "key": "missing", "extra": True}` | `{"ok": False, "value": None, "error": "INVALID_COMMAND"}` |
| 8 | `{"op": "get", "key": "missing"}` | `{"ok": False, "value": None, "error": "NOT_FOUND"}` |

Other malformed inputs include `{}`, `{"op": "get", "key": ""}`, `{"op": "get", "key": 123}`, and the string `'not a dictionary'`. Each returns `{"ok": False, "value": None, "error": "INVALID_COMMAND"}`.

## Example 3: a stored `None` is not a missing key

Use a fresh adapter and run these calls in order:

| Step | Input to `adapter.handle(...)` | Expected return value |
| ---: | --- | --- |
| 1 | `{"op": "set", "key": "optional", "value": None}` | `{"ok": True, "value": None, "error": None}` |
| 2 | `{"op": "get", "key": "optional"}` | `{"ok": True, "value": None, "error": None}` |
| 3 | `{"op": "get", "key": "missing"}` | `{"ok": False, "value": None, "error": "NOT_FOUND"}` |

The `ok` and `error` fields distinguish steps 2 and 3. Similarly, values such as `0`, `False`, and `""` are valid stored values and must be returned unchanged.

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

Use the exact contract and examples above when writing your tests. In `NOTES.md`, explain how your implementation satisfies this contract and preserves state on failed commands.

Write your own tests in `tests/test_solution.py`, importing `CommandAdapter` from `solution`. The acceptance checks above are requirements, not implemented tests. See the [test-writing guidance](../../../README.md#writing-your-own-tests).

From this **PE02 folder**, run your tests with:

```sh
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Until you add tests, this command will discover zero tests; that does not indicate a completed exercise.
