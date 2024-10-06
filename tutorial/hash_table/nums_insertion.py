"""

Write a function that takes two lists of integers, nums1 and nums2, and returns a list of their intersection. 
Each element in the result should appear as many times as it does in both arrays. 
You can assume the elements are not sorted, and each list can contain duplicate values.

"""
import unittest
from typing import List, Dict

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    count_map: Dict[int, int] = {}

    for num in nums1:
        count_map[num] = count_map.get(num, 0) + 1

    intersection_list = []

    for num in nums2:
        if num in count_map and count_map[num] > 0:
            intersection_list.append(num)
            count_map[num] -= 1

            if count_map[num] == 0:
                del count_map[num]


    return intersection_list 


class TestIntersection(unittest.TestCase):
    def test_basic_intersection(self):
        self.assertEqual(intersection([4, 9, 5, 4], [9, 4, 9, 8, 4]), [9, 4, 4])

    def test_on_common_elements(self):
        self.assertEqual(intersection([1, 2, 3], [4, 5, 6]), [])

    def test_all_elements_in_common(self):
        self.assertEqual(intersection([1, 1, 2, 2], [2, 2, 1, 1]), [2, 2, 1, 1])

    def test_one_empty_list(self):
        self.assertEqual(intersection([], [1, 2, 3]), [])

    def test_both_empty(self):
        self.assertEqual(intersection([], []), [])

    def test_one_list_with_more_occurrences(self):
        self.assertEqual(intersection([1, 2, 2, 3], [2, 2, 2, 3]), [2, 2, 3])

    def test_single_element_matching(self):
        self.assertEqual(intersection([5], [5]), [5])

    def test_single_element_non_matching(self):
        self.assertEqual(intersection([5], [6]), [])


if __name__ == "__main__":
    unittest.main()