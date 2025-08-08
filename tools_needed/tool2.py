from agents import function_tool
import random

@function_tool
def suggest_hotels(destination: str)-> list[dict]:
    """
    Suggests mock hotels in the given destination and suggest a list of hotels with name, rating, and price per night.
    """
    hotel_names = [
        "Grand Stay", "Urban Oasis", "Sunset Inn", "City Comfort", "Panorama Hotel",
        "Serenity Suites", "Vista Palace", "Royal Nest", "Harmony Rooms"
    ]

    hotels = []
    for _ in range(2):
        name = random.choice(hotel_names)
        rating = round(random.uniform(3.5, 5.0), 1)
        price = f"${random.randint(70, 200)}/night"

        hotels.append({
            "name": f"{destination} {name}",
            "rating": str(rating),
            "price": price
        })

    hotels.append({
        "name": "NOTE",
        "rating": "⚠️ This is mock data for testing purposes only.",
        "price": "N/A"
    })

    return hotels
