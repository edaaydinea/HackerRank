#!/bin/python3

import os

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

N = 10


def crosswordPuzzle():
    # Write your code here

    crossword = [list(input()) for _ in range(N)]
    words = input().split(";")

    positions = set()

    for i in range(N):
        for j in range(N):
            if crossword[i][j] == "-":
                if (i == 0 or crossword[i - 1][j] != "-") and (
                        i == N - 1 or crossword[i + 1][j] == "-"):
                    positions.add((i, j, 1, 0))

                if (j == 0 or crossword[i][j - 1] != "-") and (
                        j == N - 1 or crossword[i][j + 1] == "-"):
                    positions.add((i, j, 0, 1))

    solve(crossword, words, positions)


def field2str(field):
    return '\n'.join(map(''.join, field))


def solve(crossword, words, positions):
    if not words:
        print(field2str(crossword))
        exit()

    words, word = words[:-1], words[-1]

    for position in positions:
        i, j, di, dj = position
        go_further = True
        next_crossword = [row[:] for row in crossword]

        for letter in word:
            if (i > N - 1 or j > N - 1 or
                    (next_crossword[i][j] != '-' and next_crossword[i][j] != letter)):
                go_further = False
                break

            next_crossword[i][j] = letter
            i += di
            j += dj

        if i < N and j < N and next_crossword[i][j] == '-':
            go_further = False

        if go_further:
            next_positions = positions.copy()
            next_positions.remove(position)
            solve(next_crossword, words, next_positions)


if __name__ == '__main__':
    crosswordPuzzle()
