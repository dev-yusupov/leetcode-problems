from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeros = []
    for num in nums:
        if num == 0:
            zeros.append(num)
            nums.pop(nums.index(num))
    
    nums = nums + zeros
    return nums


print(moveZeroes(nums=[1, 0, 5, 0, 2]))