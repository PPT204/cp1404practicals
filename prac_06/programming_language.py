"""
ProgrammingLanguage class
Estimate: 10 minutes
Actual:
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """Initialise a ProgrammingLanguage."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:
        """Return a human-readable representation of the language."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")

