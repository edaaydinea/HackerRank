#!/bin/python3

import math
import os
import random
import re
import sys

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

from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    # Initialize the queue for BFS with the starting position
    queue = deque([(startX, startY, 0)])  # (x, y, distance)
    visited = set((startX, startY))
    
    while queue:
        x, y, dist = queue.popleft()
        
        # If we reached the goal, return the distance
        if (x, y) == (goalX, goalY):
            return dist
        
        # Explore all four possible directions
        for dx, dy in directions:
            nx, ny = x, y
            
            # Move in the current direction until hitting a wall or the edge of the grid
            while 0 <= nx + dx < n and 0 <= ny + dy < n and grid[nx + dx][ny + dy] == '.':
                nx += dx
                ny += dy
                
                # If the new position hasn't been visited, add it to the queue
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
    
    # If the goal is not reachable, return an appropriate value (e.g., -1 or raise an error)
    return -1

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
