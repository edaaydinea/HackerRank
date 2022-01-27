#!/bin/python3

import os
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    time1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    return str(int(abs((time1 - time2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()
