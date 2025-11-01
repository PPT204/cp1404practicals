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
