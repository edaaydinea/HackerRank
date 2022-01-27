#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    n = len(s)
    sub_strings = {}
    anagrams = 0

    for i in range(n):
        for j in range(i+1, n+1):
            sub = "".join(sorted(s[i:j]))

            if sub in sub_strings:
                sub_strings[sub] +=1
            else:
                sub_strings[sub] = 1

    for i in sub_strings:
        n = sub_strings[i] - 1
        anagrams += ((n * (n+1)) // 2)

    return anagrams

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
