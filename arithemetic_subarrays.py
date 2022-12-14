from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(0, len(l)):
            arithmetic = True
            subarray = nums[l[i]: r[i] + 1]
            subarray.sort()
            delta = subarray[1] - subarray[0]
            # print(subarray)
            for j in range(0, len(subarray) - 1):
                if (subarray[j + 1] - subarray[j]) != delta:
                    arithmetic = False
            # print('---')
            result.append(arithmetic)
        return result

print(Solution().checkArithmeticSubarrays([4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))