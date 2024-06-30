#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# Two words are anagrams of one another if their letters can be rearranged to form the other word.
# Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

# Example
# s = 'abccde'
# Break s into two parts: 'abc' and 'cde'.
# Note that all letters have been used, the substrings are contiguous and their lengths are equal. 
# Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams.
# Two changes were necessary.



def anagram(s):
    # Write your code here
    
    # If the length of the string is odd, return -1
    if len(s) % 2 != 0:
        return -1  
    
    # Split the string into two parts
    mid = len(s) // 2
    first = s[:mid]
    second = s[mid:]
    
    # Initialize a list of unique characters in the second part
    unique_chars = list(set(second))
    
    # Initialize the number of changes needed
    changes_needed = 0
    
    # Iterate through the unique characters in the second part
    for char in unique_chars:
        # Increment the number of changes needed by the maximum of the difference between the count of the character in the second part and the count of the character in the first part and 0
        changes_needed += max(second.count(char) - first.count(char), 0)
        
    # Return the number of changes needed
    return changes_needed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
