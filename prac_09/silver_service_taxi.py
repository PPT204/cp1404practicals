"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness multiplier and flagfall charge."""

    flagfall = 4.50

    def __init__(self, name: str, fuel: int, fanciness: float) -> None:
        """Initialise a SilverServiceTaxi with base Taxi data and fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Start from the shared Taxi price_per_km then scale it
        self.price_per_km *= fanciness

    def get_fare(self) -> float:
        """Return the price for the taxi trip, rounded to nearest 10c."""
        fare = self.price_per_km * self.current_fare_distance
        return round(fare, 1)

    def __str__(self) -> str:
        """Return string like Taxi but with flagfall information."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
