import itertools
import random
# -----------------------------------
# Part 1: Define Sample Space
# -----------------------------------
actions = ["Click", "Scroll", "Exit"]
# Generate sample space for two consecutive actions
sample_space = list(itertools.product(actions, actions))
print("Sample Space S:")
print(sample_space)
print("\nTotal outcomes in Sample Space:", len(sample_space))
# -----------------------------------
# Part 2: Event E = At least one Click
# -----------------------------------
event_E = [outcome for outcome in sample_space if "Click" in outcome]
print("\nEvent E (At least one Click):")
print(event_E)
# Calculate probability
probability_E = len(event_E) / len(sample_space)
print("\nProbability of at least one Click:")
print(probability_E)
# -----------------------------------
# Part 3: Dice Simulation (1000 trials)
# -----------------------------------
trials = 1000
count_sum_7 = 0
for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum_7 += 1
experimental_probability = count_sum_7 / trials
print("\nExperimental Probability of sum = 7:", experimental_probability)
# Theoretical probability
theoretical_probability = 1/6
print("Theoretical Probability of sum = 7:", theoretical_probability)
