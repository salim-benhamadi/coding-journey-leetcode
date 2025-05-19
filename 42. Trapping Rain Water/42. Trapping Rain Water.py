from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        trapped_water = 0

        while left < right:
            if height[left] <= height[right]:
                trapped_water += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                trapped_water += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
            
        return trapped_water
    
# Time Complexity : O(n), where n is the length of the height array
# Space Complexity : O(1), no extra space is used