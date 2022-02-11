#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    string = list(s)
    res = 0
    first = []
    second = []

    if len(string) % 2 == 1:
        first = list(map(lambda x: ord(x), string[: len(string) // 2]))
        first = first[::-1]
        second = list(map(lambda x: ord(x), string[len(string) // 2 + 1:]))
    else:
        first = list(map( lambda x: ord(x), string[: len(string) // 2 - 1]))
        first = first[::-1]
        second = list(map(lambda x: ord(x), string[len(string) // 2 + 1:]))
        res = abs(ord(string[len(string) // 2 - 1]) - ord(string[len(string) // 2]))

    for i in range(len(first)):
        if first[i] != second[i]:
            res += abs(first[i] - second[i])
            first[i] = min(first[i], second[i])
            second[i] = first[i]

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input().strip()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
