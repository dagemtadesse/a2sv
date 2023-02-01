class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        finder = {}
        result = []

        for n in nums1:
            finder[n] = -1
        
        for index, value in enumerate(nums2):
            if(value in finder):
                finder[value] = index
        
        for item, bound in finder.items():
            next = -1
            for other in nums2[bound:]:
                if other > item:
                    next = other
                    break
            result.append(next)
        
        return result