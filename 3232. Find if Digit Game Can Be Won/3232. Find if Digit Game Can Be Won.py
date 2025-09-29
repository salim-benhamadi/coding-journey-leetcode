from typing import List

# Sum comparison solution
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum = sum([num for num in nums if num < 10])
        double_digit_sum = sum([num for num in nums if num > 9])
        return single_digit_sum != double_digit_sum

# Time Complexity: O(n), where n is the length of the array
# Space Complexity: O(1), excluding the space for list comprehensions