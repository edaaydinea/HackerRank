#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending.
# Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

# Example
# grid = ["abc", "ade", "efg"]
# The grid is rearranged as follows:
# abc -> abc
# ade -> ade
# efg -> efg
# The letters in each row are in ascending order. The letters in the columns are also in ascending order. Return YES.

def gridChallenge(grid):
    # Write your code here
    
    # Iterate through the grid
    for i in range(len(grid)):
        # Sort the row
        grid[i] = sorted(grid[i])
        
    # Iterate through the columns
    for i in range(len(grid[0])):
        # Iterate through the rows
        for j in range(1, len(grid)):
            # Check if the columns are in ascending alphabetical order
            if grid[j][i] < grid[j - 1][i]:
                return "NO"
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
