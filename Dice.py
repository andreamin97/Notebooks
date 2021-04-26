# %%
from fractions import Fraction
import itertools
import random
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
# %%
def count_combinations(list):
    counted = Counter()

    for sub in list:
        counted += Counter(map(sum, sub))

    return {key: value for key, value in sorted(counted.items())}


def add_modifier(dict, mod=0):
    return {k+mod: dict[k] for k in dict }


def combinations(dice, n):
    items = [*range(1, dice+1)]
    return list(itertools.product(items, repeat=n))

# I need to modify this function to create each tuple with all the dice rolls
# not different lists for each dice type
def combi_dict(dict):
    rolls = []
    
    for key in dict:
        rolls.append(list(itertools.product([*range(1, key+1)], repeat=dict[key])))
    
    return rolls

# %%
rolls = combi_dict({4: 2, 6:2})
results = count_combinations(rolls)

print (rolls)
# %%
x = counted_result.keys()

total_rolls = 0
for value in counted_result.values():
    total_rolls += value

percent_rolls = [ n/total_rolls*100 for n in counted_result.values()]

plt.bar(x, percent_rolls)
plt.show()