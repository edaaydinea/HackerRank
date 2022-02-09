#!/bin/python3

import os


#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def stepPerms(number):
    # Write your code here
    ds = [0] * max(3, number + 1)
    ds[0] = 1
    ds[1] = 1
    ds[2] = ds[1] + ds[0]

    for i in range(3, number + 1):
        ds[i] = (ds[i - 1] + ds[i - 2] + ds[i - 3]) % 10000000007

    return ds[number]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
