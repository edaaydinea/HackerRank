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
    # Write your code here
    strr = list(s)
    palindrome = list(s)

    l = 0
    r = n - 1

    while l <= r:
        if strr[l] != strr[r]:
            palindrome[l] = palindrome[r] = max(strr[l], strr[r])
            k -= 1
        l += 1
        r -= 1

    if k < 0:
        return "-1"

    l = 0
    r = n - 1

    while l <= r:
        if l == r:
            if k > 0:
                palindrome[l] = "9"

        if palindrome[l] < "9":
            if k >= 2 and palindrome[l] == strr[l] and palindrome[r] == strr[r]:
                k -= 2
                palindrome[l] = palindrome[r] = "9"

            elif k >= 1 and (palindrome[l] != strr[l] or palindrome[r] != strr[r]):
                k -= 1
                palindrome[l] = palindrome[r] = "9"

        l += 1
        r -= 1

    return "".join(palindrome)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
