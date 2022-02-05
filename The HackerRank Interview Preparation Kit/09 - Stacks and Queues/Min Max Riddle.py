#!/bin/python3

import os
from collections import defaultdict


# Complete the riddle function below.
def riddle(arr):
    # complete this function
    arr.append(-1)
    answer = [0] * (len(arr) - 1)

    d, stack = defaultdict(int), []
    for i, x in enumerate(arr):
        index = i

        while stack and stack[-1][0] >= x:
            y, index = stack.pop()
            d[i - index] = max(d[i - index], y)

        stack.append((x, index))

    current = 0

    for window in range(len(arr) - 1, 0, -1):
        current = max(current, d[window])
        answer[window - 1] = current

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
