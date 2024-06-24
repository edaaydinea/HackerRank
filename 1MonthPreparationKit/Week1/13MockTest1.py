"""
Find the Media

The median of a list of numbers is essentially its middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, can you find the median?

Example:
arr = [0, 1, 2, 4, 6, 5, 3]
The sorted array is arr = [0, 1, 2, 3, 4, 5, 6] It's middle element is 3.

Sample Input 0:
7
0 1 2 4 6 5 3

Sample Output 0:
3
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    # Sort the array
    arr.sort()
    # Find the middle index
    mid = len(arr) // 2
    # Return the middle element
    return arr[mid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
