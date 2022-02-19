#!/bin/python3

import os


#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def closestNumbers(arr):
    # Write your code here
    arr.sort()

    diff = 10 ** 8
    prev = arr.pop(0)
    for i in arr:
        if i - prev < diff:
            answer = [prev, i]
            diff = i - prev
        elif i - prev == diff:
            answer.append(prev)
            answer.append(i)
        prev = i
    answer.sort()
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
