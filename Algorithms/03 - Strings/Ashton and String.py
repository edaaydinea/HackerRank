#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'ashtonString' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def ashtonString(s, k):
    # Write your code here
    kv = k - 1
    N = len(s)
    sr = [[0 for _ in range(N)] for __ in range(17)]
    sr[0] = [ord(c) - 97 for c in s]

    L = [0] * N
    cnt = 1
    kf = lambda x: x[0] * (N + 1) + x[1]

    for i in range(1, 17):
        for j in range(N):
            L[j] = (sr[i - 1][j], sr[i - 1][j + cnt] if j + cnt < N else -1, j)

        L.sort(key=kf)
        sr[i][L[0][2]] = 0
        cr = 0

        for j in range(1, N):
            if L[j - 1][0] != L[j][0] or L[j - 1][1] != L[j][1]:
                cr += 1
            sr[i][L[j][2]] = cr
        cnt *= 2

        if cnt >= N:
            break

    sa = [l[2] for l in L]
    rank = [0] * N
    lcp = [0] * N

    for i in range(N):
        rank[sa[i]] = i

    k = 0

    for i in range(N):
        if rank[i] == N - 1:
            k = 0
            continue

        j = sa[rank[i] + 1]

        while j + k < N and i + k < N and s[i + k] == s[j + k]:
            k += 1

        lcp[rank[i]] = k

        if k > 0:
            k -= 1

    numprev = 0
    tri = lambda x: ((x + 1) * x) >> 1

    for i in range(N):
        mylen = N - sa[i]
        tt = tri(mylen) - tri(numprev)
        if kv < tt:
            for j in range(1 + numprev, 1 + mylen):
                if kv < j:
                    return s[sa[i] + kv]
                kv -= j
        kv -= tt
        numprev = lcp[i]

    return sa,lcp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        res = ashtonString(s, k)

        fptr.write(str(res) + '\n')

    fptr.close()
