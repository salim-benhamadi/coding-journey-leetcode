from typing import List

# Stream simulation solution
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        target_index = 0
        
        for stream_number in range(1, n + 1):
            operations.append("Push")
            
            if stream_number == target[target_index]:
                target_index += 1
            else:
                operations.append("Pop")
            
            if target_index >= len(target):
                return operations
        
        return operations

# Time Complexity: O(max(target)), where max(target) is the largest element in target
# Space Complexity: O(max(target)), for storing the operations list