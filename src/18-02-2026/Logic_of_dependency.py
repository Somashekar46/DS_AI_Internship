# Independent Example
import random
trials = 10000
count_ind = 0
for _ in range(trials):
    if random.choice(["Heads","Tails"]) == "Heads" and random.randint(1,6) == 6:
        count_ind += 1
print("Independent Probability:", count_ind/trials)
# Dependent Example
count_dep = 0
bag = ["Red"]*5 + ["Blue"]*5
for _ in range(trials):
    temp = bag.copy()
    first = random.choice(temp)
    temp.remove(first)
    second = random.choice(temp)
    if first == "Red" and second == "Red":
        count_dep += 1
print("Dependent Probability:", count_dep/trials)
