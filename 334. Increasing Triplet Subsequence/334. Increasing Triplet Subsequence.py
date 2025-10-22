from typing import List

# Two variable tracking solution
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = second_min = float('inf')
        
        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True
        
        return False

# Time Complexity: O(n), where n is the length of the array
# Space Complexity: O(1), only using constant extra space