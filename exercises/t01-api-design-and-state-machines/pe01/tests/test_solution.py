"""Behavioural tests for PE01's baseline; no private state is inspected."""

import unittest

from solution import ParkingSystem


class ParkingSystemTests(unittest.TestCase):
    def test_original_example(self):
        lot = ParkingSystem(1, 1, 0)
        for car_type, expected in [(1, True), (2, True), (3, False), (1, False)]:
            with self.subTest(car_type=car_type, expected=expected):
                self.assertIs(lot.addCar(car_type), expected)

    def test_zero_capacity_rejects_every_type_repeatedly(self):
        lot = ParkingSystem(0, 0, 0)
        for attempt in range(5):
            for car_type in (1, 2, 3):
                with self.subTest(attempt=attempt, car_type=car_type):
                    self.assertIs(lot.addCar(car_type), False)

    def test_each_type_admits_exactly_its_capacity(self):
        for car_type in (1, 2, 3):
            for capacity in (1, 2, 5):
                with self.subTest(car_type=car_type, capacity=capacity):
                    capacities = [0, 0, 0]
                    capacities[car_type - 1] = capacity
                    lot = ParkingSystem(*capacities)
                    for _ in range(capacity):
                        self.assertIs(lot.addCar(car_type), True)
                    for _ in range(5):
                        self.assertIs(lot.addCar(car_type), False)

    def test_other_sizes_cannot_substitute_for_matching_spaces(self):
        for unavailable_type in (1, 2, 3):
            with self.subTest(unavailable_type=unavailable_type):
                capacities = [2, 2, 2]
                capacities[unavailable_type - 1] = 0
                lot = ParkingSystem(*capacities)
                self.assertIs(lot.addCar(unavailable_type), False)
                self.assertIs(lot.addCar(unavailable_type), False)
                for available_type in (1, 2, 3):
                    if available_type != unavailable_type:
                        self.assertIs(lot.addCar(available_type), True)
                        self.assertIs(lot.addCar(available_type), True)
                        self.assertIs(lot.addCar(available_type), False)

    def test_interleaved_admissions_keep_capacities_independent(self):
        lot = ParkingSystem(2, 1, 3)
        calls = [
            (3, True), (1, True), (2, True), (2, False),
            (3, True), (1, True), (1, False), (3, True), (3, False),
        ]
        for step, (car_type, expected) in enumerate(calls):
            with self.subTest(step=step, car_type=car_type):
                self.assertIs(lot.addCar(car_type), expected)

    def test_instances_do_not_share_state(self):
        first = ParkingSystem(1, 0, 0)
        second = ParkingSystem(1, 0, 0)
        self.assertIs(first.addCar(1), True)
        self.assertIs(first.addCar(1), False)
        self.assertIs(second.addCar(1), True)
        self.assertIs(second.addCar(1), False)
        fresh = ParkingSystem(1, 0, 0)
        self.assertIs(fresh.addCar(1), True)
        self.assertIs(first.addCar(1), False)

    def test_maximum_capacity_accepts_1000_cars(self):
        for car_type in (1, 2, 3):
            with self.subTest(car_type=car_type):
                capacities = [0, 0, 0]
                capacities[car_type - 1] = 1000
                lot = ParkingSystem(*capacities)
                for _ in range(1000):
                    self.assertIs(lot.addCar(car_type), True)

    def test_rejections_remain_false_through_1000_calls(self):
        lot = ParkingSystem(1, 0, 0)
        self.assertIs(lot.addCar(1), True)
        for _ in range(999):
            self.assertIs(lot.addCar(1), False)


if __name__ == "__main__":
    unittest.main()
