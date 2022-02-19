#!/bin/python3
import collections


#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    default_dict = collections.defaultdict(list)
    for i in range(len(arr)):
        key, value = arr[i].split()
        if i < n // 2:
            default_dict[int(key)].append("-")
        else:
            default_dict[int(key)].append(value)
    ordered_dict = collections.OrderedDict(sorted(default_dict.items()))
    print(" ".join([" ".join(l) for l in ordered_dict.values()]))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip())

    countSort(arr)
