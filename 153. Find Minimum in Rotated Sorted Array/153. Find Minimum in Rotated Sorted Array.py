from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            middle = (start + end) // 2
            if nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle
        return nums[start]

# Time Complexity: O(log n)
# Space Complexity: O(1)