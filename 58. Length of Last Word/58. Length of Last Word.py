# String split solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(n), for the split array


# Reverse iteration solution
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count last word length
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length

# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(1), only using constant extra space