#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    weights = []
    queue = []
    for i in s:
        if queue and queue[-1] == i:
            queue.append(i)
            weights.append((ord(i) - 96) * len(queue))
        else:
            queue = [i]
            weights.append(ord(i) - 96)
    weights = set(weights)
    ans = []
    for j in queries:
        if j in weights:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
