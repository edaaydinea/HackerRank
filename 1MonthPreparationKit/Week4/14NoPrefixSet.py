#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            # If current node is end of another word, then 'word' is a prefix of that word
            if current.is_end_of_word:
                return False
        # If any child of the last node exists, then another word is a prefix of 'word'
        if current.children:
            return False
        current.is_end_of_word = True
        return True

def noPrefix(words):
    trie = Trie()
    for word in words:
        if not trie.insert(word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")



if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
