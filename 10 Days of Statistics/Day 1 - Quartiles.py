#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def getMedian(array):
    array.sort()
    n = len(array)
    mid = n // 2
    if n % 2 != 0:
        return array[mid]
    else:
        return (array[mid] + array[mid - 1]) / 2


def quartiles(arr):
    # Write your code here
    q2 = getMedian(arr)
    n = len(arr)
    mid = n // 2

    if n % 2 != 0:
        q1 = getMedian(arr[0:mid])
        q3 = getMedian(arr[mid + 1:n])
    else:
        q1 = getMedian(arr[0:mid])
        q3 = getMedian(arr[mid:n])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(n, data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
