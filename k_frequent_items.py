from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        uniques = []

        for item in nums:
            if item in counter:
                counter[item] += 1
            else: 
                counter[item] = 1

        for key, freq in counter.items():
            if len(uniques) >= k:
                # minKey = None
                minKeyIndex = None
                # print(uniques)
                for index, keys in enumerate(uniques):
                    if minKeyIndex is None or counter[keys] < counter[uniques[minKeyIndex]]:
                        minKeyIndex = index
                # print(minKeyIndex)
                if counter[uniques[minKeyIndex]] < freq: uniques.pop(minKeyIndex)
                # print(uniques, freq, )
            if (len(uniques) < k):
                uniques.append(key)
            
        return uniques

print(Solution().topKFrequent([1,1,1,2,2,3], 2))

