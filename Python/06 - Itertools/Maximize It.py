"""
Problem:https://www.hackerrank.com/challenges/maximize-it/problem

Author: Eda AYDIN
"""
import itertools

K, M = map(int, input().split())
list_of_lists = []

for i in range(0, K):
    new_list = list(map(int, input().split()))
    del new_list[0]
    list_of_lists.append(new_list)


def squared(element):
    return element ** 2


products = list(itertools.product(*list_of_lists))
results = []

for i in products:
    result1 = sum(map(squared, [j for j in i]))
    result2 = result1 % M
    results.append(result2)

print(max(results))
