#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally. The game is played as follows:
# Initially there are n towers. 
# Each tower is of height m.
# The players move in alternating turns. 
# In each turn, a player can choose a tower of height x and reduce its height to y, where 1 <= y < x and y divides x.
# If the current player is unable to make a move, they lose the game.

# Given the values of n and m, determine which player wins the game. If the first player wins, return 1. Otherwise, return 2.

def towerBreakers(n, m):
    # Write your code here
    
    # If there is only one tower, the first player wins
    if n == 1:
        return 1
    
    # If the number of towers is even, the second player wins
    if n % 2 == 0:
        return 2
    
    # If the number of towers is odd and the height of the towers is 1, the second player wins
    if m == 1:
        return 2
    
    # If the number of towers is odd and the height of the towers is greater than 1, the first player wins
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
