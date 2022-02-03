#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp = [0] * len(arr)
    dp[0], dp[1] = arr[0], max(arr[0],arr[1])

    for i in range(2,n):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i], arr[i])

    return dp[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
