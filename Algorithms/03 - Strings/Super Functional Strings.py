#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superFunctionalStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def __substr(string):
    j = 1
    a = set()
    while True:
        for i in range(len(string) - j + 1):
            a.add(string[i: i + j])
        if j == len(string): break
        j += 1
    return a


def __distinct(p):
    ch = set(p)
    return len(ch)


def _f(p, M):
    return len(p) ** __distinct(p) % M


def __ans(foo):
    ret = __substr(foo)
    val = 0
    M = 10 ** 9 + 7
    for data in ret:
        val = (val + _f(data, M)) % M
    return val


def superFunctionalStrings(s):
    # Write your code here
    return __ans(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = superFunctionalStrings(s)

        fptr.write(str(result) + '\n')

    fptr.close()
