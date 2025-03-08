from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = dict()
        for n in arr:
            if n in occurrences:
                occurrences[n] += 1
            else:
                occurrences[n] = 1
        
        values = occurrences.values()
        return len(set(values)) == len(values)
    
# Time Complexity : O(n), where n is the length of the input array
# Space Complexity**: O(k) We store a dictionary with k entries where k is the number of unique elements