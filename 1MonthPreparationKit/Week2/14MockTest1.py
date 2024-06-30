#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# Given a string ot lowercase letters in the range ascii[a-z], determine a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.
# Example
# s = "bcbc"
# If we remove 'b' at index 0, the string becomes "cbc" which is a palindrome. If we remove 'c' at index 3, the string becomes "bcb" which is a palindrome. If we remove 'c' at index 1, the string becomes "bbc" which is not a palindrome.
# In this case, the answer is 1.



def palindromeIndex(s):
    # Write your code here
    
    # Initialize the left and right pointers
    left = 0
    right = len(s) - 1
    
    # While the left pointer is less than the right pointer
    while left < right:
        # If the characters at the left and right pointers are different
        if s[left] != s[right]:
            # Check if removing the character at the left pointer makes the string a palindrome
            if s[left + 1] == s[right] and s[left + 2] == s[right - 1]:
                return left
            # Otherwise, check if removing the character at the right pointer makes the string a palindrome
            elif s[left] == s[right - 1] and s[left + 1] == s[right - 2]:
                return right
            # If neither of the above conditions are met, return -1
            else:
                return -1
        # Increment the left pointer and decrement the right pointer
        left += 1
        right -= 1
    
    # If the string is already a palindrome, return -1
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
