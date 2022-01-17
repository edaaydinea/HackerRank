"""
Day 2: Basic Probability

Author: Eda AYDIN

P_event = #evet_outcomes / #total_outcomes

"""
import itertools

dice_outcomes = [1, 2, 3, 4, 5, 6]
total_experiment_outcomes = list(itertools.product(dice_outcomes, repeat=2))
favorable_experiment_outcomes = [sum(outcome) for outcome in total_experiment_outcomes
                                 if sum(outcome) <= 9]

print("{} / {}".format(len(favorable_experiment_outcomes), len(total_experiment_outcomes)))
