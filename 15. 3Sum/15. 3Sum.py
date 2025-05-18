from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        
        for i in range(len(sorted_nums) - 2):
            # Skip duplicates for the first position
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
                
            j, k = i + 1, len(sorted_nums) - 1
            
            while j < k:
                current_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                
                if current_sum < 0:
                    j += 1
                elif current_sum > 0:
                    k -= 1
                else: 
                    result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    
                    # Move left pointer to skip duplicates
                    j += 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                
        return result
    
# Time Complexity : O(n²), where n is the length of the input array
# Space Complexity : O(1), If we don't count the output array