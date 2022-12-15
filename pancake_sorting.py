from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ops = []

        def reverse(arr, k):
            left = 0
            right = k - 1

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        def find(arr, target):
            for index,value in enumerate(arr):
                if value == target: return index

        for i in range(len(arr), 0, -1):
            index = find(arr, i)
            # print(arr, index, i)

            if index == i - 1:
                continue
            
            if(index != 0):
                reverse(arr, index + 1)
                ops.append(index + 1)
                # print(arr)
                # print(arr)
            
            reverse(arr, i)
            ops.append(i)
            # print(arr)
    
        return ops




            




        

  
print(Solution().pancakeSort([3,2,4,1]))