"""

Find the Original Typed String I

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

"""

class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1  # Start with the original string as 1 valid possibility
        n = len(word)
        
        i = 0
        while i < n:
            j = i + 1
    
            # Find the end of the consecutive duplicate sequence
            while j < n and word[j] == word[i]:
                j += 1
            
            # The length of this group of duplicates is j - i
            length_of_group = j - i
    
            # If the group is larger than 1, we can remove 1 to length_of_group - 1 duplicates
            if length_of_group > 1:
                total += (length_of_group - 1)  # Add all possible removals
    
            # Move to the next group of characters
            i = j
    
        return total
