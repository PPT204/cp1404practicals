"""
Wimbledon
Estimate: 25 minutes
Actual:
"""

FILENAME = "wimbledon.csv"

def main():
    """Read data from file and display champions and their countries."""
    data = read_wimbledon_data(FILENAME)
    champion_to_wins, countries = process_wimbledon_data(data)

def read_wimbledon_data(filename):
    """Read the Wimbledon CSV file and return data excluding the header."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]  # skip header
    data = [line.strip().split(",") for line in lines]
    return data

def process_wimbledon_data(data):
    """Process data into a dictionary of champions to wins, and a set of countries."""
    champion_to_wins = {}
    countries = set()
    for record in data:
        champion = record[2]
        country = record[1]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
        countries.add(country)
    return champion_to_wins, countries