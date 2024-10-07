"""

Using a queue, generate binary representations of numbers from 1 to N. 
Implement a function that takes N as input and returns the binary numbers from 1 to N as strings.

"""
from typing import List
from collections import deque

import unittest

def reverse_list1(num_list: List[int]) -> List[int]:
    reversed_list = []

    for num in num_list:
        reversed_list = [num] + reversed_list

    return reversed_list

def reverse_list2(num_list: List[int]) -> List[int]:
    queue = deque(num_list)
    reversed_list = deque()

    while queue:
        reversed_list.appendleft(queue.popleft())

    return list(reversed_list)


class TestReverse(unittest.TestCase):
    def test_reversing(self):
        self.assertEqual(reverse_list1([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_reverse_empty(self):
        self.assertEqual(reverse_list1([]), [])

    def test_reverse_list_one_element(self):
        self.assertEqual(reverse_list1([1]), [1])


if __name__ == "__main__":
    unittest.main()