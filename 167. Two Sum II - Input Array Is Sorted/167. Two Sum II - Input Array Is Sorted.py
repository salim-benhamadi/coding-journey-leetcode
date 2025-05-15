from typing import List

# Solution 1: Hash Map Approach

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_index = dict()
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            
            if complement in num_to_index:
                return [num_to_index[complement], i+1]
                
            num_to_index[numbers[i]] = i+1

# Time Complexity: O(n), where n is the length of the input array
# Space Complexity: O(n), where n is the length of the input array

# Solution 2: Brute Force Approach

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for first_index in range(len(numbers)):
            first_num = numbers[first_index]
            complement = target - first_num
            
            if complement in numbers[first_index+1:]:
                second_index = first_index+1
                
                while second_index < len(numbers):
                    if numbers[second_index] == complement:
                        return [first_index+1, second_index+1]
                    second_index += 1

# Time Complexity: O(n²), where n is the length of the input array
# Space Complexity: O(1), as we are not using any extra space
