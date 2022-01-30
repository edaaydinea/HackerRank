#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

import os
from collections import defaultdict


def frequency(s):
    result = defaultdict(int)

    for char in s:
        result[char] += 1
    return result


def reverseShuffleMerge(s):
    # Write your code here
    char_frequency = frequency(s)
    used_chars = defaultdict(int)
    remain_chars = dict(char_frequency)
    result = []

    def can_use(char):
        return (char_frequency[char] // 2 - used_chars[char]) > 0

    def can_pop(char):
        needed_chars = char_frequency[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars

    for char in reversed(s):
        if can_use(char):
            while result and result[-1] > char and can_pop(result[-1]):
                removed_char = result.pop()
                used_chars[removed_char] -= 1

            used_chars[char] += 1
            result.append(char)

        remain_chars[char] -= 1

    return "".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = reverseShuffleMerge(s)
    fptr.write(result + '\n')
    fptr.close()
