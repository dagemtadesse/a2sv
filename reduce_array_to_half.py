from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}
        for item in arr:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1

        removed_count = 0
        removed = 0
        counts = list(counter.values())
        counts.sort()
        while removed < len(arr) / 2:
            removed += counts.pop()
            removed_count += 1
        return removed_count

print(Solution().minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))