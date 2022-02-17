#!/bin/python3


#
# Complete the 'virusIndices' function below.
#
# The function accepts following parameters:
#  1. STRING p
#  2. STRING v
#

def match(word1, word2):
    length = len(word1)
    if length < 10:
        counter = 0
        for i in range(length):
            if word1[i] != word2[i]:
                counter += 1
                if counter > 1:
                    return False
        return True
    if length >= 10:
        word11 = word1[:length // 2]
        word12 = word1[length // 2:]
        word21 = word2[:length // 2]
        word22 = word2[length // 2:]

        s1 = (word11 == word21)
        s2 = (word12 == word22)

        if s1 and s2:
            return True
        elif s1 and not s2:
            return match(word12, word22)
        elif not s1 and s2:
            return match(word11, word21)
        else:
            return False


def virusIndices(p, v):
    # Print the answer for this test case in a single line
    result = ""
    if len(v) > len(p):
        return "No Match!"
    else:
        for i in range(len(p) - len(v) + 1):
            temp = p[i:i + len(v)]

            flag = match(temp, v)
            if flag:
                result += str(i) + " "

        if len(result) == 0:
            return "No Match!"
        else:
            return result.strip()


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = first_multiple_input[0]

        v = first_multiple_input[1]

        print(virusIndices(p, v))
