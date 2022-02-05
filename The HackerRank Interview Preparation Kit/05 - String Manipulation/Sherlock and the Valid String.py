#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    frequency = {}

    for char in s:
        frequency.setdefault(char, 0)
        frequency[char] += 1

    values = list(frequency.values())
    first = values[0]
    accumlated_difference = 0

    for i in values:
        diff = abs(i - first)
        accumlated_difference += diff if i != 1 else 1

        if accumlated_difference > 1:
            return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
