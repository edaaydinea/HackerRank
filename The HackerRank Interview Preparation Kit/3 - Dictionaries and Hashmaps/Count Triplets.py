#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    arr2 = defaultdict(int)
    arr3 = defaultdict(int)
    count = 0

    for i in arr:
        count += arr3[i]
        arr3[i * r] += arr2[i]
        arr2[i * r] += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
