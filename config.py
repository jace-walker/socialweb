# this file will contain all of the constants needed in the program, as well as explain what each does briefly.
import numpy as np



NUM_OF_AGENTS = 10                      # number of agents in town, irrelevant this early
SEED = 20                               # important for random number gen, allows you to 'reproduce' my results
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
TRUST_GAIN = 0.1                        # gain in trust if the OTHER agent cooperates with you
BETRAYAL_BASE = 0.15                    # base value for the temptation calculation
BETRAYAL_NEURO = 0.35                   # modifer that will scale the betrayal value based off of agent's own neuroticism


rng = np.random.default_rng(SEED) 

LIST_OF_TRAITS = ['extraversion', 'agreeableness', 'neuroticism', 'honesty']               


LIST_OF_NAMES = [
    'Jon', 'Mark', 'Meagan', 'Debby', 'Damien', 
    'Josh', 'Kenzie', 'Brick', 'Ash', 'Kevin' ]                                            


PAYOFF_TABLE = [
    [PAYOFF_BOTH_CHEAT, PAYOFF_CHEAT_WIN],
    [PAYOFF_GOT_CHEATED, PAYOFF_BOTH_COOPERATE]
]        




