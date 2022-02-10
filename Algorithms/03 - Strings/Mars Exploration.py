#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    num_errors = 0

    for i, char in enumerate(s):
        if i % 3 == 1:
            if char != "O":
                num_errors += 1
        else:
            if char != "S":
                num_errors += 1

    return num_errors


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
