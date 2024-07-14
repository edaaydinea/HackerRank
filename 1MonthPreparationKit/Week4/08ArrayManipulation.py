#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Initialize an array to store the differences
    diff = [0] * (n + 1)
    
    # Process each query and update the difference array
    for query in queries:
        a, b, k = query
        diff[a - 1] += k
        if b <= n:
            diff[b] -= k
    
    # Compute the prefix sum and find the maximum value during this computation
    max_value = 0
    current_value = 0
    
    for i in range(n):
        current_value += diff[i]
        if current_value > max_value:
            max_value = current_value
    
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
