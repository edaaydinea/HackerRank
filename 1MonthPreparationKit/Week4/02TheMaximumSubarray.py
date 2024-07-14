#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# We define subsqeuence as any subset of an array. We define a subarray as a contiguous subsequence in an array.

# Given an array, find the maximum possible sum among:
# - All nonempty subarrays.
# - All nonempty subsequences.

# Print two space-separated integers denoting the maximum sums of nonempty subarrays and nonempty subsequences.

# Note that empty subarrays/subsequences should not be considered.

# Example:
# arr = [-1, 2, 3, -4, 5, 10]
# The maximum subarray sum is 16: [2, 3, -4, 5, 10]
# The maximum subsequence sum is 20: [2, 3, 5, 10]
# Return [16, 20]

def maxSubarray(arr):
    # Write your code here
    
    # Finding the maximum subarray sum using Kadane's algorithm
    max_ending_here = arr[0]
    max_so_far = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
        
    # Finding the maximum subsequence sum
    max_subsequence_sum = 0
    max_element = arr[0]
    all_negative = True
    
    for num in arr:
        if num > 0:
            max_subsequence_sum += num
            all_negative = False
        if num > max_element:
            max_element = num
            
    if all_negative:
        max_subsequence_sum = max_element
        
    return [max_so_far, max_subsequence_sum]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
