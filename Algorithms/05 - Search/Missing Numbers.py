#!/bin/python3
import collections
import os


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#


def missingNumbers(arr, brr):
    # Write your code here
    if len(arr) > len(brr):
        brr, arr = arr, brr

    l = []
    for k in brr.keys():
        if k not in arr or arr[k] < brr[k]:
            l.append(k)

    return sorted(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = collections.Counter(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = collections.Counter(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
