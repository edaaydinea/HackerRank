#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    sorted_array = sorted(arr)
    min_unfairness = sorted_array[k - 1] - sorted_array[0]

    for i in range(1, len(sorted_array) - k + 1):
        unfairness = sorted_array[i + k - 1] - sorted_array[i]
        if min_unfairness > unfairness:
            min_unfairness = unfairness

    return min_unfairness


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
