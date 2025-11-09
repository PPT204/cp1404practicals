from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    show_guitars(guitars)


def load_guitars(filename: str) -> list[Guitar]:
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars: list[Guitar] = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            name, year_text, cost_text = line.strip().split(",")
            year = int(year_text)
            cost = float(cost_text)
            guitars.append(Guitar(name, year, cost))
    return guitars


def show_guitars(guitars: list[Guitar]) -> None:
    """Print guitars in the sample’s aligned format (unsorted for now)."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")

if __name__ == "__main__":
    main()
