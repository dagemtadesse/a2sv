from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        total = 0
        for i in range(1, len(piles), 3):
            total += piles[i]
        return total

print(Solution().maxCoins([9,8,7,6,5,1,2,3,4]))