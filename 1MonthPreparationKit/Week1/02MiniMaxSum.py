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
# Give five positive integers, find the minimum and maximum values that can be calculated bu summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#

def miniMaxSum(arr):
    arr.sort()
    minSum = sum(arr[:4])
    maxSum = sum(arr[-4:])
    print(minSum, maxSum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
