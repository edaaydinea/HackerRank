#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    found = False

    for i in range(len(s) // 2):
        a = s[:i + 1]
        f = n = int(s[:i + 1])
        while len(a) < len(s):
            n += 1
            a += str(n)
        if a == s:
            found = True
            print("YES", f)
            break
    if not found:
        print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
