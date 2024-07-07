#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

# Sherlock and the Valid String Problem
# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

# Example
# s = abc
# This is a valid string because frequencies are {a: 1, b: 1, c: 1}. It is also valid because we can remove 1 character at 1 index and have 1 frequency of each character.
# s = abcc
# This is not a valid string because frequencies are {a: 1, b: 1, c: 2}.

def isValid(s):
    # Create a dictionary to store the frequency of each character in the string
    freq = {}
    
    # Count the frequency of each character in the string
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    # Create a dictionary to store the frequency of each frequency
    freq_freq = {}
    
    # Count the frequency of each frequency
    for key in freq:
        if freq[key] in freq_freq:
            freq_freq[freq[key]] += 1
        else:
            freq_freq[freq[key]] = 1
            
    # If there is only one frequency, return YES
    if len(freq_freq) == 1:
        return "YES"
    
    # If there are more than two frequencies, return NO
    if len(freq_freq) > 2:
        return "NO"
    
    # If there are exactly two different frequencies
    if len(freq_freq) == 2:
        freq_values = list(freq_freq.keys())
        # Check if we can remove one character to make the string valid
        if (freq_values[0] == 1 and freq_freq[freq_values[0]] == 1) or (freq_values[1] == 1 and freq_freq[freq_values[1]] == 1):
            return "YES"
        # Check if we can decrease one frequency to make all frequencies the same
        if abs(freq_values[0] - freq_values[1]) == 1 and (freq_freq[freq_values[0]] == 1 or freq_freq[freq_values[1]] == 1):
            return "YES"
    
    # In any other case, return NO
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
