#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    stack = list()
    index = 0
    largest_rectangle = 0

    while index < len(h):
        if (not stack) or (h[stack[-1]] <= h[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (h[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            largest_rectangle = max(largest_rectangle, area)

    while stack:
        top_of_stack = stack.pop()
        area = (h[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
        largest_rectangle = max(largest_rectangle, area)

    return largest_rectangle


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
