#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(plants):
    # Write your code here
    plants.append(-1)
    answer = 0
    stack = []

    for i, plant in enumerate(plants):
        days = 1
        while stack and stack[-1][0] >= plant:
            days = max(days, stack[-1][1] + 1)
            stack.pop()

        if not stack:
            days -= 1

        answer = max(answer, days)
        stack.append((plant, days))

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
