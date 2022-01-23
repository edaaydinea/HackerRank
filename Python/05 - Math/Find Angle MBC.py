"""
Problem:https://www.hackerrank.com/challenges/find-angle/problem

Author: Eda AYDIN
"""

import math

ab = int(input())
bc = int(input())

hypotenuse = math.sqrt(math.pow(ab, 2) + math.pow(bc, 2))
edge1 = hypotenuse / 2.0
edge2 = bc / 2.0
degree_sign = u'\N{DEGREE SIGN}'
print("{}{}".format(str(int(round(math.degrees(math.acos(edge2 / edge1))))), degree_sign))
