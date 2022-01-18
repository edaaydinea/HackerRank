"""
Day 3: Drawing Marbles

A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without
replacement. If the first marble drawn is red, what is the probability that second marble is blue?

Author: Eda AYDIN
"""

import itertools
from collections import Counter

from fractions import Fraction

# X : bag, 0 : red marbles, 1 : blue marbles
X = list(Counter({0: 3, 1: 4}).elements())

total_experiment_outcomes = itertools.permutations(X, 2)

first_draw = list(i for i in total_experiment_outcomes if i[0] == 0)

second_draw = list(i for i in first_draw if i[1] == 1)

result = Fraction(len(second_draw), len(first_draw))
