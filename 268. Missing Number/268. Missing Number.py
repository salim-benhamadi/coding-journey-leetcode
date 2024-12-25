from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # 1. XOR Solution
        result = len(nums)
        for i in range(len(nums)):
            result ^= i ^ nums[i]
        return result
        # Time complexity: O(n)
        # Space complexity: O(1)

        # 2. Mathematical Formula Solution
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
        # Time complexity: O(n)
        # Space complexity: O(1)
        
