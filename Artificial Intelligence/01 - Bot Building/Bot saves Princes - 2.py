def nextMove(n, row, column, grid):
    princess_row = 0
    princess_column = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "p":
                princess_row = i
                princess_column = j

    if row < princess_row:
        return "DOWN"
    if row > princess_row:
        return "UP"
    if column < princess_column:
        return "RIGHT"
    if column > princess_column:
        return "LEFT"
    return ""


n = int(input())  # length of grid
r, c = [int(i) for i in input().strip().split()]  # bot location
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
