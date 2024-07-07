#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

# Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.
# Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
# Complete the icecreamParlor function below.

# icecreamParlor has the following parameter(s):
#     int m: the amount of money they have to spend
#     int cost[n]: the cost of each flavor of ice cream

# Returns
#     int[2]: the indices of the two flavors they will purchase as two space-separated integers in increasing order

# Example
# cost = [1, 4, 5, 3, 2]
# m = 4

# The two flavors that cost 1 and 3 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.


def icecreamParlor(m, arr):
    # Write your code here
    
    # Create a dictionary to store the cost of each flavor of ice cream
    cost_dict = {}
    
    # Loop through the cost of each flavor of ice cream
    for i in range(len(arr)):
        
        # Calculate the cost of the current flavor
        cost = arr[i]
        
        # Calculate the cost of the other flavor
        other_cost = m - cost
        
        # Check if the other flavor is in the dictionary
        if other_cost in cost_dict:
            
            # Return the indices of the two flavors
            return [cost_dict[other_cost] + 1, i + 1]
        
        # Add the cost of the current flavor to the dictionary
        cost_dict[cost] = i
        
    # Return an empty list if no two flavors meet the criteria
    return []

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
