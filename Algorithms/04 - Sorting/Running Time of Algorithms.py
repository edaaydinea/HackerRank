#!/bin/python3

import os


#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def runningTime(arr):
    # Write your code here
    if len(arr) <= 1:
        print(0)
        return (arr)
    else:
        shifts = 0

        for j in range(1, len(arr)):
            for i in reversed(range(j)):
                if arr[i + 1] < arr[i]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    shifts += 1
                else:
                    break

        return shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
