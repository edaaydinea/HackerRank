#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(array):
    # Write your code here
    array.sort()
    diff = abs(array[0] - array[1])
    for i in range(1, len(array)-1):
        if abs(array[i] - array[i + 1]) < diff:
            diff = abs(array[i] - array[i + 1])
    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
