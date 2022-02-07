#!/bin/python3

def nextMove(posr, posc, board):
    if board[posr][posc] == "d":
        print("CLEAN")
        return

    for i in range(5):
        for j in range(5):
            if board[i][j] == "d":
                row = i
                column = j

    if posr > row:
        print("UP")
        return
    if posr < row:
        print("DOWN")
        return
    if posc > column:
        print("LEFT")
        return
    if posc < column:
        print("RIGHT")
        return

    print("")


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
