#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    r = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for k in alphabet:
        for l in alphabet:
            if k >= l:
                continue
            f = list(filter(lambda x: x == k or x == l, s))
            if valid(f):
                r = max(r, len(f))

    return r


def valid(f):
    if len(f) <= 1:
        return False
    if f[0] == f[1]:
        return False
    if len(set(f)) > 2:
        return False
    for i in range(2, len(f)):
        if i % 2 == 0:
            if f[i] != f[0]:
                return False
        else:
            if f[i] != f[1]:
                return False

    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input().strip()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
