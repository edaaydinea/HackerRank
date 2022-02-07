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

def bomberMan(n, grid):
    grid_dict = {(x, y): 3 if elem == 'O' else '.'
                 for y, line in enumerate(grid)
                 for x, elem in enumerate(line)}

    max_x = max(key[0] for key in grid_dict.keys())
    max_y = max(key[1] for key in grid_dict.keys())

    adj_offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def remove_adj_bombs(grid, pos):
        x, y = pos
        for (dx, dy) in adj_offsets:
            if (x + dx, y + dy) in grid:
                grid[(x + dx, y + dy)] = "."

        return grid

    def grid_to_str(grid):
        grid_str = ""
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                grid_str += grid_dict[(x, y)] if grid_dict[(x, y)] == "." else "O"
            grid_str += "\n"

        return grid_str

    def get_grid_at_step_n(grid, n):
        for step in range(2, n + 1):
            if step % 2 == 0:
                for pos, elem in grid.items():
                    if elem == ".":
                        grid[pos] = step + 3

            if step % 2 == 1:
                new_grid = grid.copy()
                for pos, elem in grid.items():
                    if elem == step:
                        new_grid[pos] = "."
                        new_grid = remove_adj_bombs(new_grid, pos)
                grid = new_grid
        return grid

    if n < 10:
        start_time = 2
    else:
        grid_dict = get_grid_at_step_n(grid_dict, 3)
        num_full_cycles_to_skip = (n - 3) // 4
        start_time = 3 + 4 * num_full_cycles_to_skip + 1  # continue the process from this step

    for step in range(start_time, n + 1):
        if step % 2 == 0:
            for pos, elem in grid_dict.items():
                if elem == ".":
                    grid_dict[pos] = step + 3

        if step % 2 == 1:
            new_grid = grid_dict.copy()
            for pos, elem in grid_dict.items():
                if elem <= step:
                    new_grid[pos] = "."
                    new_grid = remove_adj_bombs(new_grid, pos)

            grid_dict = new_grid

    ret_arr = []
    for y in range(max_y + 1):
        row_str = ""
        for x in range(max_x + 1):
            row_str += grid_dict[(x, y)] if grid_dict[(x, y)] == "." else "O"
        ret_arr.append(row_str)

    return ret_arr


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
