#!/bin/python3
import array
import bisect
import os


#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def insertionSort(arr):
    # Write your code here
    result = 0
    sarr = array.array("I", [arr[0]])
    for i in range(1, len(arr)):
        e = arr[i]
        j = bisect.bisect_right(sarr, e)
        sarr.insert(j, e)
        result += i - j
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
