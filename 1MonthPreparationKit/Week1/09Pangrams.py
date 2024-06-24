#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# A pangram is a string that contains every letter of alphabet at least once. Given a sentence determine whether it is a pangram in the English alphabet. Return either pangram or not pangram.

# s = "The quick brown fox jumps over the lazy dog" or "We promptly judged antique ivory buckles for the next prize"
# The sentence contains all the letters of the English alphabet, so return pangram. The sentence does not contain the letter x, so return not pangram.


def pangrams(s):
    # Write your code here
    # Create a set of the input string
    s = set(s.lower())
    # Create a set of the English alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # Check if the input string contains all the letters of the English alphabet
    if alphabet.issubset(s):
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
