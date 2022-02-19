#!/bin/python3

import os


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    y = [[] for _ in range(n)]
    result = []
    for i in queries:
        if i[0] == 1:
            x = (i[1] ^ lastAnswer) % n
            y[x].append(i[2])
        else:
            x = (i[1] ^ lastAnswer) % n
            lastAnswer = y[x][i[2] % len(y[x])]
            result.append(lastAnswer)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
