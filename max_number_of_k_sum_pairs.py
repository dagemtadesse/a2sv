
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        compliment = {}
        pairCount = 0
        for num in nums:
            if num in compliment and compliment[num] > 0:
                pairCount += 1
                compliment[num] -= 1
            else:
                if not (k - num) in compliment:
                    compliment[k - num] = 1
                else: compliment[k - num] += 1
        return pairCount

print(Solution().maxOperations([3,1,3,4,3], 6))