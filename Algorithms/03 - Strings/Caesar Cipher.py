#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here

    length = len(s)
    for i in range(length):
        if ord("Z") >= ord(s[i]) >= ord("A"):
            asciiCode = ord(s[i]) + k
            while asciiCode > ord("Z"):
                asciiCode = asciiCode - ord("Z") + ord("A") - 1
            s[i] = chr(asciiCode)
        elif ord("z") >= ord(s[i]) >= ord("a"):
            asciiCode = ord(s[i]) + k
            while asciiCode > ord("z"):
                asciiCode = asciiCode - ord("z") + ord("a") -1
            s[i] = chr(asciiCode)

    return "".join(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(input())

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
