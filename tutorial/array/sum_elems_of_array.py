"""

Write a function that takes an array of integers as input and returns the sum of all the elements in the array.

"""


"""

Big O notation: O(n)

where n is the number of elements in an array

"""

from typing import List

def sum_elements(arr: List[int]) -> int:
    result = 0

    for number in arr:
        result += number

    return result

