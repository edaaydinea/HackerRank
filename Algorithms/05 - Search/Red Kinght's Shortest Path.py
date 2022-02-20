#!/bin/python3


#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    diff_i = i_end - i_start
    diff_j = j_end - j_start

    i = i_start
    j = j_start

    if diff_i % 2 == 1:
        print("Impossible")
        return
    if diff_i % 4 == 0 and diff_j % 2 == 1:
        print("Impossible")
        return
    if diff_i % 4 == 2 and diff_j % 2 == 0:
        print("Impossible")
        return

    moves = []
    while diff_i < 0 and diff_i // -2 > diff_j:
        if j == 0:
            diff_i += 2
            diff_j -= 1
            i -= 2
            j += 1
            moves.append("UR")
            continue
        diff_i += 2
        diff_j += 1
        i -= 2
        j -= 1
        moves.append("UL")

    while diff_i < 0:
        diff_i += 2
        diff_j -= 1
        i -= 2
        j += 1
        moves.append("UR")

    while diff_j > 0 and diff_j > diff_i // 2:
        moves.append("R")
        j += 2
        diff_j -= 2

    while diff_i > 0 and diff_i // -2 < diff_j:
        if j == n - 1:
            diff_i -= 2
            diff_j += 1
            i += 2
            j -= 1
            moves.append("LL")
            continue

        moves.append("LR")
        diff_i -= 2
        diff_j -= 1
        i += 2
        j += 1

    while diff_i > 0:
        diff_i -= 2
        diff_j += 1
        i += 2
        j -= 1
        moves.append("LL")

    if diff_i == 0:
        if diff_j > 0:
            move = diff_j // 2
            moves += ["R"] * move
        else:
            move = -diff_j // 2
            moves += ["L"] * move

    print(len(moves))
    print(" ".join(moves))


if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
