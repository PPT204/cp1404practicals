import random
from car import Car


class UnreliableCar(Car):
    """Specialised Car that may fail to drive."""

    def __init__(self, name: str, fuel: float, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability
