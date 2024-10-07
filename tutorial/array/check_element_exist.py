"""

Write a function that checks if a specific element exists in an array of integers. 
The function should return True if the element is found and False otherwise.

"""

"""

Big O notation: O(n)

as n is number of elements of array

"""

from typing import List

def elementExist(arr: List[int], elem: int) -> bool:
    for element in arr:
        if element == elem:
            return True
        
    return False