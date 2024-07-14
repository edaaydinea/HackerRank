#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    #Compare the number of swaps needed for arr switching to ascending or descending array
    # Initialize swap counters for ascending and descending sorts
    
    num_swaps = [0, 0]
    
    # Iterate over ascending (count=0) and descending (count=1) sorts
    for count in range(2):
        sorted_arr = sorted(arr) if count == 0 else sorted(arr, reverse=True)
        idx = {n: i for i, n in enumerate(sorted_arr)}
        
        # Iterate over the original array to compare with the sorted array
        for i, n in enumerate(arr):
            m = sorted_arr[i]
            if m != n:
                j = idx[n]
                # Simulate swap in sorted array and update indices
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
                idx[n], idx[m] = i, j
                num_swaps[count] += 1  # Increment swap count
    
    # Return the minimum number of swaps needed
    return min(num_swaps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
