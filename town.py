# this file will create the class Town and its methods, and contain create_trait_dictionary

import numpy as np
from agent import Agent
from config import (

    NUM_OF_AGENTS,
    LIST_OF_NAMES,
    LIST_OF_TRAITS,
    BELL_CURVE_MEAN,
    BELL_CURVE_SPREAD,
    rng
)


class Town:

    def __init__(self):
        """Create class Town"""
        self.population = {}
        self.day_count = 1              # day counter starts at day 1



    def setup(self):
        """This method will create a population inside the town's dictionary named 'population' """

        for i in range(NUM_OF_AGENTS):
            self.population[i] = Agent(i, LIST_OF_NAMES[i], create_traits_dictionary())



    def step_day(self):
        """This method creates a list of ID's to loop through and calcuate each agent's interaction count for that day"""

        today_ids = list(self.population.keys())
        rng.shuffle(today_ids)


        for i in today_ids:
            current_agent = self.population[i]

            turn_count = current_agent.calculate_interactions()

            for turn in range(turn_count):
                print(f"Day {self.day_count}: {current_agent.name}, turn {turn+1} of {turn_count}.")

        self.day_count += 1

        








def create_traits_dictionary():
    
    example_dictionary = {}
    
    for trait in LIST_OF_TRAITS:
        random_value = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
        np.clip(random_value, 0, 1)
    
        example_dictionary[trait] = random_value
    
    return example_dictionary