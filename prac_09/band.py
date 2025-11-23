"""Band class for CP1404."""

from musician import Musician


class Band:
    """Band class that manages a collection of Musicians."""

    def __init__(self, name: str = "") -> None:
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians: list[Musician] = []

    def __str__(self) -> str:
        """Return string representation of the Band."""
        # Join each Musician's string representation
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add(self, musician: Musician) -> None:
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self) -> str:
        """Return a string of each Musician's play() result on separate lines."""
        return "\n".join(musician.play() for musician in self.musicians)
