#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

text_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}


# Complete the timeInWords function below.
def timeInWords(h: int, m: int):
    # o' clock case
    if m == 0:
        hours = text_dict[h]
        return f'{hours} o\' clock'
    elif m == 30:
        return f'half past {text_dict[h]}'

    if m > 40:
        minutes = 60 - m

        minutes_text = text_dict[minutes]

        if m == 45:
            m_text = ''
        else:
            m_text = 'minutes '

        return f'{minutes_text} {m_text}to {text_dict[h + 1]}'
    elif m == 40:
        return f'twenty minutes to {text_dict[h + 1]}'
    elif m > 30:
        minutes = str(60 - m)

        return f'twenty {text_dict[int(minutes[1])]} minutes to {text_dict[h + 1]}'
    elif m == 20:
        return f'twenty minutes past {text_dict[h]}'
    elif m > 20:
        minutes = str(m)
        return f'twenty {text_dict[int(minutes[1])]} minutes past {text_dict[h]}'
    else:
        minutes_text = text_dict[m]

        if m == 15:
            m_text = ''
        elif m > 1:
            m_text = 'minutes '
        else:
            m_text = 'minute '

        return f'{minutes_text} {m_text}past {text_dict[h]}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
