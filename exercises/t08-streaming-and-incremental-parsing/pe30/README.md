# PE30 · Incremental UTF-8 line parser

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T08 · Streaming and incremental parsing |
| Practice order | 27 of 48 |
| Difficulty | Medium |
| Starter | No |
| Prerequisites | [PE29](../../../exercises/t08-streaming-and-incremental-parsing/pe29/README.md), [PE05](../../../exercises/t02-queues-and-backpressure/pe05/README.md) |
| Source | Custom |
| Platform rating | n.a. |

## Task and interface

Implement feed(bytes_chunk) -> list[str] and finish() -> list[str]. Decode UTF-8 incrementally and emit complete newline-delimited records, preserving a partial final line. Choose and document strict invalid-UTF-8 behaviour. Enforce a configurable maximum line length.

## Acceptance checks

1. Splitting a multibyte character across chunks still decodes it.
2. One-byte chunks and one large chunk yield identical lines.
3. finish emits a final unterminated line once.
4. Invalid bytes and oversized lines produce the documented error.

## Python tools

codecs incremental decoder, buffers, generators

## Optional follow-up

Parse JSON Lines and report bad records with line numbers without losing later valid records.

## Reference

[Python reference](https://docs.python.org/3/library/codecs.html)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
