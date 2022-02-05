#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    palindrome_count = 0

    for i in range(n):
        j = 0

        while i + j < n and s[i] == s[i + j]:
            j += 1
            palindrome_count += 1

        if i + j + j > n:
            continue

        for k in range(1, j + 1):
            if i + j + k >= n or s[i] != s[i + j + k]:
                break
        else:
            palindrome_count += 1

    return palindrome_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
