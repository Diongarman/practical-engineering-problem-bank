# PE32 · Incremental streaming tokenizer

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T08 · Streaming and incremental parsing |
| Practice order | 40 of 48 |
| Difficulty | Hard |
| Starter | No |
| Prerequisites | [PE30](../../../exercises/t08-streaming-and-incremental-parsing/pe30/README.md), [PE29](../../../exercises/t08-streaming-and-incremental-parsing/pe29/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Build a UTF-8 byte-stream tokenizer. Define tokens as maximal runs of non-whitespace characters. Emit a token only when its delimiter or end of stream arrives. Retain only decoder state and the partial token. Reject tokens longer than a configurable limit.

## Acceptance checks

1. Splitting at every byte boundary preserves the token sequence.
2. Whitespace-only input emits no tokens.
3. End of stream flushes the last token once.
4. Memory does not grow with completed input.

## Python tools

codecs, iterators, generators, profiling

## Optional follow-up

Add token timestamps and compare streaming latency with whole-input buffering.

## Reference

[Python reference](https://docs.python.org/3/library/codecs.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
