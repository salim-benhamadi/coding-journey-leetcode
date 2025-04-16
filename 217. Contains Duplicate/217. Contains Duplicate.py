from typing import List

# Solution 1: Using Set Length Comparison
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Compare the length of the set (which removes duplicates) with the original array
        return len(set(nums)) != len(nums)

# Time Complexity : O(n), where n is the length of the input array
# Space Complexity : O(n)

# Solution 2: Using HashSet  
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Time Complexity : O(n), where n is the length of the input array
# Space Complexity : O(n)