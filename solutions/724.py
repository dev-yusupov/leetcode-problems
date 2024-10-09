from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0

        summ = sum(nums)

        for i in range(len(nums)):
            if (summ - sumLeft - nums[i]) == (sumLeft):
                return i
            else:
                sumLeft += nums[i]

        return -1