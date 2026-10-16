# PE38 · Atomic file checkpoint

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T10 · Persistence and recovery |
| Practice order | 31 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE37](../../../exercises/t10-persistence-and-recovery/pe37/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement save_snapshot(state,path) and load_snapshot(path). Write a temporary file in the destination directory, then replace the destination after serialization succeeds. Inject failures before replacement. Support one writer and describe the scope of crash guarantees.

## Acceptance checks

1. Serialization failure leaves the previous snapshot intact.
2. Restart after replacement loads the complete new state.
3. Failure before replacement loads the old state.
4. Temporary files are cleaned up after handled failures.

## Python tools

tempfile, json, os.replace, pathlib

## Optional follow-up

Investigate flush/fsync and directory syncing for stronger power-loss durability.

## Reference

[Python reference](https://docs.python.org/3/library/os.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
