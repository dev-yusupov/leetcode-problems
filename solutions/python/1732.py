from typing import List

class Solution1:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        summ = 0

        for i in range(len(gain)):
            summ += gain[i]
            ans = max(summ, ans)

        return ans
    

class Solution2:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0]
        summ = 0

        for i in range(len(gain)):
            summ += gain[i]
            ans.append(summ)

        return max(ans)