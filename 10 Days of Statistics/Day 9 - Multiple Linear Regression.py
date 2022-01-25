"""
Problem: https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

Author: Eda AYDIN

m : the number of observed features
n : the number of feature sets Andrea studied
q : the number of feature sets Andrea want to query for

Each of n subsequent lines contain m +1 space separated decimals,
    the first m elements are features
    the last element is the value of Y for the line's feature set.

"""
from sklearn import linear_model

m, n = list(map(int, input().strip().split()))

X = [0]*n
Y = [0]*n

for i in range(n):
    input1 = list(map(float, input().strip().split()))
    X[i] = input1[:-1]
    Y[i] = input1[-1]

linear_model = linear_model.LinearRegression()
linear_model.fit(X,Y)
a = linear_model.intercept_
b = linear_model.coef_

q = int(input())

for i in range(q):
    f = list(map(float, input().strip().split()))
    Y = a + sum([b[j] * f[j] for j in range(m)])
    print(round(Y,2))