from pydantic import BaseModel
from typing import List

# Define the Restaurant model
class Restaurant(BaseModel):
    name: str
    cuisine: str
    price: str
    location: str
    rating: float

# Define the Attraction model
class Attraction(BaseModel):
    name: str
    description: str
    price: str
    location: str
    rating: float
    weather: str

# Define the Trip model
class Trip(BaseModel):
    location: str
    food_choice: str
    interests: str

# Define the main model that contains both restaurants and attractions
class TripAdvise(BaseModel):
    restaurants: List[Restaurant]
    attractions: List[Attraction]

# Example usage with JSON data
data = {
    "restaurants": [
        {
            "name": "The Modern Vegan",
            "cuisine": "Vegan/Vegetarian",
            "price": "$$",
            "location": "1670 E Flamingo Rd, Las Vegas, NV 89119",
            "rating": "4.5"
        },
        {
            "name": "Chef Kenny's Vegan Dim Sum",
            "cuisine": "Chinese/Vegan",
            "price": "$$",
            "location": "3025 S Jones Blvd #102, Las Vegas, NV 89146",
            "rating": "4.7"
        },
        # More restaurants...
    ],
    "attractions": [
        {
            "name": "Bellagio Fountains",
            "description": "The Bellagio Fountains feature a stunning water show set to music and lights, occurring every 30 to 15 minutes. A must-see experience in Las Vegas.",
            "price": "Free",
            "location": "Bellagio Hotel & Casino, 3600 S Las Vegas Blvd, Las Vegas, NV 89109",
            "rating": "4.8",
            "weather": "Clear skies, perfect for an outdoor show"
        },
        {
            "name": "The Mirage Volcano",
            "description": "Experience the free volcano show at The Mirage, erupting with fire and water every hour from 7 PM to 11 PM. A thrilling spectacle combining music and pyrotechnics.",
            "price": "Free",
            "location": "The Mirage Hotel, 3400 S Las Vegas Blvd, Las Vegas, NV 89109",
            "rating": "4.4",
            "weather": "Clear skies, ideal for evening shows"
        },
        # More attractions...
    ]
}

# Create an instance of CityGuide
tripAdvise = TripAdvise(**data)
