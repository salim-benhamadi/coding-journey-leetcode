from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        output = []
        
        for n in nums:
            count[n] = count.get(n,0) +1
        
        for i in count:
            freq[count[i]].append(i)
        
        for i in freq:
            output += i
            
        return output[-k:]

# Time Complexity : O(n), where n is the length of the input array
# Space Complexity : O(n), where n is the length of the input array