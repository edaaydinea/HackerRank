#!/usr/bin/python

"""
pos_row: current row of the bot
pos_column: current column of the bot
board: grid
"""


# Head ends here

def next_move(pos_row, pos_column, board):
    if board[pos_row][pos_column] == "d":
        print("CLEAN")
        return

    dirty_current_row = 0
    dirty_current_column = 0

    value = 99

    for i in range(5):
        for j in range(5):
            if board[i][j] == "d":
                if (abs(pos_row - i) + abs(pos_column - j)) < value:
                    value = abs(pos_row - i) + abs(pos_column - j)
                    dirty_current_row = i
                    dirty_current_column = j

    if dirty_current_column > pos_column:
        print("RIGHT")
        return
    if dirty_current_column < pos_column:
        print("LEFT")
        return
    if dirty_current_row > pos_row:
        print("DOWN")
        return
    if dirty_current_row < pos_row:
        print("UP")
        return

    # Tail starts here


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
