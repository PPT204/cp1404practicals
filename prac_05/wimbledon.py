"""
Wimbledon
Estimate: 25 minutes
Actual:
"""

FILENAME = "wimbledon.csv"

def main():
    """Read data from file and display champions and their countries."""
    data = read_wimbledon_data(FILENAME)


def read_wimbledon_data(filename):
    """Read the Wimbledon CSV file and return data excluding the header."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]  # skip header
    data = [line.strip().split(",") for line in lines]
    return data