class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVolume = right * min(height[left], height[right])

        while left <= right < len(height):
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxVolume = max(maxVolume, (right - left) * min(height[left], height[right]))
        
        return maxVolume
            

            