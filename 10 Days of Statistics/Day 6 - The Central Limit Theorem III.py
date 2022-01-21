"""
Problem:https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3

Author: Eda AYDIN
"""

import math

sample_size = int(input())
mean = int(input())
stdev = int(input())
distribution_percentage = float(input())
z = float(input())

print(round(-1.96 * (stdev / math.sqrt(sample_size)) + mean, 2))
print(round(1.96 * (stdev / math.sqrt(sample_size)) + mean, 2))
