#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Convert the input time string to a datetime object
    time_obj = datetime.strptime(s, '%I:%M:%S%p')

    # Convert the datetime object to military time format
    military_time = time_obj.strftime('%H:%M:%S')

    return military_time
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
