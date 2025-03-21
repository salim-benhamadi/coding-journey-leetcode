from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_position = 0
        iteration_count = 0
        array_length = len(nums)

        while iteration_count < array_length - 1:
            if nums[unique_position] == nums[unique_position + 1]:
                nums.pop(unique_position + 1)
                array_length -= 1  
            else:
                unique_position += 1
            iteration_count += 1
        
        return array_length

# Time Complexity : O(n²)
# Space Complexity : O(1)