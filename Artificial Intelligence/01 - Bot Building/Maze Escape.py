directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
N = input()
board = []

for i in range(3):
    board.append(input())

MAZE = [board[0][1], board[1][2], board[2][1], board[1][0]]
f = 0

for i in range(4):
    if MAZE[i] == 'e':
        print(directions[i])
        f = 1
        break

if f == 0:
    for i in range(4):
        if MAZE[i] == '-' or MAZE[i] == 'b':
            print(directions[i])
            break
