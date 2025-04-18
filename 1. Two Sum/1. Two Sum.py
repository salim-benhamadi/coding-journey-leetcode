from typing import List

# Solution 1: Hash Map Approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        
        return []

# Time Complexity : O(n), where n is the length of the input array
# Space Complexity : O(n)


# Solution 2: Brute Force Approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

# Time Complexity : O(n²), where n is the length of the input array
# Space Complexity : O(1)