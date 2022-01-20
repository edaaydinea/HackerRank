"""
Day 5: Normal Distribution I

In certain plant, the time taken to assemble a car is a random variable, X having a normal distribution
with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be
assembled at this plant in:

1. Less han 19.5 hours?
2. Between 20 and 22 hours?

Author: Eda AYDIN

"""
import math


# less than 19.5 hours
def cumulative1(mean, std, less):
    print(round(0.5 * (1 + math.erf((less - mean) / (std * (2 ** 0.5)))), 3))


# Between 20 and 22 hours
def cumulative2(mean, std, lower_range, upper_range):
    print(round(0.5 * (1 + math.erf((upper_range - mean) / (std * (2 ** 0.5)))) -
                0.5 * (1 + math.erf((lower_range - mean) / (std * (2 ** 0.5)))), 3))


values = list(map(float, input().split()))
mean = values[0]
std = values[1]

less = float(input())

boundaries = list(map(float, input().split()))
lower_range = boundaries[0]
upper_range = boundaries[1]

cumulative1(mean, std, less)
cumulative2(mean, std, lower_range, upper_range)