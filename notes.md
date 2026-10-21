


FOR LATER, had to axe to make room for maya, leo simulation

  town = {}

    for n in range(NUM_OF_AGENTS):
        town[n] = Agent(n, LIST_OF_NAMES[n], create_traits_dictionary())

    for agent in town.values():
        print(agent)







FOR LATER USE

def create_traits_dictionary():
    
    example_dictionary = {}
    
    for trait in LIST_OF_TRAITS:
        random_value = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
        np.clip(random_value, 0, 1)
    
        example_dictionary[trait] = random_value
    
    return example_dictionary





because some of us dont know how git works :p
git add sim.py
git add notes.md
git commit -m "What this addition added or changed"
git push