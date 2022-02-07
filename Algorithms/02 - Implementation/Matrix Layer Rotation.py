#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    def layerRotation(level, arr):
        mod = n * 2 + m * 2 - (2 * level + 1) * 4

        for i in range(mod):
            y, x = findloc(i, level)
            ni = (i+r) % mod
            ny, nx = findloc(ni, level)

            arr[ny][nx] = matrix[y][x]

    def findloc(ind, level):
        nn = n - 2 * level
        mm = m - 2 * level
        if ind < nn - 1:
            return level + ind, level
        elif ind < nn + mm - 2:
            return level + nn - 1, level + ind - (nn - 1)
        elif ind < 2 * nn + mm - 3:
            return level + nn - 1 - (ind - (nn + mm - 2)), level + mm - 1
        else:
            return level, level + mm - 1 - (ind - (2 * nn + mm - 3))

    n = len(matrix)
    m = len(matrix[0])

    lvs = min(n, m) // 2
    new = [[0] * m for _ in range(n)]
    for l in range(lvs):
        layerRotation(l, new)

    [print(' '.join(map(str, r))) for r in new]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
