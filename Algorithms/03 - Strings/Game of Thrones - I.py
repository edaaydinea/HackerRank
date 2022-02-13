#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    string = sorted(s)
    current_letter_count = 1
    middle = False
    for index, char in enumerate(list(string[1:])):
        if string[index] != char:
            if current_letter_count % 2:
                if not middle:
                    middle = True
                else:
                    return "NO"
        current_letter_count += 1
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
