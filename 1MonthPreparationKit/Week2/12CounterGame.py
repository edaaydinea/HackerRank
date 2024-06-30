#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
# Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of 2.
# If it is, they divide it by 2. If not, they reduce it by the next lower number which is a power of 2.
# Whoever reduces the number to 1 wins the game. Louise always starts.

# Example
# n = 132
# 132 is not a power of 2. The next lower number that is a power of 2 is 128.
# 132 - 128 = 4
# 4 is a power of 2. Divide by 2 to get 2.
# 2 is a power of 2. Divide by 2 to get 1.
# Louise wins the game.

def counterGame(n):
    # Write your code here
    
    # Initialize the counter
    counter = 0
    
    # While n is greater than 1
    while n > 1:
        # If n is a power of 2
        if n & (n - 1) == 0:
            # Divide n by 2
            n = n // 2
        else:
            # Find the next lower number that is a power of 2
            temp = 1
            while temp < n:
                temp *= 2
            # Reduce n by the next lower number that is a power of 2
            n -= temp // 2
        # Increment the counter
        counter += 1
    
    # If the counter is even, return "Richard"
    if counter % 2 == 0:
        return "Richard"
    # Otherwise, return "Louise"
    else:
        return "Louise"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
