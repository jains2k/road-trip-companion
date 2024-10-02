from crewai import Task
from textwrap import dedent


"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""
class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    
    def find_unique_restaurants(self, agent, city, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**: Find Unique or Highly Rated Restaurants
                    **Description**: Find unique or highly rated restaurants in the city that match the traveler's food preferences. 
                        You MUST suggest actual restaurants with detailed menus and reviews. 
                        The agent should also provide a detailed description of the restaurant, including price, location, and ambiance.

                    **Parameters**: 
                    - City: {city}
                    - Traveler Interests: {interests}

                    **Note**: {self.__tip_section()}
                """
            ),
            expected_output=""" A list of unique or highly rated restaurants in the city with name, cusiness, price, location, and rating.

                Example:
                [{
                    "name": "Restaurant Name",
                    "cuisine": "Multicuisine",
                    "price": "$$",
                    "location": "Cupertino, CA",
                    "rating": "4.5"
                }]

            """,
            async_execution=True,
            agent=agent,
        )
    
    def find_unique_attractions(self, agent, city, interests): #, context):
        #                        For outdoor activities, use the weather forecast to update suggestions.
        return Task(
            description=dedent(
                f"""
                    **Task**: Find Unique or Highly Rated Attractions
                    **Description**: Find unique or highly rated attractions in the city that match the traveler's interests. 
                        You MUST suggest actual attractions with detailed descriptions. If there are tickets that apply, add pricing details in the descriptio and actual price for adults in the output.
                        If there is a special event in the city, include it in the description.
                        The agent should also provide a detailed description of the attraction, including location, price, and accessibility.

                    **Parameters**: 
                    - City: {city}
                    - Traveler Interests: {interests}

                    **Note**: {self.__tip_section()}
                """
            ),
            expected_output=""" A list of unique or highly rated attractions in the city with name, description, price (if any), location, and rating.

                Example:
                [{
                    "name": "Attraction Name",
                    "description": "Attraction Description",
                    "price": "$$",
                    "location": "Cupertino, CA",
                    "rating": "4.5",
                    "weather": "appropriate weather"
                }, {
                    "name": "Wine tasting",
                    "description": "Outdoor wine tastings in the city",
                    "price": "$$",
                    "location": "Fremont, CA",
                    "rating": "4.5",
                    "weather": "rains predicted"
                }]
            """,
            async_execution=False,
            #context=context,
            agent=agent,
        )

    def check_weather_forecast(self, agent, city, interests):
            return Task(
                description=dedent(
                    f"""
                        **Task**:  Check the Weather Forecast
                        **Description**: Check the weather forecast for the selected city for today and provide a detailed description of the forecast. 
                            You MUST provide a detailed description of the weather conditions, including any specific weather events or changes.

                        **Parameters**: 
                        - City: {city}
                        - Traveler Interests: {interests}

                        **Note**: {self.__tip_section()}    
            """
                ),
                agent=agent,
                async_execution=False
            )

    def task_manager(self, agent, context):
            #and the weather forecast
            return Task(
                description=dedent(
                    f"""
                        **Task**: Give suggestions for best food and activities doable in 1-4 hour window from current time.
                        **Description**: Combine the restaurant suggestions and unique / highly rated attraction suggestions and give four suggestions each - one for food and one for local attractions or events.
                        When suggesting local attractions or events, make sure to take into consideration the current time of day.

                        **Note**: {self.__tip_section()}
            """
                ),
                expected_output=""" A list of four suggestions for food and activities.
                    Example:
                    {
                        "restaurants": [{
                            "name": "Restaurant Name",
                            "cuisine": "Multicuisine",
                            "price": "$$",
                            "location": "Cupertino, CA",
                            "rating": "4.5"
                        }],
                        "attractions": [{
                            "name": "Attraction Name",
                            "description": "Attraction Description",
                            "price": "$$",
                            "location": "Cupertino, CA",
                            "rating": "4.5",
                            "weather": "appropriate weather"
                        }, {
                            "name": "Wine tasting",
                            "description": "Outdoor wine tastings in the city",
                            "price": "$$",
                            "location": "Fremont, CA",
                            "rating": "4.5",
                            "weather": "rains predicted"
                        }]
                    }

                """,
                agent=agent,
                context=context,
                async_execution=False
            )