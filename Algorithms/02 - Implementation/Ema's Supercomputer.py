#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy


#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid: list) -> int:
    # Write your code here
    for i in range(len(grid)):
        grid[i] = list(grid[i])
        grid[i].append('o')
        grid[i].insert(0, 'o')
    grid.append(['o' for i in range(len(grid[0]))])
    grid.insert(0, ['o' for i in range(len(grid[0]))])
    res = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == 'G':
                currCord = [(i, j)]
                area = 1
                start = 1
                res.append([area, currCord.copy()])
                while (grid[i - start][j] == 'G') & (grid[i + start][j] == 'G') & (grid[i][j - start] == 'G') & (grid[i][j + start] == 'G'):
                    currCord.append((i-start, j))
                    currCord.append((i+start, j))
                    currCord.append((i, j-start))
                    currCord.append((i, j+start))
                    area += 4
                    start += 1
                    res.append([area, currCord.copy()])
    answer = 0
    for i in range(len(res)-1):
        for j in range(i+1, len(res)):
            if (len(set(res[i][1]).intersection(set(res[j][1]))) == 0) & (res[i][0]*res[j][0] > answer):
                answer = res[i][0]*res[j][0]
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
