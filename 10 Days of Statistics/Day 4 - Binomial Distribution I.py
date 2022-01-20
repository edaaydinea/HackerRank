"""
Day 4: Binomial Distribution I

The ratio of boys to girls for babies born in Russia is 1.09:1.
If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places.

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
    binomial_distribution = combination * p**x * (1.0 - p)**(n - x)
    return binomial_distribution


values = list(map(float, input().split()))
p = values[0] / (values[0] + values[1])
n = 6
result = 0

for i in range(3,7):
    a = binomial(i, n, p)
    result += a

print(round(result, 3))
