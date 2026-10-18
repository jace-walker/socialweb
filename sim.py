# JACE WALKER'S LIFEWORK!!

import numpy as np
#import chatgpt, claude, gemini



# these constants are all in my blueprint that is not on the repo because i am a pos i guess..

NUM_OF_AGENTS = 10                      # number of agents in town, irrelevant this early
SEED = 21                               # important for random number gen, allows you to 'reproduce' my results
BELL_CURVE_MEAN = 0.5                   # look dude, statistics is all just jargon to me bro
BELL_CURVE_SPREAD = 0.15                # see above...
DEFAULT_TRUST = 0.5                     # the default value of trust that will be used if agents never met or heard gossip
COOPERATE = 1                           # named constant for the action of 'cooperating'
CHEAT = 0                               # named constant for the action of 'cheating'              you cheater
CHEAT_URGE = 0.6                        # used in temptation calculation
PAYOFF_BOTH_COOPERATE = 3               # payoff if both agents cooperate with each other
PAYOFF_CHEAT_WIN = 5                    # payoff if agent1 cheats while the other agent2 tried to cooperate
PAYOFF_GOT_CHEATED = 0                  # payoff if agent1 gets cheated while trying to cooperate
PAYOFF_BOTH_CHEAT = 1                   # payoff if both agents cheat against each other

rng = np.random.default_rng(SEED) 

LIST_OF_TRAITS = ['extraversion', 'agreeableness', 'neuroticism', 'honesty']               


LIST_OF_NAMES = [
    'Jon', 'Mark', 'Meagan', 'Debby', 'Damien', 
    'Josh', 'Kenzie', 'Brick', 'Ash', 'Kevin' ]                                            


PAYOFF_TABLE = [
    [PAYOFF_BOTH_CHEAT, PAYOFF_CHEAT_WIN],
    [PAYOFF_GOT_CHEATED, PAYOFF_BOTH_COOPERATE]
]        





class Agent:
# this class creates an Agent and all the needed methods as they come up

    def __init__(self, agent_id, name, traits):
        self.agent_id = agent_id        # unique agent id starting from 0 to number of agents
        self.name = name                # agent's name, useless for statistics, just to make more human
        self.traits = traits            # list of four traits that are being tested
        self.trust = {}                 # dictionary that will contain trust rating for every OTHER agent
        self.met = set()                # create empty set for which who Agent has interacted with DIRECTLY
        self.resources = 0              # if money is a measure of success for you, then this is the agent's success. starting with 0 money
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



    def make_decision(self, partner_id):
        """This is a biggie. Takes in self and partner's ID in order to run the formula to calculate willingness, then 
           if the agent rolled to COOPERATE, run the formula for temptation chance and note the agent's final decision"""
        
        agent_trust_of_partner = self.get_trust(partner_id)
        agent_agreeableness = self.traits['agreeableness']
        agent_honesty = self.traits['honesty']

        willingness = (0.5 * agent_agreeableness) + (0.5 * agent_trust_of_partner)       # this formula will be somewhere in the docs idk yet
        willingness_dice_roll = rng.uniform(0, 1)


# basically, if the agent has decided to cooperate, they undergo another check, the 'temptation' check on if they will switch to CHEAT.
#   if after the first willingness roll, the agent decides to CHEAT, that is their final choice, and NO temptation check will happen
        if willingness > willingness_dice_roll:
            temptation = CHEAT_URGE * (1 - agent_honesty)
            temptation_dice_roll = rng.uniform(0, 1)

            if temptation > temptation_dice_roll:
                chosen_action = CHEAT

            else:
                chosen_action = COOPERATE


        else:
            chosen_action = CHEAT


        
        return chosen_action



    def change_resources(self, resource_change):
        self.resources += resource_change
        return self.resources

        







def main():

# main function you get the gist man

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









def interaction(agent1, agent2):

    agent1_decision = agent1.make_decision(agent2.agent_id)
    agent2_decision = agent2.make_decision(agent1.agent_id)
    print(agent1_decision)
    print(agent2_decision)


    agent1_payoff = PAYOFF_TABLE[agent1_decision][agent2_decision]
    agent2_payoff = PAYOFF_TABLE[agent2_decision][agent1_decision]
    print(agent1_payoff)
    print(agent2_payoff)


    agent1.change_resources(agent1_payoff)
    agent2.change_resources(agent2_payoff)
    print(agent1.resources)
    print(agent2.resources)





















    







if __name__ == '__main__':
    main()
