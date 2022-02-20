#!/bin/python3

import os


#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    dictionary = {price[i]: i for i in range(len(price))}
    price = sorted(price)

    minimum = 10000000

    for i in range(1, len(price)):
        if dictionary[price[i]] < dictionary[price[i - 1]]:
            minimum = min(minimum, price[i] - price[i - 1])

    return minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # number of years of house data

    price = list(map(int, input().rstrip().split()))  # space-separated long integers describe price[i]

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
