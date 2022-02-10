#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def hackerrankInString(s):
    # Write your code here

    pattern = ".*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*"

    if re.search(pattern, s) is not None:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input().strip()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
