"""
Author: Eda AYDIN

N: the total number of students
the names of the columns in any order
"""

from collections import namedtuple

N = int(input())
Student = namedtuple("Student", input())

result = sum([int(Student(*input().split()).MARKS) for i in range(N)]) / N

print("{:.2f}".format(result))
