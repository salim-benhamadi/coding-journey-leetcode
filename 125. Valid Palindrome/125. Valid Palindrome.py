class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1:
        cleaned = [i.lower() for i in s if i.isalnum()]
        return cleaned == cleaned[::-1]
        # Time complexity: O(n)
        # Space complexity: O(n)

        # Method 2:
        lower = 0
        upper = len(s) -1
        while lower >= upper:
            if not s[lower].isalnum():
                lower+= 1
                continue
            if not s[upper].isalnum():
                upper-= 1
                continue
            if s[lower].lower() != s[upper].lower():
                return False
            lower, upper = lower + 1, upper -1 
        return True
    
        # Time complexity: O(n)
        # Space complexity: O(1)