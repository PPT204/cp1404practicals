from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Car that sometimes fails to drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(fuel)
        self.name = name
        self.reliability = reliability

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}, reliability={self.reliability}%"

    def drive(self, distance):
        """Drive only if random check passes."""
        if random.uniform(0, 100) < self.reliability:
            # drive normally
            return super().drive(distance)
        else:
            # unreliable car fails to move
            return 0
