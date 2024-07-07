#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
# 

# Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.
# Each bomb can be planted in any cell of the grid but, once planted, it will detonate after exactly 3 seconds.
# Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells.
# This means that if a bomb detonates in cell i, j, any valid cells (i +- 1, j) and (i, j +- 1) are cleared.
# Bomberman is immune to bombs, so he can move freely throughout the grid.
# Here's what he does:
# 1. Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
# 2. After one second, Bomberman does nothing.
# 3. After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
# 4. After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
# 5. Bomberman then repeats steps 3 and 4 indefinitely.

# Note: Bomberman can move any number of cells in a single move, but he can't move diagonally. He stops moving once he's adjacent to a wall and can't move into the wall.
# Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after n seconds.


def bomberMan(n, grid):
    # Write your code here
    # If n is 1, return the grid as is
    if n == 1:
        return grid
    
    # Function to detonate bombs
    def detonate(grid):
        rows = len(grid)
        cols = len(grid[0])
        result = [['O'] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'O':
                    result[i][j] = '.'
                    if i > 0:
                        result[i-1][j] = '.'
                    if i < rows - 1:
                        result[i+1][j] = '.'
                    if j > 0:
                        result[i][j-1] = '.'
                    if j < cols - 1:
                        result[i][j+1] = '.'
        return ["".join(row) for row in result]
    
    # Full bomb grid
    full_bomb_grid = ['O' * len(grid[0]) for _ in range(len(grid))]
    
    # Determine which state to return based on n
    if n % 2 == 0:
        return full_bomb_grid
    
    # State after 3 seconds
    grid_after_3 = detonate(grid)
    
    # State after 5 seconds
    grid_after_5 = detonate(grid_after_3)
    
    if n % 4 == 1:
        return grid_after_5
    else:  # n % 4 == 3
        return grid_after_3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
