#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#
from bisect import bisect,insort


def maximumSum(a, m):
    # Write your code here
    n = len(a)
    cumulative_sums = []
    sum_so_far = 0
    max_sum = 0

    for i in range(n):
        sum_so_far = (sum_so_far + a[i]) % m
        pos = bisect(cumulative_sums, sum_so_far)
        d = 0 if pos == i else cumulative_sums[pos]
        max_sum = max(max_sum, (sum_so_far + m - d) % m)
        insort(cumulative_sums, sum_so_far)

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
