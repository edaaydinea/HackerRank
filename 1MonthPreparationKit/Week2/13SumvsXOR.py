#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

# Given an integer n, find the number of non-negative integers x such that n + x = n ^ x.
# Example
# n = 4
# There are four values that satisfy the condition:
# 4 + 0 = 4 ^ 0 = 4
# 4 + 1 = 4 ^ 1 = 5
# 4 + 2 = 4 ^ 2 = 6
# 4 + 3 = 4 ^ 3 = 7
# Thus, the answer is 4.



def sumXor(n):
    # Write your code here
    
    # Count the number of zeros in the binary representation of n
    zeros = 0
    while n:
        if n % 2 == 0:
            zeros += 1
        n //= 2
    
    # Return 2 to the power of the number of zeros
    return 2 ** zeros

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
