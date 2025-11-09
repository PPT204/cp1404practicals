from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    guitars.sort()
    show_guitars(guitars)

    add_new_guitars(guitars)
    guitars.sort()
    print("\nUpdated (sorted) list:")
    show_guitars(guitars)

    save_guitars("guitars.csv", guitars)
    print("\nSaved to guitars.csv")

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

def add_new_guitars(guitars: list[Guitar]) -> None:
    """Prompt for new guitars and append to the list until blank name."""
    print("\nAdd new guitars (blank name to stop).")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ").strip()

def save_guitars(filename: str, guitars: list[Guitar]) -> None:
    """Write all guitars to CSV (Name,Year,Cost)."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for g in guitars:
            out_file.write(f"{g.name},{g.year},{g.cost}\n")

if __name__ == "__main__":
    main()
