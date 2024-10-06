from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        intersection_list = []

        for num in nums2:
            if num in count and count[num] > 0:
                intersection_list.append(num)
                del count[num]

        return intersection_list