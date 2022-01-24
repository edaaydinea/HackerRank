"""
Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem

Author: Eda AYDIN
"""
import itertools


S = list(map(str, input().split()))
string1 = sorted(S[0])
number = int(S[1])

print(*list(map("".join, itertools.permutations(string1,number))), sep="\n")