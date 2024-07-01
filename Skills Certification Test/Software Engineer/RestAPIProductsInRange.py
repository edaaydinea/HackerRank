#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getProductsInRange' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/inventory?category=<category>&page=<pageNumber>
#
# The function is expected to return an Integer value.
# The function accepts String category, Integer minPrice and Integer maxPrice as arguments.
#

import requests

def getProductsInRange(category, minPrice, maxPrice):
    url_template = "https://jsonmock.hackerrank.com/api/inventory"
    page_number = 1
    total_items = 0
    
    while True:
        url = f"{url_template}?category={category}&page={page_number}"
        response = requests.get(url)
        data = response.json()
        
        # Extract relevant information from the response
        items = data.get('data', [])
        
        # If no items are returned, break out of the loop
        if not items:
            break
        
        # Filter items based on price range
        for item in items:
            price = item.get('price', 0.0)
            if minPrice <= price <= maxPrice:
                total_items += 1
        
        # Move to the next page
        page_number += 1
    
    return total_items

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    category = input()

    minPrice = int(input().strip())
    
    maxPrice = int(input().strip())

    result = getProductsInRange(category, minPrice, maxPrice)

    fptr.write(str(result) + '\n')

    fptr.close()
