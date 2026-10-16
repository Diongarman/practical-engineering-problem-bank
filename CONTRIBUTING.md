# Repository conventions

For the complete practice workflow and CLI commands, follow the README:

- [Getting started](README.md#getting-started)
- [Writing your own tests](README.md#writing-your-own-tests)
- [Finishing an exercise](README.md#finishing-an-exercise)

## File conventions

Use stable exercise IDs such as `PE01` in notes and commits. Keep each exercise's implementation and tests in its own folder so exercises can evolve independently.

Use `src/solution.py` and `tests/test_solution.py` for small exercises; split them into more files only when useful. The `.gitkeep` files preserve empty directories in Git and can be removed when real files are added.

## Editing curriculum data

In `data/problems.csv`, keep stable IDs, original order, prerequisites, source, and platform rating intact when updating practice records. Use `YYYY-MM-DD` dates, such as `2026-10-16`. Preserve CSV quoting for fields containing commas or line breaks.

The files in `data/` are local records, not a live connection to Google Drive. See [source details](docs/source.md) for their origin and mapping to the workbook.

## Repository housekeeping

Add dependencies or shared abstractions when an exercise needs them. Keep virtual environments, local secrets, bytecode, and generated test output out of commits. There is no repository-wide test runner or CI workflow configured yet.
