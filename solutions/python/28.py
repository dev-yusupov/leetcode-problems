"""

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.


Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1

Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        begin, end = 0, len(needle)
        length = len(haystack)

        while end <= length:
            if haystack[begin:end] == needle:
                return begin

            else:
                begin += 1
                end += 1

        return -1