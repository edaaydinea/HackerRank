#!/bin/python3

import os


#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def getMoves(matrix, i, j):
    l, v = [], (".", "*")
    if i > 0 and matrix[i - 1][j] in v:
        l.append((i - 1, j))
    if j > 0 and matrix[i][j - 1] in v:
        l.append((i, j - 1))
    if i < m - 1 and matrix[i + 1][j] in v:
        l.append((i + 1, j))
    if j < n - 1 and matrix[i][j + 1] in v:
        l.append((i, j + 1))

    return l


def search(matrix, m, n, i, j, c=0):
    if matrix[i][j] == "*":
        return c
    matrix[i][j] = 0
    moves = getMoves(matrix, i, j)
    if len(moves) > 1:
        c += 1
    for move in moves:
        result = search(matrix, m, n, move[0], move[1], c)
        if result is not None:
            return result
    return None


def countLuck(matrix, m, n, k):
    # Write your code here
    for i in range(m):  # rows
        for j in range(n):  # columns
            if matrix[i][j] == "M":
                return "Impressed" if search(matrix, m, n, i, j) == k else "Oops!"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for _ in range(int(input())):
        m, n = map(int, input().split())

        matrix = [list(input()) for _ in range(m)]

        k = int(input())

        result = countLuck(matrix, m, n, k)

        fptr.write(result + '\n')

    fptr.close()
