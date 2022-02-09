#!/bin/python3

import sys
sys.setrecursionlimit(1000000)


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(number):
    # Write your code here
    while number > 9:
        number = sum(map(int, str(number)))
    return number


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(superDigit(superDigit(n) * k))