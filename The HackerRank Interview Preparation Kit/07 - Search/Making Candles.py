#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    # Write your code here
    days = 0
    candies = 0
    answer = math.ceil(n / (m * w))

    while days < answer:
        if p > candies:
            daysNeeded = math.ceil((p - candies) / (m * w))
            candies += daysNeeded * m * w
            days += daysNeeded

        diff = abs(m - w)
        available = candies // p
        purchased = min(diff, available)

        if m < w:
            m += purchased
        else:
            w += purchased

        rest = available - purchased
        m += rest // 2
        w += rest - rest // 2
        candies -= available * p

        candies += m * w
        days += 1

        remainingCandies = max(n - candies, 0)
        answer = min(answer, days + math.ceil(remainingCandies / (m * w)))

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
