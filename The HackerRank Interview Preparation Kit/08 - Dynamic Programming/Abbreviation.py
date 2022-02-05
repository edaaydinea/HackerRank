#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # Write your code here
    n, m = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True
    for i in range(1, n + 1):
        dp[i][0] = a[:i].islower()

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1].isupper():
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False
            else:
                if a[i - 1].upper() == b[j - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

    if dp[n][m]:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
