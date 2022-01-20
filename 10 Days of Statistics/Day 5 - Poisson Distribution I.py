"""
Day 5: Poisson Distribution I

A random variable,X, follows Poisson distribution with mean of 2.5.
Find the probability with which the random variable X is equal to 5.

Author: Eda AYDIN

"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n


def poisson(k, lambda1):
    e = 2.71828
    poisson_distribution = (lambda1 ** k) * (e ** -lambda1) / factorial(k)
    return poisson_distribution


lambda1 = float(input())
k = float(input())

print(round(poisson(k, lambda1), 3))
