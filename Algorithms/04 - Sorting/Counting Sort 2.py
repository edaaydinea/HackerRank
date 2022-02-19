#!/bin/python3

import os


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    answer = []
    count = [0] * 100
    for item in arr:
        count[item] += 1

    for i in range(100):
        if count[i] > 0:
            answer.extend([str(i)] * count[i])
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
