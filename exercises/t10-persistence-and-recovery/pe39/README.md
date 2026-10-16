# PE39 · Transactional idempotent ledger

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T10 · Persistence and recovery |
| Practice order | 32 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE33](../../../exercises/t09-retries-and-failure-handling/pe33/README.md), [PE37](../../../exercises/t10-persistence-and-recovery/pe37/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Use SQLite to implement credit(account_id,request_id,amount). Create account balances and uniquely keyed successful-operation records. Balance change and receipt insertion occur in one transaction. Identical retries return the saved receipt; conflicting reuse of a request ID is rejected.

## Acceptance checks

1. Identical retries change the balance once.
2. Injected failure before commit changes neither balance nor receipt.
3. A conflicting amount under the same request ID is rejected.
4. Restart preserves balances and successful receipts.

## Python tools

sqlite3, transactions, UNIQUE constraints, context managers

## Optional follow-up

Add concurrent writers using separate connections and define bounded handling of busy/locked errors.

## Reference

[Python reference](https://docs.python.org/3/library/sqlite3.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
