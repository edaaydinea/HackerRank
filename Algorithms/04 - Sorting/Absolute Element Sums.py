#!/bin/python3

import os


#
# Complete the 'playingWithNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def playingWithNumbers(n, arr, queries):
    # Write your code here
    count = [0] * 4001
    for i in arr:
        count[2000 + i] += 1

    sum_num_right = [n]

    for i in range(4000):
        sum_num_right.append(sum_num_right[i] - count[i])

    sum_right = [0] * 4001
    for i in range(4001):
        sum_right[0] += count[i] * i

    for i in range(1, 4001):
        sum_right[i] = sum_right[i - 1] - sum_num_right[i]

    sum_left = [0] * 4001
    for i in range(4000, -1, -1):
        sum_left[4000] += count[i] * (4000 - i)

    for i in range(3999, -1, -1):
        sum_left[i] = sum_left[i + 1] - (n - sum_num_right[i + 1])

    acc = 0
    result = []
    for i in queries:
        acc += i
        mid = 2000 - acc
        if 4001 > mid >= 0:
            result.append(sum_right[mid] + sum_left[mid])
        elif mid < 0:
            result.append(sum_right[0] + n * abs(mid))
        else:
            result.append(sum_left[4000] + n * (mid - 4000))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().split()))

    q = int(input().strip())

    queries = list(map(int, input().split()))

    result = playingWithNumbers(n, arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
