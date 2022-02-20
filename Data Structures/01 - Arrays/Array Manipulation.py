#!/bin/python3

import os


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    max_value = 0
    total_sum = 0
    array = [0] * (n + 1)

    for query in queries:
        left_index = query[0]
        right_index = query[1]
        summand = query[2]

        array[left_index - 1] += summand
        array[right_index] -= summand

    for value in array:
        total_sum += value
        max_value = max(max_value, total_sum)
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
