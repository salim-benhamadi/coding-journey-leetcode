# Method 1 : List-based Approach
class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        result = []
        
        for char in s:
            if char != " ":
                word.append(char)
            elif word:
                result.insert(0, "".join(word))
                word = []
                
        if word:
            result.insert(0, "".join(word))
            
        return " ".join(result)

# Time Complexity : O(n)
# Space Complexity : O(n)


# Method 2 : Python Built-ins
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

# Time Complexity : O(n)
# Space Complexity : O(n)