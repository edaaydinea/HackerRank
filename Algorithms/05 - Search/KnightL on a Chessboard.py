#!/bin/python3

import os


#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def allMoves(i, j, a, b, n):
    moves = []
    deltas = [(a, b,), (a, -b), (-a, b), (-a, -b)]
    deltas.extend([(b, a), (b, -a), (-b, a), (-b, -a)])
    for delta in deltas:
        if 0 <= i + delta[0] < n and 0 <= j + delta[1] < n:
            moves.append((i + delta[0], j + delta[1]))
    return moves


def findDistance(n, a, b):
    distance = [[-1 for x in range(n)] for x in range(n)]
    distance[n - 1][n - 1] = 0
    todo = [(n - 1, n - 1)]
    while len(todo) > 0:
        (i, j) = todo.pop(0)
        new_moves = allMoves(i, j, a, b, n)
        for move in new_moves:
            if distance[move[0]][move[1]] == -1:
                distance[move[0]][move[1]] = distance[i][j] + 1
                todo.append((move[0], move[1]))
                if move[0] == 0 and move[1] == 0:
                    break
    return distance[0][0]


def knightlOnAChessboard(n):
    # Write your code here
    answer = [[0 for x in range(n - 1)] for x in range(n - 1)]
    for i in range(n - 1):
        for j in range(n - 1):
            answer[i][j] = findDistance(n, i + 1, j + 1)
    for i in range(n - 1):
        return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
