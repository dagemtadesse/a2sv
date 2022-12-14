from typing import List


class Solution:
    def merge(self, left, right):
        merged = []
        while (left and right):
            if (left[0] < right[0]):
                merged.append(left.pop(0))

            else:
                merged.append(right.pop(0))

        while (left):
            merged.append(left.pop(0))

        while (right):
            merged.append(right.pop(0))

        return merged

    def mergeSort(self, nums: List[int]):
        if (len(nums) <= 1):
            return nums

        left = self.mergeSort(nums[0:len(nums)//2])
        right = self.mergeSort(nums[len(nums)//2:])

        return self.merge(left, right)

    def maxFrequency(self, nums: List[int], k: int) -> int:

        sorted = self.mergeSort(nums)
        maxFrequency = 1
        print(sorted)

        if len(nums) == 1:
            return 1

        left = 0
        right = 1
        ops = sorted[right] - sorted[left]

        while left < len(nums) and right < len(nums):

            while ops <= k:
                maxFrequency = max(right - left + 1, maxFrequency)
                right += 1
                if(right >= len(nums)): break
                ops += (sorted[right] - sorted[right - 1]) * (right - left)
                # print(left, right, ops)

            if (ops > k):
                if right >= len(nums):
                    right = len(nums) - 1
                ops -= (sorted[right] - sorted[left])
                left += 1
                
                # print(left, right, ops)

        return maxFrequency


print(Solution().maxFrequency([9930, 9923, 9983, 9997, 9934, 9952, 9945, 9914, 9985, 9982, 9970, 9932, 9985, 9902, 9975, 9990, 9922, 9990, 9994, 9937, 9996, 9964, 9943, 9963, 9911, 9925, 9935, 9945, 9933, 9916, 9930, 9938, 10000, 9916, 9911, 9959, 9957, 9907, 9913, 9916,
      9993, 9930, 9975, 9924, 9988, 9923, 9910, 9925, 9977, 9981, 9927, 9930, 9927, 9925, 9923, 9904, 9928, 9928, 9986, 9903, 9985, 9954, 9938, 9911, 9952, 9974, 9926, 9920, 9972, 9983, 9973, 9917, 9995, 9973, 9977, 9947, 9936, 9975, 9954, 9932, 9964, 9972, 9935, 9946, 9966], 3056))
print(Solution().maxFrequency([1, 2, 4], 5))
print(Solution().maxFrequency([1,4,8,13], 5))
print(Solution().maxFrequency([3, 9, 6], 2))
#  1, 2, 3
