# JACE WALKER'S LIFEWORK!!

import numpy as np




# these constants are all in my blueprint that is not on the repo because i am a pos i guess..

NUM_OF_AGENTS = 10    
SEED = 21
LIST_OF_TRAITS = ['extraversion', 'agreeableness', 'neuroticism', 'honesty']
BELL_CURVE_MEAN = 0.5
BELL_CURVE_SPREAD = 0.15
DEFAULT_TRUST = 0.5

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
        self.resources = 0              # if money is a measure of success for you, then this is the agent's success. starting with 10 money.
        self.was_cheated = 0            # counter for how many times Agent was cheated by someone else
        self.did_cheating = 0           # counter for how many times Agent did the cheating against someone else

    def __repr__(self):
        """For display purposes"""
        return f"Agent({self.agent_id}, {self.name})"


    def __str__(self):
        """Displays Agent ID, Name, and Each trait with value assigned"""
        pieces = []

        for trait in LIST_OF_TRAITS:
            score = self.traits[trait]
            pieces.append(f"{trait[0].upper()} {score:.2f}")
        traits_text = " ".join(pieces)
        return f"{self.agent_id}, {self.name:<8} {traits_text}"


    def add_to_met(self, partner_id):
        """This method adds the partner's id to the agent's met set"""
        self.met.add(partner_id)


    def get_trust(self, partner_id):
        """This method uses the partner's ID to search for the agent's trust of said partner in their trust dictionary
           If there is no trust because the agent's have never met or heard gossip, the default value is set to a constant above"""
        if partner_id in self.trust:
            return self.trust[partner_id]

        return DEFAULT_TRUST

        
    def set_trust(self, partner_id, new_trust_rating):
        """This method will set/override the agent's trust rating attached to the partner ID to the new trust rating
           The entire program relies on the trust rating being between 0-1, so make a safety net or whatever"""
        new_trust_rating = np.clip(new_trust_rating, 0, 1)
        self.trust[partner_id] = new_trust_rating
        


def main():

# create maya and leo with predetermined personality values, trust, and they HAVE met before

    maya_traits = {'agreeableness': 0.6, 'neuroticism': 0.7, 'honesty': 0.8, 'extraversion': 0.8}
    leo_traits = {'agreeableness': 0.7, 'neuroticism': 0.3, 'honesty': 0.9, 'extraversion': 0.5}

    maya = Agent(0, 'Maya', maya_traits)
    leo = Agent(1, 'Leo', leo_traits)

    maya.add_to_met(leo.agent_id)
    leo.add_to_met(maya.agent_id)

    maya.set_trust(leo.agent_id, 0.70)
    leo.set_trust(maya.agent_id, 0.60)



    print(maya.get_trust(leo.agent_id))
    print(leo.get_trust(maya.agent_id))


    print(maya.__str__())
    print(leo.__str__())
    print(maya.__repr__())
    print(leo.__repr__())



        






def create_traits_dictionary():
    
    example_dictionary = {}
    
    for trait in LIST_OF_TRAITS:
        random_value = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
        np.clip(random_value, 0, 1)
    
        example_dictionary[trait] = random_value
    
    return example_dictionary
    







if __name__ == '__main__':
    main()
