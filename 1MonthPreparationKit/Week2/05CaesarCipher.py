#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

# Example
# s = middle-Outz
# k = 2

# The alphabet is rotated by 2, so the encrypted string is okffng-Qwvb.


def caesarCipher(s, k):
    # Write your code here
    
    # Create a list with the alphabet
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    
    # Create a dictionary with the alphabet and the rotated alphabet
    rotated_alphabet = {}
    
    # Iterate over the alphabet
    for i in range(26):
        # Calculate the index of the rotated alphabet
        index = (i + k) % 26
        # Add the letter and the rotated letter to the dictionary
        rotated_alphabet[alphabet[i]] = alphabet[index]
        
    # Create a list to store the encrypted string
    encrypted_string = []
    
    # Iterate over the string
    for letter in s:
        # If the letter is in the rotated alphabet, add the rotated letter to the encrypted string
        if letter.lower() in rotated_alphabet:
            if letter.isupper():
                encrypted_string.append(rotated_alphabet[letter.lower()].upper())
            else:
                encrypted_string.append(rotated_alphabet[letter])
        # If the letter is not in the rotated alphabet, add the letter to the encrypted string
        else:
            encrypted_string.append(letter)
            
    # Return the encrypted string
    return ''.join(encrypted_string)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
