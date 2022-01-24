"""
Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem

Author: Eda AYDIN
"""
import itertools

S,N = input().split()

for i in range(1, int(N) + 1):
    for j in itertools.combinations(sorted(S), i):
        print("".join(j))