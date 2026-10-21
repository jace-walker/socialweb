# this file will create the class Town and its methods, and contain create_trait_dictionary

import numpy as np
from agent import Agent
from config import (
    LIST_OF_NAMES,
    LIST_OF_TRAITS,
    BELL_CURVE_MEAN,
    BELL_CURVE_SPREAD
)


class Town:
    def __init__(self, population):
        """Create class Town"""
        self.population = {}



    def setup(self):
        pass










def create_traits_dictionary():
    
    example_dictionary = {}
    
    for trait in LIST_OF_TRAITS:
        random_value = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
        np.clip(random_value, 0, 1)
    
        example_dictionary[trait] = random_value
    
    return example_dictionary