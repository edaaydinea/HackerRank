#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Watson gives Sherlock an array of integers.
# His challenge is to find an element to the left is equal to the sum of all elements to the right.

# Example
# arr = [5, 6, 8, 11]
# 8 is between two subarrays that sum to 11. 
# arr = [1]
# The answer is [1] since left and right sum to 0.
# You will be given arrays of integers and must determine whether there is an element that meets the criterion.
# If there is, return YES. Otherwise, return NO.

def balancedSums(arr):
    # Write your code here
    
    # Initialize the left sum and right sum
    left_sum = 0
    right_sum = sum(arr)
    
    # Loop through the array
    for i in range(len(arr)):
        right_sum -= arr[i]
        
        # Check if the left sum is equal to the right sum
        if left_sum == right_sum:
            return "YES"
        
        left_sum += arr[i]
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
