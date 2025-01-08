from types import List

# 1. Brute Force Solution (Time Limit Exceeded)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for left in range(len(height)):
            for right in range(len(height)):
                current_area = (right - left) * min(height[left], height[right])
                max_area = max(max_area, current_area)
        return max_area

# Time complexity: O(n²)
# Space complexity: O(1)


# 2. Two Pointer Solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

# Time complexity: O(n)
# Space complexity: O(1)