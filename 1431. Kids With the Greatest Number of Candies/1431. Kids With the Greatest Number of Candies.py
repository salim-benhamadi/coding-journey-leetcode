from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [i + extraCandies >= max_candies for i in candies]

# Time complexity: O(n)
# Space complexity: O(n)