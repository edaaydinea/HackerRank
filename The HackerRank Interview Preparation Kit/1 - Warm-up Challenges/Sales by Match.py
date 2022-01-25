"""
Problem:https://www.hackerrank.com/challenges/sock-merchant/problem

Author: Eda AYDIN
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    visited = []

    for i in range(n):
        if ar[i] not in visited:
            visited.append(ar[i])
            count = 1
            for j in range(i + 1, n):
                if ar[i] == ar[j]:
                    count += 1
            pairs += count // 2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
