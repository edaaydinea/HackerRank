#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    changed = True
    while changed and s != "":
        changed = False
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                changed = True
                s = s[:i] + s[(i + 2):]
                break
    if s == "":
        return "Empty String"
    else:
        return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
