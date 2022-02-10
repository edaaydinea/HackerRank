#!/bin/python3

import os


#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    numbers_count = 1
    lower_case_count = 1
    upper_case_count = 1
    special_char_count = 1

    for char in password:
        if char in numbers:
            numbers_count = 0
        elif char in lower_case:
            lower_case_count = 0
        elif char in upper_case:
            upper_case_count = 0
        elif char in special_characters:
            special_char_count = 0

    return max(6 - n, numbers_count + lower_case_count + upper_case_count + special_char_count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
