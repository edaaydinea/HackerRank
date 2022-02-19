#!/bin/python3


#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    i = 1
    switch = False
    while i < len(arr):
        j = i
        switch = False
        while arr[j] < arr[j - 1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            switch = True
            j -= 1
        i += 1
        for num in arr:
            print(num, "", end="")
            if arr.index(num) == len(arr) - 1:
                print()


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
