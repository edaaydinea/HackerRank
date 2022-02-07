#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    # print all the moves here
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "m":
                bot_row = i
                bot_column = j
            if grid[i][j] == "p":
                princess_row = i
                princess_column = j

    i = bot_row - princess_row
    while i != 0:
        if i < 0:
            print("DOWN")
            i += 1
        if i > 0:
            print("UP")
            i -= 1

    i = bot_column - princess_column
    while i != 0:
        if i < 0:
            print("RIGHT")
            i += 1
        if i > 0:
            print("LEFT")
            i -= 1


m = int(input())  # odd integer between 3 and 100
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
