# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#       3
#      7 4
#     2 4 6
#    8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle given in input.

# Input Format
# First line contains T, the number of testcases. For each testcase:
# First line contains N, the number of rows in the triangle.
# For next N lines, i'th line contains i numbers.

# Constraints
# 1 <= T <= 10
# 1 <= N <= 15
# Numbers in the triangle are between 0 and 100.

# Output Format
# For each testcase, print the required answer in a newline.

# Sample Input
# 1
# 4
# 3
# 7 4
# 2 4 6
# 8 5 9 3

# Sample Output
# 23


def maximum_path_sum(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

for _ in range(int(input())):
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]
    print(maximum_path_sum(triangle))
    