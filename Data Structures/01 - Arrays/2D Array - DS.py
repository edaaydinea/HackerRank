#!/bin/python3

import os


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(array):
    # Write your code here

    maximum = -9 * 7

    for i in range(len(array)):
        for j in range(len(array)):
            if j + 2 < 6 and i + 2 < 6:
                result = array[i][j] + array[i][j + 1] + array[i][j + 2] + \
                         array[i + 1][j + 1] + \
                         array[i + 2][j] + array[i + 2][j + 1] + array[i + 2][j + 2]
                if result > maximum:
                    maximum = result
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
