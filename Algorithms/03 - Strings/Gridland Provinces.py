#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandProvinces' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

PRIME = 1000000007 * 65535

PMAP = [int((1 << (5 * i)) % PRIME) for i in range(1202)]


def chash(s, p=0):
    for c in s:
        p = ((p << 5) + ord(c)) % PRIME
    return p


def hmap(s):
    ret = [0]
    for c in s:
        ret.append(((ret[-1] << 5) + ord(c)) % PRIME)
    return ret


def hrange(l, i, j, s):
    return (l[j] + ((s - l[i]) * PMAP[j - i])) % PRIME


def count(s1: str, s2: str, s1rev, s2rev):
    ret = set()
    n, n2 = len(s1), 2 * len(s1)
    left_to_top = s2rev + s1
    left_to_bot = s1rev + s2

    right_from_top = s1 + s2rev
    right_from_bot = s2 + s1rev

    mid_even_tb = [ord(s1[i // 2]) if ((i % 4) in (0, 3)) else ord(s2[i // 2]) for i in range(n2)]
    mid_odd_tb = [ord(s2[i // 2]) if ((i % 4) in (0, 3)) else ord(s1[i // 2]) for i in range(n2)]

    left_to_top, left_to_bot, right_from_top, right_from_bot = map(hmap, (
        left_to_top, left_to_bot, right_from_top, right_from_bot))

    mid_even_tb = [mid_even_tb[2 * j + 1] + mid_even_tb[2 * j] * PMAP[1] for j in range(n)]
    mid_odd_tb = [mid_odd_tb[2 * j + 1] + mid_odd_tb[2 * j] * PMAP[1] for j in range(n)]

    for left, mids, rights in (left_to_top, (mid_even_tb, mid_odd_tb), (right_from_top, right_from_bot)), (
            left_to_bot, (mid_odd_tb, mid_even_tb), (right_from_bot, right_from_top)):
        for i in range(0, n + 1):
            mid = mids[i & 1]
            s = hrange(left, n - i, n + i, 0)
            for j in range(i, n):
                ret.add(hrange(rights[j & 1], j, n2 - j, s))
                s = (s * PMAP[2] + mid[j]) % PRIME
            ret.add(s)
            rights = rights[::-1]
    return ret


def gridlandProvinces(s1, s2):
    # Write your code here
    s1rev, s2rev = s1[::-1], s2[::-1]
    return len(count(s1, s2, s1rev, s2rev).union(count(s1rev, s2rev, s1, s2)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        s1 = input()

        s2 = input()

        result = gridlandProvinces(s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
