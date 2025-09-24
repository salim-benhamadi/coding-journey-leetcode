# ASCII manipulation solution
class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for char in s:
            if ord("A") <= ord(char) <= ord("Z"):
                result += chr(ord(char) + 32)
            else:
                result += char
        return result

# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(n), for the output string