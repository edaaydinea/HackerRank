#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    # Write your code here
    # Initialize the sum of the diagonals
    sum_diagonal1 = 0
    sum_diagonal2 = 0
    
    # Calculate the sum of the diagonals
    for i in range(len(arr)):
        sum_diagonal1 += arr[i][i]
        sum_diagonal2 += arr[i][len(arr) - i - 1]
    
    # Calculate the absolute difference between the sums of the diagonals
    return abs(sum_diagonal1 - sum_diagonal2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
