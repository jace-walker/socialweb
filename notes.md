this is how to generate random values for each trait. incase i need for later

    random_extraversion = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
    np.clip(random_extraversion, 0, 1)
    print(random_extraversion)

    random_agreeableness = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
    np.clip(random_agreeableness, 0, 1)
    print(random_agreeableness)

    random_neuroticism = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
    np.clip(random_neuroticism, 0, 1)
    print(random_neuroticism)

    random_honesty = rng.normal(BELL_CURVE_MEAN, BELL_CURVE_SPREAD)
    np.clip(random_honesty, 0, 1)
    print(random_honesty)





FOR LATER, had to axe to make room for maya, leo simulation

  town = {}

    for n in range(NUM_OF_AGENTS):
        town[n] = Agent(n, LIST_OF_NAMES[n], create_traits_dictionary())

    for agent in town.values():
        print(agent)



because some of us dont know how git works :p
git add sim.py
git add notes.md
git commit -m "What this addition added or changed"
git push