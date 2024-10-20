"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_char = min(len(word1), len(word2))
        merged = []

        for i in range(min_char):
            merged.append(word1[i])
            merged.append(word2[i])

        merged.append(word1[min_char:] + word2[min_char:])

        return "".join(merged)