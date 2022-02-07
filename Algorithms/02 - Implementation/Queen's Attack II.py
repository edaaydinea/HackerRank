#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n :the number of rows and columns in the board
#  2. INTEGER k : the number of obstacles on the board
#  3. INTEGER r_q : the row number of the queen's position
#  4. INTEGER c_q : the column number of the queen's position
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    obs = {(x, y) for (x, y) in obstacles}

    directions = ["UP", "UPRIGHT", "RIGHT", "DOWNRIGHT", "DOWN", "DOWNLEFT", "LEFT", "UPLEFT"]
    steps = {"UP": (0,1), "UPRIGHT": (1,1), "RIGHT": (1,0), "DOWNRIGHT": (1,-1),
             "DOWN": (0,-1), "DOWNLEFT": (-1,-1), "LEFT": (-1,0), "UPLEFT": (-1, 1)
             }

    num_reachable_squares = 0

    for direction in directions:
        dx, dy = steps[direction]
        step_num = 1
        while True:
            current_x = r_q + step_num * dx
            current_y = c_q + step_num * dy

            if current_x < 1 or current_x > n or current_y < 1 or current_y > n or (current_x, current_y) in obs:
                break
            else:
                num_reachable_squares += 1
                step_num += 1

    return num_reachable_squares


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
