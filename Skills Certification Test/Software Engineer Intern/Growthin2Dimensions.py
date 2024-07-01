#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countMax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY upRight as parameter.
## Start with an infinite two dimensional grid filled with zeros, indexed from (1,1) at the bottom left corner with increasing towards the top and right.
# Given a series of coordinates (r,c) where r is the ending row and c is the ending column, add 1 to each element in the range from (1,1) to (r,c) inclusive.
# Once all coordinates are processed, determine how many cells contain the maximal value in the grid.

# Example
# upRight = ["2 3", "3 7", "4 1"]
# The maximum value is 3, and there are 2 cells that have this value.



def countMax(upRight):
    # Write your code here
    # Find the minimum row and column values
    min_row = float('inf')
    min_col = float('inf')
    
    # Find the minimum row and column values
    for coord in upRight:
        r, c = map(int, coord.split())
        min_row = min(min_row, r)
        min_col = min(min_col, c)
    
    return min_row * min_col


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    upRight_count = int(input().strip())

    upRight = []

    for _ in range(upRight_count):
        upRight_item = input()
        upRight.append(upRight_item)

    result = countMax(upRight)

    fptr.write(str(result) + '\n')

    fptr.close()
