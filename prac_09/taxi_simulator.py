"""
CP1404 - Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    bill_to_date = 0

    menu = "q)uit, c)hoose taxi, d)rive"

    print(menu)
    user_choice = input(">>> ").lower()

    while user_choice != "q":
        if user_choice == "c":
            current_taxi = choose_taxi(taxis)

        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date += drive_taxi(current_taxi)

            print(f"Bill to date: ${bill_to_date:.2f}")

        else:
            print("Invalid option")

        print(menu)
        user_choice = input(">>> ").lower()

    # Quit → show final bill + all taxi states
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Display taxis and let user choose one."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    try:
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice < 0 or taxi_choice >= len(taxis):
            print("Invalid taxi choice")
            return None
        return taxis[taxi_choice]
    except ValueError:
        print("Invalid taxi choice")
        return None

def drive_taxi(taxi):
    """Ask distance, drive taxi, return trip cost."""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0

    taxi.start_fare()
    taxi.drive(distance)

    trip_cost = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost


main()