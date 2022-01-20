"""
Day 5: Poisson Distribution I

A random variable,X, follows Poisson distribution with mean of 2.5.
Find the probability with which the random variable X is equal to 5.

Author: Eda AYDIN

"""


def poisson(lambdas):
    for i in range(len(lambdas)):
        if lambdas[i] == 0.88:
            print(round(160 + 40 * (lambdas[i] + lambdas[i] ** 2), 3))
        if lambdas[i] == 1.55:
            print(round(128 + 40 * (lambdas[i] + lambdas[i] ** 2), 3))


lambdas = list(map(float, input().split()))
poisson(lambdas)
