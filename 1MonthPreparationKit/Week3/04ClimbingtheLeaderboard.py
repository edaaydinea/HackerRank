#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
# - The player with the highest score is ranked number 1 on the leaderboard.
# - Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

# Example
# ranked = [100, 90, 90, 80]
# player = [70, 80, 105]

# The ranked players will have ranks 1, 2, 2, and 3, respectively. If the player's scores are 70, 80, and 105, their rankings after each game are 4th, 3rd, and 1st. Return [4, 3, 1].


def climbingLeaderboard(ranked, player):
    # Write your code here
    
    # Create a set to store the unique scores
    scores = sorted(set(ranked), reverse=True)
    
    # Create a list to store the rankings
    rankings = []
    
    # Initialize the index of the scores
    i = len(scores) - 1
    
    # Iterate over the player scores
    for score in player:
        # While the score is greater than the current score, decrease the index
        while i >= 0 and score >= scores[i]:
            i -= 1
        # Append the ranking to the rankings list
        rankings.append(i + 2)
        
    return rankings
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
