#!/bin/python3

import os


#
# Complete the 'stringSimilarity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringSimilarity(s):
    # Write your code here
    result = length = len(s)
    right = 0
    left = 0
    z = [length]

    for i in range(1, length):
        z.append(0)
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < length and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1

        result += z[i]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()
