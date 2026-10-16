"""PE01: complete the ParkingSystem implementation below."""


class ParkingSystem:
    """A parking lot with separate capacities for three car types.

    Car types: 1 = big, 2 = medium, 3 = small.
    Each car must use a space matching its type.
    """

    def __init__(self, big: int, medium: int, small: int) -> None:
        """Initialise the lot with capacities in the range 0 through 1000."""
        # TODO: Decide how to represent this instance's parking state.
        raise NotImplementedError("Implement ParkingSystem.__init__")

    def addCar(self, carType: int) -> bool:
        """Admit a car if a matching space is available.

        Return True on admission, or False when that type is full.
        The caller supplies a valid carType (1, 2, or 3).
        """
        # TODO: Implement the admission contract.
        raise NotImplementedError("Implement ParkingSystem.addCar")
