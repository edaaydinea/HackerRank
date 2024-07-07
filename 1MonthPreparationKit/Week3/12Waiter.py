#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
# You are a waiter at a party. There are N stacked plates on pile A0. Create an empty answers array. At each iteration, i, remove each plate from the top of stack in order. Determine if the number on the plate is evenly divisible by the i-th prime number. If the number is evenly divisible, stack it on pile B. Otherwise, stack it on pile A. After all iterations are complete, stack the plates on pile B onto pile A. The first plate removed from pile A should be added to the answer array, then the plates from pile B, in order, and finally the rest of the plates from pile A. Return the answer array.

# Example
# number = [3, 4, 7, 6, 5]
# q = 1
# The first prime number is 2. The plates are divided into two piles as follows:
#     A = [4, 6]
#     B = [3, 7, 5]
# After the first iteration, the plates are in the following order:
#     B = [5, 7, 3]
#     A = [6, 4]
# The plates are printed in the following order:
#     5
#     7
#     3
#     6
#     4


def generate_primes_up_to_q(q):
    primes = []
    num = 2
    while len(primes) < q:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1
    return primes

def waiter(number, q):
    answers = []
    pile_A = number
    primes = generate_primes_up_to_q(q)
    
    for prime in primes:
        pile_B = []
        new_pile_A = []
        
        while pile_A:
            plate = pile_A.pop()
            if plate % prime == 0:
                pile_B.append(plate)
            else:
                new_pile_A.append(plate)
        
        # Add pile B plates in reverse order
        answers.extend(reversed(pile_B))
        # Update pile A to new pile A
        pile_A = new_pile_A
    
    # Add remaining plates in pile A (if any)
    answers.extend(reversed(pile_A))
    
    return answers
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
