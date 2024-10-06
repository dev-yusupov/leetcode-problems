"""

Write a function that takes a list of integers and returns True 
if there are any duplicates in the list, and False otherwise. 
Use a hash table (dictionary) to solve this in an efficient way.

"""

from typing import List


def num_freq(nums: List[int]) -> bool:
    hashed_map = {}

    for num in nums:
        if num in hashed_map:
            return True
        
        hashed_map[num] = 1

    return False


print(num_freq([1, 2, 3, 4])) # False
print(num_freq([1, 2, 3, 1])) # True