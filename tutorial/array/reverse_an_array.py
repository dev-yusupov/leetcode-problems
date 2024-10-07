"""

Write a function that takes an array of integers as input and returns a new array that contains the same elements but in reverse order.

"""

"""

Big O notation: O(n) + O(2)

"""

from typing import List
from collections import deque

def reverse_arr(arr: List[int]) -> List[int]:
    reversed_arr = deque()

    arr = deque(arr)

    for i in arr:
        reversed_arr.appendleft(arr[i]) # O(1)

    return list(reversed_arr)