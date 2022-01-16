#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    s = []
    n = len(values)

    for i in range(n):
        s += [values[i]] * freqs[i]

    sumFreq = sum(freqs)
    mid = sumFreq // 2
    s.sort()

    if n % 2 != 0:
        q1 = statistics.median(s[:mid])
        q3 = statistics.median(s[mid + 1:])
    else:
        q1 = statistics.median(s[:mid])
        q3 = statistics.median(s[mid:])

    print("{:.1f}".format(q3 - q1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
