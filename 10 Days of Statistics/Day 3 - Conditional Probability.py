"""
Day 3: Conditional Probability

Author: Eda AYDIN
"""
import itertools
from fractions import Fraction

"""
b : boy
g : girl

Bayes' Theorem:

P(A|B) = P(B|A) * P(A) / P(B)
P(B) = P(B | A) * P(B) + P(B | A') * P(B')
"""

total_experiment_outcomes = list(itertools.product(("b", "g"), ("b", "g")))

# At least 1 boy [A]
event_1_boy = list(i for i in total_experiment_outcomes if i[0] == "b" or i[1] == "g")

# 2 boy [B]
event_2_boy = list(i for i in total_experiment_outcomes if i[0] == "b" and i[1] == "b")

pb_2_boy = list(i for i in event_2_boy)

# p(B | A)
prob_pb_2_boy = Fraction(len(pb_2_boy), len(event_2_boy))

# P(A)
prob_1_boy = Fraction(len(event_2_boy), len(total_experiment_outcomes))

# P(B)
prob_2_boy = Fraction(len(event_1_boy), len(total_experiment_outcomes))

# P(A|B) = P(B|A) * P(A) / P(B)
print(prob_pb_2_boy * prob_1_boy / prob_2_boy)

