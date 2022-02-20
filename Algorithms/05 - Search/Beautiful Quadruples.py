#!/bin/python3

import os


#
# Complete the beautifulQuadruples function below.
#
def beautifulQuadruples(a, b, c, d):
    #
    # Write your code here.
    #
    a, b, c, d = sorted((int(a), int(b), int(c), int(d)))

    total = [0] * 3010
    count = [[0 for j in range(4200)] for i in range(3010)]

    for i in range(1, a + 1):
        for j in range(i, b + 1):
            total[j] += 1
            count[j][i ^ j] += 1
    for i in range(1, 3001):
        total[i] += total[i - 1]
        for j in range(4101):
            count[i][j] += count[i - 1][j]

    result = 0

    for i in range(1, c + 1):
        for j in range(i, d + 1):
            result += total[i] - count[i][i ^ j]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])

    b = int(abcd[1])

    c = int(abcd[2])

    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()
