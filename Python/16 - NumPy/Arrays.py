import numpy

def arrays(arr):
    # complete this function
    return(numpy.array(arr[::-1], float))
arr = input().strip().split(' ')
result = arrays(arr)
print(result)