"""
Problem: https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

Author: Eda AYDIN
"""


def mean(X):
    return sum(X) / len(X)


def leastSquareRegression(X, Y):
    b = sum([(X[i] - mean(X)) * (Y[i] - mean(Y))
             for i in range(len(X))]) / sum([(j - mean(X)) ** 2 for j in X])
    a = mean(Y) - (b * mean(X))
    return a + (b * 80)


X = []
Y = []
for i in range(5):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

print(round(leastSquareRegression(X, Y), 3))
