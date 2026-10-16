# PE29 · Exercism Word Count

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T08 · Streaming and incremental parsing |
| Practice order | 14 of 48 |
| Difficulty | Easy |
| Starter | No |
| Prerequisites | None |
| Source | Exercism |
| Platform rating | Easy |

## Task and interface

Complete the original Python Word Count exercise. Count ASCII words case-insensitively, keep internal apostrophes in contractions, treat numbers as words, and handle punctuation and whitespace separators.

## Acceptance checks

1. Different capitalisation merges into one word count.
2. Contractions stay intact.
3. Punctuation and multiple whitespace forms separate words.
4. Result ordering does not affect correctness.

## Python tools

re, Counter, strings, unittest

## Optional follow-up

Turn the input into chunks and preserve a partial final word between chunks.

## Reference

[Problem statement](https://exercism.org/tracks/python/exercises/word-count)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
