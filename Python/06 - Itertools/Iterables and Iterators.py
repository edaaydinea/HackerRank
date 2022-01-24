"""
Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem

Author: Eda AYDIN
"""
import itertools

n = int(input())
letters = list(input().split(" "))
k = int(input())

tuples = list(itertools.combinations(letters,k))
contains = list(word for word in tuples if "a" in word)
print(len(contains) / len(tuples))