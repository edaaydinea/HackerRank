import numpy

poly = [float(x) for x in input().split()]
x = float(input())

print(numpy.polyval(poly, x))