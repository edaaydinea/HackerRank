#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    b = sorted(arr[:])
    n = len(arr)
    l = n + 1;
    r = 0
    for i in range(n):
        if arr[i] != b[i]:
            l = min(l, i)
            r = max(r, i)

    if l == n + 1:
        print('yes')
    elif arr[l] == b[r] and arr[r] == b[l] and arr[l + 1:r - 1] == b[l + 1:r - 1]:
        print('yes')
        print('swap', l + 1, r + 1)
    elif arr[l:r + 1] == [*reversed(b[l:r + 1])]:
        print('yes')
        print('reverse', l + 1, r + 1)
    else:
        print('no')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
