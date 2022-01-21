"""
Problem: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/

Author: Eda AYDIN
"""

import math

max_height = int(input())
number_of_boxes = int(input())
mean_weight_of_cargo_box = int(input())
std = int(input())

print(round(0.5 * (1 + math.erf((max_height - (number_of_boxes * mean_weight_of_cargo_box)) /
                                ((math.sqrt(number_of_boxes) * std) * math.sqrt(2)))), 4))
