from guitar import Guitar


def main():
    guitars = [
        Guitar("Fender Stratocaster", 2014, 765.40),
        Guitar("Gibson L-5 CES", 1922, 16035.40),
        Guitar("Line 6 JTV-59", 2010, 1512.90),
    ]

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


if __name__ == "__main__":
    main()
