# create a class Agent and run super basic sim of just two agents

import numpy as np

# constants mostly for later
NUM_OF_AGENTS = 0       # change later
SEED = 42
LIST_OF_TRAITS = ['extraversion', 'agreeableness', 'neuroticism', 'honesty']
BELL_CURVE_MEAN = 0.5
BELL_CURVE_SPREAD = 0.15


class Agent:
# this class creates an Agent. only agent_id, name, and trait dictionary for now

    def __init__(self, agent_id, name, traits):
        self.agent_id = agent_id
        self.name = name
        self.traits = traits
        self.trust = {}


def main():

    maya_traits = {
    "extraversion": 0.8,
    "agreeableness": 0.6,
    "neuroticism": 0.7,
    "honesty": 0.8, 
    }

    MAYA = Agent(1, 'Maya', maya_traits)
    MAYA.trust[1] = 0.7

    leo_traits = {
        "extraversion": 0.7,
        "agreeableness": 0.3,
        "neuroticism": 0.4,
        "honesty": 0.6,
    }

    LEO = Agent(2, 'Leo', leo_traits)

    print(LEO.name)
    print(MAYA.agent_id)
    print(LEO.traits['honesty'])
    print(MAYA.trust)
    print(LEO.trust)





main()
