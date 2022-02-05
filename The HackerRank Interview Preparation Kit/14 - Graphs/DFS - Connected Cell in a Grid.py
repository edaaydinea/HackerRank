#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#
def maxRegion(grid):
    maxRegion = 0
    rowSize = len(grid)
    colSize = len(grid[0])
    visited = [[False for _ in range(colSize)] for _ in range(rowSize)]

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if grid[r][c] == 1:
                regionSize = DFS_Region(grid, r, c, visited)
                maxRegion = max(maxRegion, regionSize)

    return maxRegion


def DFS_Region(grid, row, col, visited):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return 0

    if visited[row][col] is True:
        return 0

    visited[row][col] = True

    if grid[row][col] == 0:
        return 0

    size = 1

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r != row or c != col:
                size += DFS_Region(grid, r, c, visited)

    return size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
