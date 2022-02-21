#!/bin/python3

import os
import sys

sys.setrecursionlimit(2000000)


#
# Complete the 'similarPair' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY edges
#


def add(x, v):
    x += 1
    while x <= n:
        a[x] += v
        x += x & -x


def que(x):
    x += 1
    if x <= 0:
        return 0
    ret = 0
    x = min(n, x)
    while x > 0:
        ret += a[x]
        x -= x & -x
    return ret


st = []
vis = {}


def similarPair(x):
    global result
    st.append(x)
    while st:
        x = st[-1]
        if x not in vis:
            result += que(x + k) - que(x - k - 1)
            add(x, 1)
            vis[x] = 1
        if nx[x]:
            st.append(nx[x][-1])
            nx[x].pop()
        else:
            st.pop()
            add(x, -1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    a = [0 for i in range(4 * n)]
    nx = [[] for i in range(n)]
    pre = [-1 for i in range(n)]
    edges = []

    for i in range(n - 1):
        s, edges = (int(x) - 1 for x in input().split())
        nx[s].append(edges)
        pre[edges] = s

    s = 1
    while pre[s] != -1:
        s = pre[s]

    result = 0
    similarPair(s)

    fptr.write(str(result) + '\n')

    fptr.close()
