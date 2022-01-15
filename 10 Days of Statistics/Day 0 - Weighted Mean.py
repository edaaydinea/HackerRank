#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(n, X, W):
    # Write your code here
    sum_items = 0
    for i in range(n):
        sum_items = sum_items + (X[i] * W[i])

    print("{:.1f}".format(sum_items / sum(W)))


if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    weightedMean(n, vals, weights)
