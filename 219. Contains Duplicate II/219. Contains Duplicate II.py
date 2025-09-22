from typing import List

# Solution 1: Hash Map Approach

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
            
        index_map = {}

        for current_index, value in enumerate(nums):
            if value in index_map:
                if abs(current_index - index_map[value]) <= k:
                    return True
            index_map[value] = current_index
            
        return False


# Time Complexity : O(n), where n is the length of the nums array
# Space Complexity : O(min(n, k+1))

# Solution 2: Sliding Window Approach

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        
        for current_index in range(len(nums)):
            current_value = nums[current_index]
            window_end = min(current_index + 1 + k, len(nums))
            
            if current_value in nums[current_index + 1:window_end]:
                return True
                
        return False

# Time Complexity : O(n * k), where n is the length of the nums array
# Space Complexity : O(n)