# Practice conventions

## Working on an exercise

Follow the ordered index in the root README and use stable IDs such as `PE01` in notes and commits. Each exercise has its own `src/` and `tests/` folders so implementations can evolve independently.

When beginning an exercise, use `src/solution.py` for a small implementation and `tests/test_solution.py` for its tests. Split files only when useful. The `.gitkeep` files simply preserve empty directories; remove them when adding real files. PE01 includes an unfinished solution scaffold and baseline tests; the other exercises start empty.

Use the exercise's public contract and acceptance criteria. Add behavioural tests as you implement functionality. Copy `docs/design-note-template.md` into the exercise as `NOTES.md` and fill it in yourself.

## Running tests once you have written them

From an exercise directory, for standard-library `unittest` tests importing `solution` from `src/`:

```sh
PYTHONPATH=src python -m unittest discover -s tests -p 'test_*.py' -v
```

PowerShell equivalent:

```powershell
$env:PYTHONPATH = 'src'
python -m unittest discover -s tests -p 'test_*.py' -v
```

These commands assume the environment described in the README is active. PE01 has baseline tests; untouched exercises contain zero tests. A zero-test run is not evidence that an exercise is complete. There is no repository-wide test runner or CI yet.

## Tracking practice

Update `data/problems.csv`: Status, Practice attempts, Last practised, and Notes. Keep stable IDs, original order, prerequisites, source, and platform rating intact. Use dates such as `2026-10-16`. Mark an exercise complete only after its acceptance checks pass and you can explain the implementation.

The topic progress and README completion total are static initial values; update them manually if you want a current summary. CSV fields containing commas or line breaks must remain quoted correctly.

## Scope

Keep optional follow-ups separate from the baseline. Avoid adding dependencies or shared abstractions before an exercise needs them. Do not commit virtual environments, local secrets, bytecode, or generated test output.
