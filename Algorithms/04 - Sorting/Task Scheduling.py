#!/bin/python3

import os


#
# Complete the 'taskScheduling' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER m
#

def binarySearch(array, number, si, ei):
    if si == ei:
        if number >= array[si]:
            return si
        else:
            return si - 1
    else:
        middle = (ei - si) // 2 + si
        if number > array[middle]:
            return binarySearch(array, number, middle + 1, ei)
        elif number < array[middle]:
            return binarySearch(array, number, si, middle)
        else:
            return middle


def returnIndex(array, number):
    if not array:
        return None
    if len(array) == 1:
        if number > array[0]:
            return 0
        else:
            return None

    si = 0
    ei = len(array) - 1
    return binarySearch(array, number, si, ei)


def taskScheduling(length, array, deadline, minutes, late):
    if length < deadline:
        for i in range(deadline - length):
            array.append(i + length)
        length = deadline

    min_left = minutes
    index = returnIndex(array, deadline - 1)
    if index is not None:
        while index >= 0 and min_left > 0:
            array.pop(index)
            index -= 1
            min_left -= 1

    while min_left > 0 and array and array[0] < deadline:
        array.pop(0)
        min_left -= 1
    late += min_left
    return late, length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    length, late = 0, 0
    array = []

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        late, length = taskScheduling(length, array, d, m, late)

        fptr.write(str(late) + '\n')

    fptr.close()
