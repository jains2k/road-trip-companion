from crewai import Crew, Process
from textwrap import dedent
from agents import RoadTripCompanion
from tasks import TravelTasks
from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv
load_dotenv()
os.environ["OTEL_SDK_DISABLED"] = "true"

# This is the main class that launches the crew.

class RoadTripCrew:
    def __init__(self, cities, interests, food_choice):
        self.cities = cities
        self.interests = interests
        self.food_choice = food_choice

        self.OpenAIGPT4o = ChatOpenAI(
            model="gpt-4o-mini", temperature=0.7)

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = RoadTripCompanion()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        road_trip_companion = agents.road_trip_companion()
        foodie = agents.foodie()
        weatherman = agents.weatherman()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        find_restaurants = tasks.find_unique_restaurants(
            foodie,
            self.cities,
            self.food_choice
        )

        check_weather = tasks.check_weather_forecast(
            weatherman,
            self.cities,
            self.interests
        )

        find_unique_attractions = tasks.find_unique_attractions(
            local_tour_guide,
            self.cities,
            self.interests
            #context=[check_weather]
        )

        task_manager = tasks.task_manager(
            road_trip_companion,
            context=[find_restaurants, find_unique_attractions]
        )

        # Define your custom crew here
        crew = Crew(
            agents=[foodie, local_tour_guide, road_trip_companion],
            tasks=[find_restaurants, find_unique_attractions, task_manager],
            process=Process.sequential,
            manager_llm=self.OpenAIGPT4o,
            verbose=True,
            share_crew=False,
            max_rpm=1
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Road Trip Companion")
    print('-------------------------------')
    cities = input(
        dedent("""
      Which place are you looking to find about?
    """))
    interests = input(
        dedent("""
      What are some of your high level interests and hobbies?
    """))
    food_choice = input(
        dedent("""
      What type of food are you interested in? 
    """))

    trip_crew = RoadTripCrew(cities, interests, food_choice)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here are your visit options")
    print("########################\n")
    print(result)