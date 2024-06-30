#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar

# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# Example
# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]
# There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.



def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    # Sort the array
    ar.sort()
    # Iterate through the array
    i = 0
    # Check if the current element is equal to the next element
    while i < n-1:
        # If it is, increment the pairs and skip the next element
        if ar[i] == ar[i+1]:
            pairs += 1
            i += 2
        # If it is not, move to the next element
        else:
            i += 1
            
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
