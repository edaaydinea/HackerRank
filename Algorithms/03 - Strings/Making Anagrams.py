#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    S1 = [0] * 26
    for char in s1:
        S1[ord(char) - 97] += 1

    S2 = [0] * 26
    for char in s2:
        S2[ord(char) - 97] += 1

    deletions = 0
    for i in range(len(S1)):
        deletions += math.fabs(S1[i] - S2[i])

    return int(deletions)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
