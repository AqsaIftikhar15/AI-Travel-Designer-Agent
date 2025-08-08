from agents import function_tool
import random

@function_tool
def get_flights(destination: str) -> list[dict]:
    """
    Simulates mock flight options to a given destination and give a list of mock flight options including airline, price, and times.
    """
    airlines = ["AirwayX", "FlyHigh", "GlobalJet", "SkyBridge", "NimbusAir"]
    flight_options = []

    for _ in range(2):
        airline = random.choice(airlines)
        price = f"${random.randint(300, 900)}"
        departure_hour = random.randint(1, 12)
        arrival_hour = (departure_hour + random.randint(5, 10)) % 12 or 12
        am_pm_dep = random.choice(["AM", "PM"])
        am_pm_arr = "AM" if am_pm_dep == "PM" else "PM"

        flight = {
            "airline": airline,
            "price": price,
            "departure": f"{departure_hour}:00 {am_pm_dep}",
            "arrival": f"{arrival_hour}:00 {am_pm_arr}",
            "destination": destination
        }
        flight_options.append(flight)

    # Append disclaimer message
    flight_options.append({
        "airline": "NOTE",
        "price": "This is mock data",
        "departure": "N/A",
        "arrival": "N/A",
        "destination": destination
    })

    return flight_options
