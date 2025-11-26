from typing import List

# Sorting with hash map solution
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index_map = {}
        sorted_nums = sorted(nums)
        
        for i, num in enumerate(sorted_nums):
            if num not in index_map:
                index_map[num] = i
        
        result = [index_map[num] for num in nums]
        return result

# Time Complexity: O(n log n), where n is the length of the array (dominated by sorting)
# Space Complexity: O(n), for the hash map and sorted array


# Brute force solution
class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    result[i] += 1
        return result

# Time Complexity: O(n²), where n is the length of the array
# Space Complexity: O(n), for the result array