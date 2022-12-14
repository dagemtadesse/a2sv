from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        min, max, avg = 0, len(piles) - 1, len(piles) - 2
        total = 0
        while min < max:
            total += piles[avg]
            min += 1
            max -= 2
            avg -= 2
        return total

print(Solution().maxCoins([9,8,7,6,5,1,2,3,4]))