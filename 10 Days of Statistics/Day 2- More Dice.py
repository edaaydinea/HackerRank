"""
Day 2: More Dice

Author: Eda AYDIN

"""
import itertools

dice_outcomes = [1, 2, 3, 4, 5, 6]
total_experiment_outcomes = list(itertools.product(dice_outcomes, repeat=2))
favorable_experiment_outcomes = list((x, y) for x, y in itertools.product(dice_outcomes, repeat=2) if x != y)
favorable_experiment_outcomes = [sum(outcome) for outcome in favorable_experiment_outcomes
                                 if sum(outcome) == 6]

print("{} / {}".format(len(favorable_experiment_outcomes), len(total_experiment_outcomes)))
