#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
# We define super digit of an integer x using the following rules:
# Given an integer, we need to find the super digit of the integer.
# If x has only 1 digit, then its super digit is x.
# Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
# For example, the super digit of 9875 will be calculated as:

# super_digit(9875) = super_digit(9+8+7+5)
#                   = super_digit(29)
#                   = super_digit(2+9)
#                   = super_digit(11)
#                   = super_digit(1+1)
#                   = super_digit(2)
#                   = 2

def superDigit(n, k):
    # Write your code here
    
    # If the length of n is 1, return n
    if len(n) == 1:
        return n
    
    # Calculate the sum of the digits of n
    sum_n = sum([int(i) for i in n])
    
    # Return the super digit of the sum of the digits of n
    return superDigit(str(sum_n * k), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
