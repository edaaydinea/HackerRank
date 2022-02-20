#!/bin/python3
import collections
import os


#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER money : the amount money they have to spend
#  2. INTEGER_ARRAY cost : the cost of each flavor of ice cream
#

def icecreamParlor(money, cost):
    # Write your code here
    d = collections.Counter(cost)
    result = []
    for sunny in cost:
        johnny = money - sunny
        if sunny != johnny:
            if d[johnny] > 0:
                j = cost.index(johnny)
                result.extend((cost.index(sunny) + 1, j + 1))
                return result
        else:
            if d[johnny] > 1:
                j = cost[cost.index(johnny) + 1:].index(johnny)
                result.extend((cost.index(sunny) + 1, j + 2 + cost.index(sunny)))
                return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        result = icecreamParlor(money, cost)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
