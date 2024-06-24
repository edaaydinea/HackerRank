#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
# There are two n-element arrays of integers, A and B. You have to pick one element from each array such that the sum of the elements is at least k. Return YES if it is possible, otherwise return NO.
# q = 2, A[] : 3, B[] : 10, k = 10
# A[] : [2,1,3], B[] : [7,8,9]
# Output: YES

def twoArrays(k, A, B):
    # Write your code here
    # Sort A in ascending order
    A.sort()
    # Sort B in descending order
    B.sort(reverse=True)
    
    # Iterate through the length of A
    for i in range(len(A)):
        # If the sum of the elements at index i in A and B is less than k
        if A[i] + B[i] < k:
            # Return NO
            return 'NO'
    # If the sum of the elements at index i in A and B is greater than or equal to k
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
