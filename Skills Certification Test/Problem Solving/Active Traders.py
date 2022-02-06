#!/bin/python3

import math
import os
import random
import re
import sys



from collections import defaultdict

#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    # Write your code here
    default_dict = defaultdict(int)
    for customer in customers:
        default_dict[customer] +=1
    return sorted([c for c, count in default_dict.items() if count / len(customers)>= 0.05])
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
