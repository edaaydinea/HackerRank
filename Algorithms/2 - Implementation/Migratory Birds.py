#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import operator

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    migration_dict = dict(Counter(arr))
    migration_dict = dict(sorted(migration_dict.items()))
    maximum_frequency = max(migration_dict, key=migration_dict.get)
    return maximum_frequency

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
