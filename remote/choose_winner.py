class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def calcScore( left, right):
            
            if (left, right) in memo:
                return memo[(left, right)]

            if right - left == 0:
                return nums[left]

            if right - left <= 0:
                return 0
            
            # print(nums)

            first = min(
#  nums = num[1:]
                nums[left] + calcScore(left + 2, right),
                nums[left] + calcScore( left + 1, right - 1),
            )

            second = min(
                # nums[:-1]
                nums[right] + calcScore( left + 1, right - 1),
                nums[right] + calcScore( left, right - 2),
            )

            sol =  max(first, second)
            memo[(left, right)] = sol
            return sol
        
        total = sum(nums)
        ans = calcScore(0, len(nums) - 1)
        return ans >= (total - ans)
