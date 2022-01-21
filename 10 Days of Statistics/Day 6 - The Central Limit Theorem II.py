"""
Problem: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2

Author: Eda AYDIN
"""
import math

tickets = int(input())
students = int(input())
mean = float(input())
stdev = float(input())

mu = students * mean
standard_deviation = math.sqrt(100) * stdev


# mu : mean of the distribution
# sigma^2: variance
# sigma: standard deviation

def normal_distribution(x, mu, stdev):
    return 1 / 2 * (1 + math.erf((x - mu) / (stdev * math.sqrt(2))))


print(round(normal_distribution(tickets, mu, standard_deviation), 4))
