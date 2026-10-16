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

Track status and attempts in [problems.csv](../../../data/problems.csv). This workspace starts empty; the acceptance checks above are requirements, not implemented tests.
