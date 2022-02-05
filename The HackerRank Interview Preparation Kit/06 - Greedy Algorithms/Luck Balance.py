#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    con = contests
    con = sorted(con, reverse=True, key=lambda con: con[con[1] == 0])

    contests_1 = [implementation[0] for i, implementation in enumerate(sorted(con)) if implementation[1] == 0]
    contests_2 = [implementation[0] for j, implementation in enumerate(sorted(con[0:k], reverse=True)) if
                  implementation[1] == 1]
    contests_3 = [implementation[0] for l, implementation in enumerate(sorted(con[k:], reverse=True)) if
                  implementation[1] == 1]

    max_luck = sum(contests_1) + sum(contests_2) - sum(contests_3)
    return max_luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
