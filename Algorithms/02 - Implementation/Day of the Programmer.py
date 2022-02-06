#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    
    result = 0

    if year > 1918 and year <= 2700:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            counter = 1
            if counter == 1:
                result = "12.09.{}".format(str(year))
        else:
            result = "13.09.{}".format(str(year))
    
    if year < 1918 and year >= 1700:
        if year % 4 == 0:
            counter = 1
            if counter == 1:
                result = "12.09.{}".format(str(year))
        else:
            result = "13.09.{}".format(str(year))
    
    if year == 1918:
        result = "26.09.1918"
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(str(result) + '\n')

    fptr.close()
