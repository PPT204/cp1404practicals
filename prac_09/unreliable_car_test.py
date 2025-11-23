from unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Reliable", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 9)

    print("Attempting to drive each car 10 km, 10 times:\n")
    for attempt in range(1, 11):
        reliable_distance = reliable_car.drive(10)
        unreliable_distance = unreliable_car.drive(10)
        print(
            f"Attempt {attempt:2}: "
            f"{reliable_car.name} drove {reliable_distance:2} km, "
            f"{unreliable_car.name} drove {unreliable_distance:2} km"
        )

    print("\nFinal car states:")
    print(reliable_car)
    print(unreliable_car)


if __name__ == "__main__":
    main()
