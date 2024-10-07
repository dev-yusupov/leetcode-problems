"""

Using a queue, generate binary representations of numbers from 1 to N. 
Implement a function that takes N as input and returns the binary numbers from 1 to N as strings.

"""
from typing import List
import unittest

def int_to_binary(num: int) -> str:
    binary_string: str = ""

    while num > 0:
        remainder = num % 2
        binary_string = str(remainder) + binary_string
        num //= 2

    return binary_string

def generate_binary_list(number: int) -> List[str]:
    binary_list: List[str] = []

    for num in range(1, number+1):
        binary_list.append(int_to_binary(num))

    return binary_list


class BinaryListTest(unittest.TestCase):
    def test_int_to_binary(self):
        self.assertEqual(int_to_binary(5), '101')
        self.assertEqual(int_to_binary(4), '100')

    def test_generate_binary_list(self):
        self.assertEqual(generate_binary_list(5), ['1', '10', '11', '100', '101'])
        self.assertNotEqual(generate_binary_list(5), ['1', '10', '11', '100'])


if __name__ == "__main__":
    unittest.main()