from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        running_product = 1
        result = []
        
        # Calculate left products
        for i in range(array_length):
            result.append(running_product)
            running_product *= nums[i]
            
        # Calculate right products and combine
        running_product = 1
        for i in range(array_length - 1, -1, -1):
            result[i] *= running_product
            running_product *= nums[i]
            
        return result
    

# Time complexity: O(n)
# Space complexity: O(n) 