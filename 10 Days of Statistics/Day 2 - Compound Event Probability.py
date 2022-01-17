"""
Day 2: Compound Event Probability

Author: Eda AYDIN

"""
import itertools
from collections import Counter
from fractions import Fraction

X = list(Counter({0: 4, 1: 3}).elements())
Y = list(Counter({0: 5, 1: 4}).elements())
Z = list(Counter({0: 4, 1: 4}).elements())

total_experiment_outcomes = list(itertools.product(X, Y, Z))
favorable_experiment_outcomes = sum([sum(i) == 1 for i in total_experiment_outcomes])

print(Fraction(favorable_experiment_outcomes, len(total_experiment_outcomes)))
