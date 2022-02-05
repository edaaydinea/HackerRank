#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    total_swaps = 0
    start = 0

    while start < len(arr):
        if arr[start] == start + 1:
            start +=1
            continue
        arr[arr[start] - 1], arr[start] = arr[start], arr[arr[start]-1]
        total_swaps +=1
    return total_swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
