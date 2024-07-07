#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().
# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:
#     It contains no unmatched brackets.
#     The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

def isBalanced(s):
    # Write your code here
    
    # Create a stack to store the brackets
    stack = []
    
    # Create a dictionary to store the brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    # Iterate through the string
    for bracket in s:
        # If the bracket is an opening bracket, append it to the stack
        if bracket in brackets.values():
            stack.append(bracket)
        # If the bracket is a closing bracket
        else:
            # If the stack is empty or the bracket does not match the last bracket in the stack, return 'NO'
            if not stack or brackets[bracket] != stack.pop():
                return 'NO'
            
    # If the stack is empty, return 'YES'
    if not stack:
        return 'YES'
    # Otherwise, return 'NO'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
