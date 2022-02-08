"""
posx: row of coordinates of MegaMaid's initial location
posy: column of coordinates of MegaMaid's initial location
dimx: respective height of the matrix
dimy: respective width of the matrix
board: grid

@author: Eda AYDIN
"""


def next_move(posx, posy, dimx, dimy, board):
    if board[posx][posy] == "d":
        print("CLEAN")
        return

    value = 99
    dirty_current_row = - 1
    dirty_current_column = -1

    for i in range(dimx):
        for j in range(dimy):
            if board[i][j] == "d":
                if (abs(posx - i) + abs(posy - j)) < value:
                    value = abs(posx - i) + abs(posy - j)
                    dirty_current_row = i
                    dirty_current_column = j

    if dirty_current_column > posy:
        print("RIGHT")
        return
    if dirty_current_column < posy:
        print("LEFT")
        return
    if dirty_current_row > posx:
        print("DOWN")
        return
    if dirty_current_row < posx:
        print("UP")
        return
    return


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)