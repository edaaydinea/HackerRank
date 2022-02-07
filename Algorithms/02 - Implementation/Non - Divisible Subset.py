#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    c = Counter(i % k for i in s)
    count = 0
    blacklist = set()

    for x,y in c.most_common():
        if x == k / 2 or x == 0:
            count += 1
        elif k - x not in blacklist:
            count += y
            blacklist.add(x)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
