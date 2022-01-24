"""
Problem: https://www.hackerrank.com/challenges/compress-the-string/problem

Author: Eda AYDIN
"""
import itertools

for S, k in itertools.groupby(input()):
    print("(%d, %d)" % (len(list(k)), int(S)), end=' ')
