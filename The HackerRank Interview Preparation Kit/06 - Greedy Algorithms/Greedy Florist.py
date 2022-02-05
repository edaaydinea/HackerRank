#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    sorted_c = sorted(c, reverse=True)
    s = 0
    counter = 0
    additional = 0

    for c in sorted_c:
        if counter == k:
            counter = 0
            additional += 1

        s += (additional + 1) * c
        counter += 1

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
