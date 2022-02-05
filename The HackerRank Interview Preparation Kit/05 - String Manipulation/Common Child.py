#!/bin/python3

import os


#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    last_row = [0] * (len(s1) + 1)

    for i in range(1, len(s1) + 1):
        current = [0]
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                current.append(last_row[j - 1] + 1)
            else:
                current.append(max(last_row[j], current[-1]))
        last_row = current

    return last_row[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
