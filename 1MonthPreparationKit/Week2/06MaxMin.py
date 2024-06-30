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

# You will be given a list of integers, arr, and a single integer k. 
# You must create an array of length k from elements of arr such that its unfairness is minimized. 
# Call that array arr. Unfairness of an array is calculated as max(arr) - min(arr).

# Where:
# - max denotes the largest integer in arr
# - min denotes the smallest integer in arr

# Example
# arr = [1, 4, 7, 2]
# k = 2

# Pick any two elements, test subarrays: [1, 4] or [4, 7] or [7, 2] or [1, 7] or [1, 2] or [4, 2]
# The unfairness of the subarray [1, 4] is 4 - 1 = 3
# Testing for all pairs, the solution [1,2] provides the minimum unfairness.

def maxMin(k, arr):
    # Write your code here
    
    # Sort the array
    arr.sort()
    
    # Initialize the minimum unfairness
    min_unfairness = arr[-1]
    
    # Iterate over the array
    for i in range(len(arr) - k + 1):
        # Calculate the unfairness
        unfairness = arr[i + k - 1] - arr[i]
        # Update the minimum unfairness
        min_unfairness = min(min_unfairness, unfairness)
    
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
