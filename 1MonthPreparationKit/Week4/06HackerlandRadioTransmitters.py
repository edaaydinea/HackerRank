#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

# Hackerland is a one-dimensional city with houses, where each house i is located at some x_i on the x-axis. The Mayor wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a range, k, meaning it can transmit a signal to all houses <= k units of distance away.

# Given a map of Hackerland and the value of k, determine the minimum number of transmitters needed to cover every house in the city. It is guaranteed that all houses are located on the x-axis.

# For example, if Hackerland houses are located at x = [1, 2, 3, 5, 9] and the
# Mayor installs transmitters with a range of k = 1, they can provide optimal coverage to all houses

# There are two ways to cover all houses:
# 1. Put a transmitter on house 2 and 5
# 2. Put a transmitter on house 2 and 3

# The first solution is the best, so the answer is 2.


def hackerlandRadioTransmitters(x, k):
    # Write your code here
    # Sort the houses
    x = sorted(x)
    # Initialize the count of transmitters
    c = 1
    # Initialize the transmitter position
    t = x[0]
    
    # Iterate through the houses
    for i in range(len(x)):
        # If the house is within the range of the transmitter
        if x[i] == t + k:
            t = x[i]
        # If the house is outside the range of the transmitter
        elif x[i] > t + k:
            t = x[i-1]
        # If the house is the last house
        else:
            continue
        
        # Increment the count of transmitters
        for j in range(i, len(x)):
            # If the house is outside the range of the transmitter
            if x[j] > t + k:
                t = x[j]
                c += 1
                break
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
