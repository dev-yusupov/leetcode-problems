from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_bool: List[bool] = []

        for candy in candies:
            candies_bool.append(bool(max(candies) <= candy + extraCandies))

        return candies_bool