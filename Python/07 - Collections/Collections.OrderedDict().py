"""
Author: Eda AYDIN

N: items
"""
from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()

for i in range(N):
    dictionary_input = input()

    if type(int) != int:
        split = dictionary_input.split()

        item = split[:-1]
        item = " ".join(item)

        cost = split[-1]
        cost = "".join(cost)
        cost = int(cost)

        if item in ordered_dictionary:
            current = ordered_dictionary[item]
            current += cost
            ordered_dictionary[item] = current
        else:
            ordered_dictionary[item] = cost

for key, value in ordered_dictionary.items():
    print(key, value)
