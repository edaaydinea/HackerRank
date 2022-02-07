#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    new_grid = []
    n = len(grid)
    result = [list(row[:]) for row in grid]

    for i in range(1, (n - 2) + 1):
        for j in range(1, (n - 2) + 1):
            if grid[i][j] > max(grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i][j + 1]):
                result[i][j] = 'X'
    for i in range(n):
        new_grid.append("".join(result[i]))

    return new_grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
