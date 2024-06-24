"""
Flipping the Matrix

Sean invented a game involving a 2n x 2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times, and the goal of the game is to maximize the sum of the elements in the n x n submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal. For each matrix, print the maximized sum.

Example

matrix = 
[[112, 42, 83, 119],
[56, 125, 56, 49], 
[15, 78, 101, 43], 
[62, 98, 114, 108]]

If Sean reverses the row with the second row, the matrix will become 
[[112, 42, 83, 119], 
[62, 98, 114, 108],
[15, 78, 101, 43], 
[56, 125, 56, 49]]. 

The sum of the elements in the submatrix in the upper left is 312. It is the largest possible sum.


"""
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    # Get the length of the matrix
    n = len(matrix) // 2
    
    # Get the sum of the maximum values of the matrix
    sum_max = 0
    
    # Iterate through the matrix
    # Four possible elements:
    # 1. matrix[i][j]
    # 2. matrix[i][2 * n - 1 - j] : 2 * n - 1 - j is the index of the element in the same row but in the opposite column
    # 3. matrix[2 * n - 1 - i][j] : 2 * n - 1 - i is the index of the element in the same column but in the opposite row
    # 4. matrix[2 * n - 1 - i][2 * n - 1 - j] : 2 * n - 1 - i and 2 * n - 1 - j are the indices of the element in the opposite row and column respectively
    for i in range(n):
        for j in range(n):
            sum_max += max(matrix[i][j], 
                           matrix[i][2 * n - 1 - j], 
                           matrix[2 * n - 1 - i][j], 
                           matrix[2 * n - 1 - i][2 * n - 1 - j])
    return sum_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
