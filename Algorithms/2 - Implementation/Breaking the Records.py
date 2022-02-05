#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    low_value = scores[0]
    high_value = scores[0]
    low_breaking = 0
    high_breaking = 0
    
    for i in range(1, len(scores)):
        if scores[i] < low_value:
            low_breaking +=1
            low_value = scores[i]
        
        if scores[i] > high_value:
            high_breaking += 1
            high_value = scores[i]
    
    return [high_breaking, low_breaking]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
