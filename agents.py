from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class RoadTripCompanion:
    def __init__(self):
        self.OpenAIGPT4o = ChatOpenAI(
            model="gpt-4o-mini", temperature=0.7)

    def foodie(self): 
        return Agent(
            role="Foodie",
            backstory=dedent(f"""
            I'm a food enthusiast with a deep knowledge of local cuisine.
            I can recommend the best places to eat and drink in the city.
            """),
            goal=dedent(f"""
            Provide recommendations for the best local food and drink spots and unique food eating experinces, if available, in the area.
            """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4o,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""
            I'm a local expert with extensive knowledge of the city, town or place.
            I can provide information about local history, landmarks, and hidden gems.
            """),
            goal=dedent(f"""
            Provide information about local history, landmarks, and hidden gems.
            """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4o,
        )

    def weatherman(self): 
        return Agent(
            role="Weatherman",
            backstory=dedent(f"""
            I am a weather expert with extensive knowledge of the city, town or place and its tourist spots.
            """),
            goal=dedent(f"""
            Provide hourly forecasts for the selected city, for current day, town or place and tourist spots around it, including wind chills 
            and visibility, heat waves, rain, snow, and other tourism impacting information.
            """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4o,
        )

    def road_trip_companion(self):
        return Agent(
            role="Road Trip Companion",
            backstory=dedent(f"""
            Road trip companion that shares inights into the place the user is in, 
            and its local history, culture, unique food and drink experiences, unique places to visit.
            """),
            goal=dedent(f"""
            Collect information from other agents and give recommendations on places to visit and restaurants to go to in the selected city, town or place.
                        For places to visit also include weather information especially if they may impact the visit.
            """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4o,
    )
