"""
Day 5: Normal Distribution I

Question: The final grades for a Physics exam taken by a large group of students have a mean of
mi = 70 and a standard deviation of sigma = 10. If we can approximate the distribution of these
grades by a normal distribution, what percentage of the students:

1. Scored higher than 80 (i.e., have a grade > 80)?
2. Passed the test (i.e., have a grade >= 60)?
3. Failed the test (i.e., have a grade < 60)?
Author: Eda AYDIN

"""
import math


def cumulative(mean, std, value):
    return (0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))) * 100


values = list(map(float, input().split()))
mean = values[0]
std = values[1]
question1 = float(input())
threshold_number = float(input())

print(round(100 - cumulative(mean, std, question1), 2))
print(round(100 - cumulative(mean, std, threshold_number), 2))
print(round(cumulative(mean, std, threshold_number), 2))
