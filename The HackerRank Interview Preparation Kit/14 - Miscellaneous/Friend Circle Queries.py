#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxCircle function below.
def maxCircle(queries):
    elements = {}
    groups = {}
    result = []
    maxl = 0

    for a, b in queries:
        if a not in elements:
            groups[a] = set([a])
            elements[a] = a
        if b not in elements:
            groups[b] = set([b])
            elements[b] = b
        if elements[a] != elements[b]:
            a, b = elements[a], elements[b]
            if len(groups[b]) > len(groups[a]):
                a,b = b,a
            groups[a] |= groups[b]
            for p in groups[b]:
                elements[p] = a
            del groups[b]

        maxl = max(maxl, len(groups[elements[a]]))
        result.append(maxl)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
