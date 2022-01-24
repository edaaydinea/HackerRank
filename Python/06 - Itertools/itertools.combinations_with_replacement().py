"""
Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

Author: Eda AYDIN
"""
import itertools

S, k = map(str, input().split())
S = sorted(S)
k = int(k)

print(*list(map("".join, itertools.combinations_with_replacement(S,k))), sep="\n")