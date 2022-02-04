#!/bin/python3

import os
from collections import deque


#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    def next_steps(grid, point, queue, visited):
        rows, cols = len(grid), len(grid[0])
        cx, cy, cs = point
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx, cy
            while True:
                nx, ny = nx + dx, ny + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "X":
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, cs + 1))
                else:
                    break

    d = deque()
    visited = {startX, startY}
    d.append((startX, startY, 0))
    while d:
        cur_p = d.popleft()
        if cur_p[:2] == (goalX, goalY):
            return cur_p[2]
        else:
            next_steps(grid, cur_p, d, visited)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
