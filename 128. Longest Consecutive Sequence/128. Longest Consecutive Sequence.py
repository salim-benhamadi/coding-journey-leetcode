from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)
        for n in numsSet:
            if n-1 not in numsSet:
                length = 0
                while n + length in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest

# Time Complexity : O(n), where n is the length of the input array
# Space Complexity : O(n)