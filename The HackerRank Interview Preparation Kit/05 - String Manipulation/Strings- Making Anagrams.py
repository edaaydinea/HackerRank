#!/bin/python3

import os

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
from collections import Counter


def makeAnagram(a, b):
    # Write your code here
    count_a = Counter(a)
    count_b = Counter(b)

    difference_a = count_a - count_b
    difference_b = count_b - count_a

    return sum(difference_a.values()) + sum(difference_b.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
