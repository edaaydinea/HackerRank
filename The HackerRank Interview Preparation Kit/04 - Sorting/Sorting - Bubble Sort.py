#!/bin/python3


#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0
    size = len(a)

    for i in range(size):
        for j in range(i + 1, size):
            if a[j] < a[i]:
                a[i] = a[i] + a[j]
                a[j] = a[i] - a[j]
                a[i] = a[i] - a[j]
                count += 1

    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
