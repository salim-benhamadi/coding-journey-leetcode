from typing import List

# Product multiplication solution
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            if num == 0: 
                return 0
            product *= num
        return product // abs(product)

# Time Complexity: O(n), where n is the length of the array
# Space Complexity: O(1), only using constant extra space


# Count negatives solution
class Solution2:
    def arraySign(self, nums: List[int]) -> int:
        negative_count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                negative_count += 1
        return -1 if negative_count % 2 == 1 else 1

# Time Complexity: O(n), where n is the length of the array
# Space Complexity: O(1), only using constant extra space