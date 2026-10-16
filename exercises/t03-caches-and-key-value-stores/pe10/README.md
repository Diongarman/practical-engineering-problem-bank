# PE10 · 146. LRU Cache

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T03 · Caches and key-value stores |
| Practice order | 12 of 48 |
| Difficulty | Medium |
| Starter | Yes |
| Prerequisites | [PE09](../../../exercises/t03-caches-and-key-value-stores/pe09/README.md) |
| Source | LeetCode |
| Platform rating | Medium |

## Task and interface

Implement the original get and put API with positive capacity. Accessing or updating a key makes it most recently used. Inserting past capacity evicts the least recently used key. Meet average O(1) operation requirements.

## Acceptance checks

1. A get changes the next eviction choice.
2. Updating an existing key does not increase cache size.
3. Missing keys return the original sentinel.
4. Capacity one evicts the correct key.

## Python tools

OrderedDict; later dict plus doubly linked list

## Optional follow-up

Make both get and put thread-safe. Add counters for hits, misses and evictions.

## Reference

[Problem statement](https://leetcode.com/problems/lru-cache/)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
