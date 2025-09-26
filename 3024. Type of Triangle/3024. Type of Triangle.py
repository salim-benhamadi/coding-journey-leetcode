from typing import List

#  Set-based solution
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        unique_sides = len(set(nums))
        a, b, c = nums
        
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return "none"
        
        if unique_sides == 1: 
            return "equilateral"
        elif unique_sides == 2: 
            return "isosceles"
        else: 
            return "scalene"

# Time Complexity: O(1), constant time operations on fixed-size array
# Space Complexity: O(1), constant space for set operations on 3 elements