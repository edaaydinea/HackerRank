#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    areas = {(h, w): 2 for h in range(len(A)) for w in range(len(A[0]))}
    blocks = {(h, w): A[h][w] for h in range(len(A)) for w in range(len(A[0]))}

    for (h, w), curr_blocks in blocks.items():
        visible_areas_sides = sum(max(0, curr_blocks - blocks.get(key, 0))
                                  for key in ((h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)))
        areas[(h, w)] += visible_areas_sides

    return sum(areas.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
