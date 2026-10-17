# create a class Agent and run super basic sim of just two agents

import numpy as np

# constants mostly for later
NUM_OF_AGENTS = 10    
SEED = 21
LIST_OF_TRAITS = ['extraversion', 'agreeableness', 'neuroticism', 'honesty']
BELL_CURVE_MEAN = 0.5
BELL_CURVE_SPREAD = 0.15

LIST_OF_NAMES = [
    'Jon', 'Mark', 'Meagan', 'Debby', 'Damien', 
    'Josh', 'Kenzie', 'Brick', 'Ash', 'Kevin' ]

rng = np.random.default_rng(SEED)


class Agent:
# this class creates an Agent. only agent_id, name, and trait dictionary for now

    def __init__(self, agent_id, name, traits):
        self.agent_id = agent_id
        self.name = name
        self.traits = traits
        self.trust = {}

    def __repr__(self):
        return f"Agent({self.agent_id}, {self.name})"

    def __str__(self):
        pieces = []

        for trait in LIST_OF_TRAITS:
            score = self.traits[trait]
            pieces.append(f"{trait[0].upper()} {score:.2f}")
        traits_text = " ".join(pieces)
        return f"{self.agent_id}, {self.name:<8} {traits_text}"

        


def main():

    town = {}

    for n in range(NUM_OF_AGENTS):
        town[n] = Agent(n, LIST_OF_NAMES[n], create_traits_dictionary())

    for agent in town.values():
        print(agent)
        






def create_traits_dictionary():
    
    example_dictionary = {}
    
    for trait in LIST_OF_TRAITS:
        random_value = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
        np.clip(random_value, 0, 1)
    
        example_dictionary[trait] = random_value
    
    return example_dictionary
    




main()
