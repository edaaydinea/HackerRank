#!/bin/python3

import os


#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x.sort()
    l = list()

    l = [0 for i in range(100001)]

    for i in x:
        l[i - 1] = 1

    x = []
    for i in range(100001):
        if l[i] == 1:
            x.append(i + 1)

    start = 0
    i = 0
    c = 1
    n = len(x)
    while i < n:
        if x[i] <= x[start] + k:
            i += 1
            continue
        else:
            s = i - 1
            while i < n and x[s] + k >= x[i]:
                i += 1
            start = i
            if i < n:
                c += 1

    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
