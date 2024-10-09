"""

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. 
Use two pointers to compare characters from the beginning and the end of the string.

O annotation: O(n)

"""

def validPalindrome(word: str) -> bool:
    start = 0
    end = len(word) - 1

    while start < end:
        if word[start] != word[end]:
            return False
        
        start += 1
        end -= 1

    return True


print(validPalindrome("cat"))
print(validPalindrome("kayak"))