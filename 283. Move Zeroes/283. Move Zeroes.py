from typing import List

# First Approach : Brute Force 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, i, j = len(nums), 0, 0

        while j < n:
            if nums[i] == 0: 
                nums.pop(i)
                nums.append(0)
            else: 
                i += 1
            j += 1

# Time complexity: O(n²)
# Space complexity: O(1) 

# Second Approach : Two-Pointers 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0  # position to place the next non-zero element
        
        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

# Time complexity: O(n)
# Space complexity: O(1) 