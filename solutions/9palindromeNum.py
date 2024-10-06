"""

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x

        reversed_num = 0

        while x > 0:
            reversed_num = reversed_num * 10 + (x % 10)

            x = x // 10

        return bool(original == reversed_num)