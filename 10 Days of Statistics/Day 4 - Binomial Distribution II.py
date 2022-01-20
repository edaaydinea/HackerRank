"""
Day 4: Binomial Distribution II

A manufacturer of metal pistons finds that, on average 12% of the pistons they
manufacture are rejected because they are incorrectly sized. What is the probability
that a batch of 10 pistons will contain:

1. no more than 2 rejects?
2. At least 2 rejects?

b(x,n,p) = (n p).p^x . q^(n-x)
x: number of successes
n : total number of trials
p : the probability of success of 1 trial
q: the probability of failure of 1 trial ( - p)
(n p): combination x! / x! (n-x)!

Author: Eda AYDIN
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n


def binomial(x, n, p):
    combination = factorial(n) / (factorial(x) * factorial(n - x))
    binomial_distribution = combination * p ** x * (1.0 - p) ** (n - x)
    return binomial_distribution


values = list(map(float, input().split()))
p = values[0] / 100
n = int(values[1])

# 1. no more than 2 rejects?
no_more_than_2_rejects = 0
for i in range(n):
    if i < 3:
        no_more_than_2_rejects += binomial(i, n, p)

print(round(no_more_than_2_rejects, 3))

# At least 2 rejects?
at_least_2_rejects = 0
for i in range(n):
    if i > 1:
        at_least_2_rejects += binomial(i, n, p)

print(round(at_least_2_rejects, 3))
