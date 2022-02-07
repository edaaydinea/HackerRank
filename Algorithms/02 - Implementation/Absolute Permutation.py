#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    available_nums = set(range(1, n+1))
    smallest_permutation = []

    for pos in range(1, n+1):
        if pos-k in available_nums:
            smallest_permutation.append(pos-k)
            available_nums.remove(pos-k)
        elif pos+k in available_nums:
            smallest_permutation.append(pos+k)
            available_nums.remove(pos+k)
        else:
            return [-1]

    return smallest_permutation

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
