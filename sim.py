# JACE WALKER'S LIFEWORK!!


import numpy as np


# imported Agent class from agent.py
from agent import Agent

# imported Town class from town.py
from town import Town


# importing all constants from config.py
from config import (
    NUM_OF_AGENTS,
    SEED,
    BELL_CURVE_MEAN,
    BELL_CURVE_SPREAD,
    DEFAULT_TRUST,
    COOPERATE,
    CHEAT,
    CHEAT_URGE,
    PAYOFF_BOTH_COOPERATE,
    PAYOFF_CHEAT_WIN,
    PAYOFF_GOT_CHEATED,
    PAYOFF_BOTH_CHEAT,
    TRUST_GAIN,
    BETRAYAL_BASE,
    BETRAYAL_NEURO,
    rng,
    NUM_OF_DAYS,
    LIST_OF_TRAITS,
    LIST_OF_NAMES,
    PAYOFF_TABLE
)




def main():
# creates maya and leo because we are testing with them, calls interaction function

    # create maya and leo with predetermined personality values, trust, and they HAVE met before
    maya_traits = {'agreeableness': 0.6, 'neuroticism': 0.7, 'honesty': 0.8, 'extraversion': 0.8}
    leo_traits = {'agreeableness': 0.7, 'neuroticism': 0.3, 'honesty': 0.9, 'extraversion': 0.5}
    maya = Agent(0, 'Maya', maya_traits)
    leo = Agent(1, 'Leo', leo_traits)
    maya.add_to_met(leo.agent_id)
    leo.add_to_met(maya.agent_id)
    maya.set_trust(leo.agent_id, 0.70)
    leo.set_trust(maya.agent_id, 0.60)

    interaction(maya, leo)

# this is where milestone 3 starts in main function!!
    print()

    
    town = Town()
    town.setup()

    for i in town.population:
        print(town.population[i])

    print()
    print(maya.calculate_interactions())
    print(leo.calculate_interactions())
    print()


    town.step_day()












def interaction(agent1, agent2):

# decision each agent made, is signified by constants for CHEAT, COOPERATE
    agent1_decision = agent1.make_decision(agent2.agent_id)
    agent2_decision = agent2.make_decision(agent1.agent_id)


# pay off 
    agent1_payoff = PAYOFF_TABLE[agent1_decision][agent2_decision]
    agent2_payoff = PAYOFF_TABLE[agent2_decision][agent1_decision]

# changed resources based off agent payoff
    agent1.change_resources(agent1_payoff)
    agent2.change_resources(agent2_payoff)


# get initial trust of each other, and after trust of each other
    initial_agent1_trust_of_agent2 = agent1.get_trust(agent2.agent_id)
    initial_agent2_trust_of_agent1 = agent2.get_trust(agent1.agent_id)
    agent1.trust_update(agent2.agent_id, agent2_decision)
    agent2.trust_update(agent1.agent_id, agent1_decision)
    after_agent1_trust_of_agent2 = agent1.get_trust(agent2.agent_id)
    after_agent2_trust_of_agent1 = agent2.get_trust(agent1.agent_id)



    print('\nSimulated interaction between Maya and Leo')
    print(f"Seed #: {SEED}\n")
    agent1.display_stats(agent1_decision, initial_agent1_trust_of_agent2, after_agent1_trust_of_agent2)
    agent2.display_stats(agent2_decision, initial_agent2_trust_of_agent1, after_agent2_trust_of_agent1)
    print()







if __name__ == '__main__':
    main()
