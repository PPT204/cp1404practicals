"""
CP1404/CP5632 Practical
Test SilverServiceTaxi
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi functionality."""
    # Example from prac notes: 18 km trip, fanciness 2
    hummer = SilverServiceTaxi("Hummer", fuel=200, fanciness=2)
    hummer.start_fare()
    hummer.drive(18)
    fare = hummer.get_fare()
    print(hummer)
    print(f"Fare for 18 km trip is ${fare:.2f}")

    # After rounding to nearest 10c, this should be 48.80
    assert fare == 48.8, f"Expected 48.8, got {fare}"


if __name__ == "__main__":
    main()
