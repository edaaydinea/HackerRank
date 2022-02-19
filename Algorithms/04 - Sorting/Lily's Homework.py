#!/bin/python3

import os


#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    sortedArr = sorted(arr)
    reversedArr = list(reversed(arr))

    d = {}

    for i in range(len(arr)):
        if sortedArr[i] not in d:
            d[sortedArr[i]] = i

    swaps = 0
    i = 0
    while i < len(arr):
        if sortedArr[i] == arr[i]:
            i += 1
            continue
        swaps += 1
        arr[d[arr[i]]], arr[i] = arr[i], arr[d[arr[i]]]
        d[sortedArr[i]] += 1

    d = {}
    for i in range(len(arr)):
        if sortedArr[i] not in d:
            d[sortedArr[i]] = i

    swaps_reversed = 0
    i = 0
    while i < len(arr):
        if sortedArr[i] == reversedArr[i]:
            i += 1
            continue
        swaps_reversed += 1
        reversedArr[d[reversedArr[i]]], reversedArr[i] = reversedArr[i], reversedArr[d[reversedArr[i]]]
        d[sortedArr[i]] += 1

    return min(swaps, swaps_reversed)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
