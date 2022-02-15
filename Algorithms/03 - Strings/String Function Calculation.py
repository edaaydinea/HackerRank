#!/bin/python3

import os
from itertools import zip_longest, islice


#
# Complete the 'maxValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING t as parameter.
#

def toIntKeysBest(l):
    seen = set()
    ls = []
    for e in l:
        if e not in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def inverseArray(l):
    n = len(l)
    ans = [0] * n
    for i in range(n):
        ans[l[i]] = i
    return ans


def suffixArrayBest(s):
    n = len(s)
    k = 1
    line = toIntKeysBest(s)
    while max(line) < n - 1:
        line = toIntKeysBest([a * (n + 1) + b + 1
                              for (a, b) in
                              zip_longest(line, islice(line, k, None), fillvalue=-1)])
        k <<= 1
    return line


def suffixMatrixBest(t):
    n = len(t)
    k = 1
    line = toIntKeysBest(t)
    ans = [line]
    while max(line) < n - 1:
        line = toIntKeysBest([a * (n + 1) + b + 1
                              for (a, b) in
                              zip_longest(line, islice(line, k, None), fillvalue=-1)])
        ans.append(line)
        k <<= 1
    return ans


def lcp(sm, i, j):
    n = len(sm[-1])
    if i == j:
        return n - 1
    k = 1 << (len(sm) - 2)
    ans = 0
    for line in sm[-2::-1]:
        if i >= n or j >= n:
            break
        if line[i] == line[j]:
            ans ^= k
            i += k
            j += k
        k >>= 1
    return ans


def maxValue(t):
    # Write your code here
    res = inverseArray(suffixArrayBest(t))
    mtx = suffixMatrixBest(t)

    lcp_res = []
    for n in range(len(res) - 1):
        lcp_res.append(lcp(mtx, res[n], res[n + 1]))
    lcp_res.append(0)

    max_score = len(t)

    lcp_res_len = len(lcp_res)

    for i, num in enumerate(res):
        if lcp_res[i] <= 1:
            continue
        lcp_res_i = lcp_res[i]

        cnt = 2
        for j in range(i + 1, lcp_res_len):
            if lcp_res[j] >= lcp_res_i:
                cnt += 1
            else:
                break
        for j in range(i - 1, -1, -1):
            if lcp_res[j] >= lcp_res_i:
                cnt += 1
            else:
                break

        max_score = max(cnt * lcp_res_i, max_score)

    return max_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = maxValue(t)

    fptr.write(str(result) + '\n')

    fptr.close()
