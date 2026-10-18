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

        self.agent_id = agent_id        # unique agent id starting from 0 to number of agents
        self.name = name                # agent's name, useless for statistics, just to make more human
        self.traits = traits            # list of four traits that are being tested
        self.trust = {}                 # dictionary that will contain trust rating for every OTHER agent
        self.met = set()                # create empty set for which who Agent has interacted with DIRECTLY
        self.resources = 10              # if money is a measure of success for you, then this is the agent's success. starting with 10 money.
        self.was_cheated = 0            # counter for how many times Agent was cheated by someone else
        self.did_cheating = 0           # counter for how many times Agent did the cheating against someone else

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

    MAYA = Agent(11, 'Maya', create_traits_dictionary())
    LEO = Agent(12, 'Leo', create_traits_dictionary())


    MAYA.met.add('Leo')
    print(MAYA.met)
    print(LEO.met)
    print(MAYA.resources)
    print(MAYA.traits)
        






def create_traits_dictionary():
    
    example_dictionary = {}
    
    for trait in LIST_OF_TRAITS:
        random_value = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
        np.clip(random_value, 0, 1)
    
        example_dictionary[trait] = random_value
    
    return example_dictionary
    







if __name__ == '__main__':
    main()
