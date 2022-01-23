"""
Problem: https://www.hackerrank.com/challenges/s10-mcq-7/problem

Author: Eda AYDIN
"""
import math
import statistics
import sympy
import fractions

x, y = sympy.symbols('x y')

eq1 = sympy.Eq(3*x + 4*y + 8)
eq2 = sympy.Eq(4*x + 3*y + 7)

m1 = fractions.Fraction(-3/4)
m2 = fractions.Fraction(-3/4)

p2 = fractions.Fraction(math.sqrt(m1 * m2))




