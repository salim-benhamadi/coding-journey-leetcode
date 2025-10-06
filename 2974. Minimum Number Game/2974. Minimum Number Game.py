from typing import List

# Sort and swap solution
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result = sorted(nums)
        for i in range(0, len(result) - 1, 2):
            result[i], result[i + 1] = result[i + 1], result[i]
        return result

# Time Complexity: O(n log n), where n is the length of nums (dominated by sorting)
# Space Complexity: O(n), for the sorted result array