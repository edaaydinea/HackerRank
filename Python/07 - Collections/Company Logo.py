#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    S = input()
    S = sorted(S)

    frequency = Counter(list(S))

    for key, value in frequency.most_common(3):
        print(key, value)
