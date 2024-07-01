#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxPresentations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY scheduleStart
#  2. INTEGER_ARRAY scheduleEnd
#

# Conference Schedule Problem
# A schedule has just been releases for an upcoming tech conference. The schedule provides the start and end times of each of the presentations. Once a presentation has begun, no one can enter or leave the room. It takes no time to go from one presentation to another. Determine the maximum number of presentations that can be attended by one person.

# Example
# n = 3
# scheduleStart = [1, 1, 2]
# scheduleEnd = [3, 2, 4]
# The maximum number of presentations that can be attended is 2. One possible schedule is to attend the first and third presentations.



def maxPresentations(scheduleStart, scheduleEnd):
    # Write your code here
    # Create a list of tuples (start, end)
    presentations = list(zip(scheduleStart, scheduleEnd))
    
    # Sort the presentations based on their end times
    presentations.sort(key=lambda x: x[1])
    
    # Initialize count of presentations and the end time of the last attended presentation
    count = 0
    last_end_time = 0
    
    # Iterate through the sorted presentations
    for start, end in presentations:
        if start >= last_end_time:
            # Attend this presentation
            count += 1
            last_end_time = end
    
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scheduleStart_count = int(input().strip())

    scheduleStart = []

    for _ in range(scheduleStart_count):
        scheduleStart_item = int(input().strip())
        scheduleStart.append(scheduleStart_item)

    scheduleEnd_count = int(input().strip())

    scheduleEnd = []

    for _ in range(scheduleEnd_count):
        scheduleEnd_item = int(input().strip())
        scheduleEnd.append(scheduleEnd_item)

    result = maxPresentations(scheduleStart, scheduleEnd)

    fptr.write(str(result) + '\n')

    fptr.close()
