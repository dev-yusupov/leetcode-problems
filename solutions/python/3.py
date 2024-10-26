"""

Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3

Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in characters_set:
                characters_set.remove(s[left])
                left += 1
            
            characters_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len