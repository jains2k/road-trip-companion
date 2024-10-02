from fastapi import FastAPI
from pydantic import BaseModel
from models import Trip
from models import Restaurant
from models import Attraction
from models import TripAdvise
from models import tripAdvise
from typing import List

# Initialize the FastAPI app
app = FastAPI()

# Define a GET route
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a POST route
@app.post("/trips/")
def create_trip(trip: Trip):
    return {"location": trip.location, "food_choice": trip.food_choice, "interests": trip.interests, "id": 100}

@app.get("/trip_advise/{id}")
def get_trip_advise(id: int):
    return tripAdvise

