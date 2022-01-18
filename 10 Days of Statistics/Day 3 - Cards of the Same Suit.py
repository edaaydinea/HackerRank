"""
Day 3 - Cards of the Same Suit

Author: Eda AYDIN
"""
import itertools

# You draw 2 cars from a standard 52-card deck without replacing them.
from fractions import Fraction

total_experiment_outcomes = 52
suit_number = 4

for_each_suite_number = total_experiment_outcomes / suit_number

first_card = Fraction(int(for_each_suite_number), total_experiment_outcomes)
second_card = Fraction(int(for_each_suite_number) - 1, total_experiment_outcomes - 1)

result = first_card * second_card * suit_number

