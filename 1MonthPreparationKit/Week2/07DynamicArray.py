#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# Declare a 2-dimensional array, arr of n empty arrays. All arrays are zero indexed.
# Declare an integer, lastAnswer, and initialize it to 0.
# There are 2 types of queries, given as an array of strings for you to parse:
# 1. Query: 1 x y
# Find the list at index ((x XOR lastAnswer) % n) in arr.
# Append the integer y to the list.

# 2. Query: 2 x y
# Find the list at index ((x XOR lastAnswer) % n) in arr.
# Find the value of element y % size in the list where size is the size of the list and assign it to lastAnswer.
# Store the new value of lastAnswer to an answers array.

def dynamicArray(n, queries):
    # Write your code here
    
    # Initialize the 2-dimensional array
    arr = [[] for _ in range(n)]
    
    # Initialize the last answer
    lastAnswer = 0
    
    # Initialize the answers array
    answers = []
    
    # Iterate through the queries
    for query in queries:
        # Parse the query
        q, x, y = query
        
        # Find the index
        index = (x ^ lastAnswer) % n
        
        # Perform the query
        if q == 1:
            arr[index].append(y)
        else:
            lastAnswer = arr[index][y % len(arr[index])]
            answers.append(lastAnswer)
    
    return answers    

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
