#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
# You will be given a list of 32-bit unsigned integers. Flip all the bits in the list and return the result as an unsigned integer.
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

# n = 9_10
# 9_10 = 1001_2
# 00000000000000000000000000001001_2 = 9_10
# 11111111111111111111111111110110_2 = 4294967286_10

def flippingBits(n):
    # Write your code here
    # Convert decimal to binary
    binary = bin(n)[2:]
    print(binary)
    # Get the length of the binary number
    length = len(binary)
    print(length)
    # Get the difference between the length of the binary number and 32
    difference = 32 - length
    print(difference)
    # Add the difference to the binary number
    binary = '0' * difference + binary
    print(binary)
    # Flip the bits
    flipped = ''.join(['1' if bit == '0' else '0' for bit in binary])
    print(flipped)
    # Convert the flipped bits to decimal
    return int(flipped, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
