#!/bin/python3

import os
from collections import Counter
from math import inf


#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#


def balancedForest(c, edges):
    # Write your code here
    n = len(c)
    adj = [[] for i in range(n)]
    for v0, v1 in edges:
        adj[v0 - 1].append(v1 - 1)
        adj[v1 - 1].append(v0 - 1)

    def sumTree(i, p):
        s = 0
        for j in adj[i]:
            if j != p:
                s += sumTree(j, i)

        s += c[i]
        sumCounts[s] += 1
        totals[i] = s
        return s

    def minExtra(i, p, path):
        s = totals[i]
        path.add(s)
        m = min((minExtra(j, i, path) for j in adj[i] if j != p), default=inf)

        if 3 * s < t:
            if (t + s) % 2 == 0:
                s0 = (t + s) // 2
                if s0 in path:
                    m = min(m, s0 - 2 * s)
                s1 = (t - s) // 2
                sumCount = sumCounts[s1]
                if sumCount > 0 and (s1 not in path or sumCount > 1):
                    m = min(m, s1 - s)
        else:
            s0 = 2 * s
            if s0 in path:
                m = min(m, s + s0 - t)
            s0 = t - s
            if s0 in path:
                m = min(m, 2 * s - s0)
            if sumCounts[s] > 1:
                m = min(m, 3 * s - t)

        path.remove(s)
        return m

    sumCounts = Counter()
    totals = {}
    t = sumTree(0, None)
    m = minExtra(0, None, set())
    return m if m < inf else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
