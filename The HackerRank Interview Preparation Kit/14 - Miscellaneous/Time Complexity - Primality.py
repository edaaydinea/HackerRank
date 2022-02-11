#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#


def primality(n):
    # Write your code here
    if n == 1:
        return "Not prime"
    if n == 2:
        return "Prime"

    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return "Not prime"
        i += 1

    return "Prime"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
