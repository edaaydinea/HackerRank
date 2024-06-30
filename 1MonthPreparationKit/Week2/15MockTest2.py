#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example
# a = [2, 6]
# b = [24, 36]
# There are two numbers between the arrays: 6 and 12.
# 6 % 2 = 0, 6 % 6 = 0, 24 % 6 = 0 and 36 % 6 = 0 for the first value.
# 12 % 2 = 0, 12 % 6 = 0, 24 % 12 = 0 and 36 % 12 = 0 for the second value.
# Return 2.

def getTotalX(a, b):
    # Write your code here
    
    # Initialize the count of numbers between the two arrays
    count = 0
    
    # Iterate through the range from the maximum element in the first array to the minimum element in the second array
    for i in range(max(a), min(b) + 1):
        # Check if all elements in the first array are factors of i
        if all(i % x == 0 for x in a):
            # Check if i is a factor of all elements in the second array
            if all(x % i == 0 for x in b):
                # Increment the count
                count += 1
                
    # Return the count
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
