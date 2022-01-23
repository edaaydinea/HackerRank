"""
Problem: https://www.hackerrank.com/challenges/python-power-mod-power/problem

Author: Eda AYDIN
"""
import math

a = int(input())
b = int(input())
m = int(input())

print(int(math.pow(a, b)))
print(int(math.fmod(math.pow(a, b), m)))
