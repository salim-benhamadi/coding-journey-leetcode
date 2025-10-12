
from typing import List

# Single pass solution
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0

        for num in nums:
            element_sum += num
            while num > 0:
                digit_sum += num % 10
                num //= 10

        return abs(element_sum - digit_sum)

# Time Complexity: O(n * d), where n is length of array and d is average number of digits
# Space Complexity: O(1), only using constant extra space