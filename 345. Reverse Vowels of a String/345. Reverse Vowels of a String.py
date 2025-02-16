from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        sl = list(s)
        pos = []
        
        # Store positions of all vowels
        for i in range(len(s)):
            if s[i] in vowels:
                pos.append(i)
                
        # Swap vowels from start and end
        n = len(pos)
        for i in range(n//2):
            sl[pos[i]], sl[pos[n-i-1]] = sl[pos[n-i-1]], sl[pos[i]]
        
        return ''.join(sl)

# Time complexity: O(n)
# Space complexity: O(n)