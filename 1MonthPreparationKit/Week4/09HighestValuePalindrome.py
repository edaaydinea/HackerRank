#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    s = list(s)

    least_changes = 0
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            least_changes += 1

    if least_changes > k:
        return '-1'

    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            if k > least_changes:
                if s[i] != '9':
                    s[i] = '9'
                    k -= 1
                if s[len(s) - i - 1] != '9':
                    s[len(s) - i - 1] = '9'
                    k -= 1
                least_changes -= 1
            else:
                s[i] = max(s[i], s[len(s) - i - 1])
                s[len(s) - i - 1] = max(s[i], s[len(s) - i - 1])
                least_changes -= 1
                k -= 1

        elif k - least_changes >= 2 and s[i] != '9':
            s[i] = '9'
            s[len(s) - i - 1] = '9'
            k -= 2

    if k > 0 and len(s) % 2 != 0:
        s[len(s) // 2] = '9'

    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
