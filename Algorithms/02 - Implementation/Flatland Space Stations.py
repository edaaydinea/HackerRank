#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    result = 0

    chain_len = c[0] - 0
    result = max(result, chain_len)

    for i in range(len(c) - 1):
        chain_len = c[i + 1] - c[i] - 1
        if chain_len % 2 == 0:
            mid = chain_len // 2
        else:
            mid = (chain_len + 1) // 2
        result = max(result, mid)

    chain_len = (n - 1) - c[-1]
    return max(result, chain_len)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
