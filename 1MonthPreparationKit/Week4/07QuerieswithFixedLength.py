#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

# Queries with Fixed Length
# Consider an n-integer sequence, A = a[0], a[1], ..., a[n-1]. We perform a query on A by using an integer, d, to calculate the result of the following expression:
# max(a[i], a[i+1], ..., a[i+d-1]), 0 <= i < n-d+1
# In other words, we consider each subsequence of d consecutive elements in the sequence. For each subsequence, we find the maximum value in that subsequence.
# Complete the solve function in the editor below. It has two parameters:


from collections import deque

def min_of_max_in_subarrays_with_size(d, arr):
    # use sliding window to iterate through array
    dq = deque()
    candidtaes = []
    for i in range(len(arr)):
        # remove out-of-window index
        if dq and dq[0] <= i-d:
            dq.popleft()
        # before adding the current index, make sure to remove all indexes
        # indicating to value not larger than that of the current i
        # this way can make sure the maximum is in the front of queue
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)
        # add to max subarrays
        if i >= d-1:
            candidtaes.append(arr[dq[0]])
    return min(candidtaes)

def solve(arr, queries):
    result = []  # the min of max subarrays with size d
    for d in queries:
        result.append(min_of_max_in_subarrays_with_size(d, arr))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
