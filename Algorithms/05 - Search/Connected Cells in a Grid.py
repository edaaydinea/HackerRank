#!/bin/python3

import os

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

cellCtr = 0


def dfs(i, j):
    global cellCtr
    if i < 0 or i >= n or j < 0 or j < 0 or j >= m or matrix[i][j] == 0:
        return

    matrix[i][j] = 0
    cellCtr += 1

    dfs(i - 1, j - 1)
    dfs(i - 1, j)
    dfs(i - 1, j + 1)
    dfs(i, j - 1)
    dfs(i, j + 1)
    dfs(i + 1, j - 1)
    dfs(i + 1, j)
    dfs(i + 1, j + 1)


def connectedCell(n, m, matrix):
    # Write your code here
    global cellCtr
    maxCtr = 0
    for i in range(0, n):
        for j in range(0, m):
            dfs(i, j)
            if cellCtr > maxCtr:
                maxCtr = cellCtr
            cellCtr = 0

    return maxCtr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(n, m, matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
