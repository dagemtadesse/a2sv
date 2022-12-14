from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        maxPairSum = 0
        while(left < right):
            maxPairSum = max(maxPairSum, nums[left] + nums[right])
            left += 1
            right -= 1
        return maxPairSum

print(Solution().minPairSum([3,5,2,3]))
