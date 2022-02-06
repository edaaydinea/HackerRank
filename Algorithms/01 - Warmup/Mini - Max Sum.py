#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    summation = [None]*int(len(arr)-3)
    for i in range(0, len(arr)-3):
        total = 0
        for j in range (i, i+4):
            total += arr[j]
        summation[i] = total

    print(summation[0],summation[-1])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
