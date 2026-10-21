# this file holds the agent class and all of its methods

import numpy as np
from config import (
    rng,
    LIST_OF_TRAITS,
    DEFAULT_TRUST,
    COOPERATE,
    CHEAT,
    BETRAYAL_BASE,
    BETRAYAL_NEURO,
    CHEAT_URGE,
    TRUST_GAIN,
)







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
        """Takes in resource change amount and spits out new resource count"""

        self.resources += resource_change
        return self.resources



    def trust_update(self, partner_id, partner_choice):
        """This method will update the trust of idk fill in later.."""

        if partner_choice == COOPERATE:
            agent_trust_of_partner = self.get_trust(partner_id) + TRUST_GAIN
            self.set_trust(partner_id, agent_trust_of_partner)

        else:
            agent_trust_of_partner = self.get_trust(partner_id)
            agent_neuroticism = self.traits['neuroticism']
            
            neuroticism_change = BETRAYAL_BASE + (BETRAYAL_NEURO * agent_neuroticism)

            agent_trust_of_partner -= neuroticism_change

            self.set_trust(partner_id, agent_trust_of_partner)



    def display_stats(self, move, initial, after):
        """Displays the agent's own ID, own name, inital trust of partner, after trust of partner, final resource count"""

        if move == 0:
            action = 'Cheat'
        if move == 1:
            action = 'Cooperate'


        print(f"Agent {self.agent_id}: {self.name}, {action}, {initial:.2f} -> {after:.2f}, {self.resources} ")