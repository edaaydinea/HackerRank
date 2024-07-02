#!/bin/python3

# In the 20×20 grid below, four numbers along a diagonal line have been marked in bold.

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

# Input Format
# Input consists of 20 lines each containing 20 integers.

# Output Format
# Print the required answer.

# Constraints
# 0 ≤ grid[i][j] ≤ 100

# Sample Input


import sys

# Reading the grid from input
grid = []
for _ in range(20):
    grid.append(list(map(int, input().strip().split())))

# Direction vectors for right, down, diagonal-right-down, diagonal-left-down
directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

max_product = 0

# Iterate through each cell in the grid
for i in range(20):
    for j in range(20):
        # Check in all 4 directions
        for di, dj in directions:
            # Calculate product of four adjacent numbers in the current direction
            product = 1
            for step in range(4):
                ni, nj = i + step * di, j + step * dj
                if 0 <= ni < 20 and 0 <= nj < 20:
                    product *= grid[ni][nj]
                else:
                    product = 0  # out of bounds, reset product to 0
                    break
            # Update max_product if the current product is greater
            if product > max_product:
                max_product = product

print(max_product)

            

