# Hash map solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_frequency = {}
        n = len(s)
        for i in range(n):
            if s[i] in char_frequency:
                char_frequency[s[i]] = -1
            else:
                char_frequency[s[i]] = i
        
        for char in char_frequency:
            if char_frequency[char] != -1:
                return char_frequency[char] 
        return -1

# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(1), at most 26 lowercase letters can be stored