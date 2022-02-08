#!/usr/bin/python3

"""
posx: current row of the bot
posy: current column of the bot
board: grid
"""
import os


def next_move(posx, posy, board):
    current_board, lastMove = load_board("test.txt")

    try:
        for i in range(5):
            for j in range(5):
                if board[i][j] != 'o':
                    current_board[i][j] = board[i][j]

    except (ValueError, IndexError):
        print(i)
        print(j)
        print(board)
        print(current_board)
        print(load_board("test.txt"))
        with open('test.txt', 'r') as content_file:
            content = content_file.read()
            print(content)

    if current_board[posx][posy] == 'd':
        print("CLEAN")
        save_board("test.txt", current_board, lastMove)

        return

    value = 99
    dirty_current_row = -1
    dirty_current_column = -1
    for i in range(5):
        for j in range(5):
            if current_board[i][j] == 'd':
                if (abs(posx - i) + abs(posy - j)) < value:
                    value = abs(posx - i) + abs(posy - j)
                    dirty_current_row = i
                    dirty_current_column = j

    if dirty_current_row != -1:
        if dirty_current_column > posy:
            print("RIGHT")
            save_board("test.txt", current_board, "RIGHT")
            return

        if dirty_current_column < posy:
            print("LEFT")
            save_board("test.txt", current_board, "LEFT")
            return

        if dirty_current_row > posx:
            print("DOWN")
            save_board("test.txt", current_board, "DOWN")
            return

        if dirty_current_row < posx:
            print("UP")
            save_board("test.txt", current_board, "UP")
            return

    gain_up = 0
    gain_down = 0
    gain_left = 0
    gain_right = 0

    for i in range(posx):
        for j in range(5):
            if current_board[i][j] == 'o':
                gain_up += 1 / float((abs(posx - i) + abs(posy - j)))

    for i in range(posx, 5):
        for j in range(5):
            if current_board[i][j] == 'o':
                gain_down += 1 / float((abs(posx - i) + abs(posy - j)))

    for i in range(5):
        for j in range(posy):
            if current_board[i][j] == 'o':
                gain_left += 1 / float((abs(posx - i) + abs(posy - j)))

    for i in range(5):
        for j in range(posy, 5):
            if current_board[i][j] == 'o':
                gain_right += 1 / float((abs(posx - i) + abs(posy - j)))

    if gain_up == max(gain_up, gain_down, gain_left, gain_right) and lastMove != "DOWN" and gain_up != 0 and posx != 0:
        print("UP")
        save_board("test.txt", current_board, "UP")
        return

    if gain_down == max(gain_down, gain_left, gain_right) and lastMove != "UP" and gain_down != 0 and posx != 4:
        print("DOWN")
        save_board("test.txt", current_board, "DOWN")

        return
    if gain_left == max(gain_left, gain_right) and lastMove != "RIGHT" and gain_left != 0 and posy != 0:
        print("LEFT")
        save_board("test.txt", current_board, "LEFT")

        return
    if lastMove != "LEFT" and gain_right != 0 and posy != 4:
        print("RIGHT")
        save_board("test.txt", current_board, "RIGHT")
        return

    if gain_up == max(gain_up, gain_down, gain_left, gain_right) and gain_up != 0 and posx != 0:
        print("UP")
        save_board("test.txt", current_board, "UP")

        return
    if gain_down == max(gain_down, gain_left, gain_right) and gain_down != 0 and posx != 4:
        print("DOWN")
        save_board("test.txt", current_board, "DOWN")

        return
    if gain_left == max(gain_left, gain_right) and gain_left != 0 and posy != 0:
        print("LEFT")
        save_board("test.txt", current_board, "LEFT")

        return
    if gain_right != 0 and posy != 4:
        print("RIGHT")
        save_board("test.txt", current_board, "RIGHT")
        return

    return


def load_board(filename):
    board_initial = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'],
                     ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]
    lastMove = "None"

    if not os.path.isfile('./test.txt'):
        return [board_initial, lastMove]

    with open(filename) as f:
        lastMove = f.readline()
        lastMove = lastMove.strip()
        board_initial = [[j for j in f.readline().strip()] for _ in range(5)]
        return [board_initial, lastMove]


def save_board(filename, mem_board, last_move):

    with open(filename, "w") as f:
        f.write(last_move + '\n')

        for i in mem_board:
            line = ""
            for j in i:
                line += j
            f.write(line + '\n')


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
