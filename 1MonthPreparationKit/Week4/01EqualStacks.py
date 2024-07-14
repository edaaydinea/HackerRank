#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

# You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then return the height.

# Steps:
# 1. Initial Setup: 
# - Calculate the total height of each stack.
# - Compare the total heights and remove cyclinders from the stack(s) with the greatest height until all stacks are equal heights.

# 2. Steps:
# Step 1: Calculate the total height of each stack.
# Step 2: Remove the top cylinder from the stack with the greatest height.
# Step 3: Repeat steps 1 and 2 until all stacks are equal heights.
# Step 4: Return the height of the stacks.

# Consider the following example:
# h1 = [3, 2, 1, 1, 1]           Total height = 8
# h2 = [4, 3, 2]                 Total height = 9
# h3 = [1, 1, 4, 1]              Total height = 7

# The maximum height is 9 (h2). Remove the top cyclinder grom h2: h2 = [3, 2]. The new heights are:
# h1 = [3, 2, 1, 1, 1]           Total height = 8
# h2 = [3, 2]                    Total height = 5
# h3 = [1, 1, 4, 1]              Total height = 7

# The maximum height is 8 (h1). Remove the top cyclinder grom h1: h1 = [2, 1, 1, 1]. The new heights are:
# h1 = [2, 1, 1, 1]              Total height = 5
# h2 = [3, 2]                    Total height = 5
# h3 = [1, 1, 4, 1]              Total height = 7

# The maximum height is 7 (h3). Remove the top cyclinder grom h3: h3 = [1, 1, 4]. The new heights are:
# h1 = [2, 1, 1, 1]              Total height = 5
# h2 = [3, 2]                    Total height = 5
# h3 = [1, 1, 4]                 Total height = 6

# The maximum height is 6 (h3). Remove the top cyclinder grom h3: h3 = [1, 4]. The new heights are:
# h1 = [2, 1, 1, 1]              Total height = 5
# h2 = [3, 2]                    Total height = 5
# h3 = [1, 4]                    Total height = 5

# Now all stacks are equal heights. The height is 5.

def equalStacks(h1, h2, h3):
    # Write your code here
    
    # Calculate the initial height of each stack
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)
    
    # Convert stacks to lists to allow pop operations
    h1, h2, h3 = h1[::-1], h2[::-1], h3[::-1]

    
    # Iterate until all stacks are equal heights
    while not(sum1 == sum2 == sum3):
        # Find the stack with the greatest height
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= h1.pop()
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= h2.pop()
        elif sum3 >= sum1 and sum3 >= sum2:
            sum3 -= h3.pop()
            
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
