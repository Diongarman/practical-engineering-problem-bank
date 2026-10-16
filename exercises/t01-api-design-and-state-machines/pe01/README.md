# PE01 · 1603. Design Parking System

[← Curriculum and exercise order](../../../README.md#exercise-order)

| Field | Value |
| --- | --- |
| Topic | T01 · API design and state machines |
| Practice order | 1 of 48 |
| Difficulty | Easy |
| Starter | Yes |
| Prerequisites | None |
| Source | LeetCode |
| Platform rating | Easy |

## Task and interface

Implement ParkingSystem(big, medium, small) and addCar(carType). Track remaining spaces for each type. Return a boolean indicating whether a car was admitted. Follow the original input contract.

## Acceptance checks

1. A type with zero capacity rejects a car.
2. Admitting a car consumes exactly one matching space.
3. Repeated calls never make remaining capacity negative.

## Python tools

Classes, list or dict, unittest

## Optional follow-up

Add invalid-input handling and a thread-safe check-and-decrement. Two workers competing for one space must produce one success.

## Reference

[Problem statement](https://leetcode.com/problems/design-parking-system/)

## Workspace

- `src/` — add your implementation when you begin.
- `tests/` — add behavioural tests when you begin.
- `NOTES.md` — create from the [design-note template](../../../docs/design-note-template.md).

Track status and attempts in [problems.csv](../../../data/problems.csv).

## Starting the exercise

Fill in the two methods in [src/solution.py](src/solution.py). Both currently raise `NotImplementedError`; no solution is provided.

The baseline contract uses car types **1 = big, 2 = medium, 3 = small**, capacities from **0 to 1000**, and at most **1000 calls per instance**. A car can only use its matching space type. See the linked original problem statement above.

From this exercise directory, run:

```sh
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
```

[tests/test_solution.py](tests/test_solution.py) covers the original example, zero/full capacity, exact admission counts, type isolation, interleaved calls, independent instances, and the upper input limits. Assertions require actual booleans and inspect only the public API. Invalid inputs and concurrency belong to the optional follow-up and are not tested here.

The tests are expected to fail with `NotImplementedError` until you complete the methods. Repeated rejection checks verify observable full-lot behaviour; they do not inspect your internal capacity representation.
