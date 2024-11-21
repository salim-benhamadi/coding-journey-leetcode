class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapOpenToClose = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in mapOpenToClose:
                stack.append(c)
            else:
                if not stack or mapOpenToClose.get(stack[-1]) != c:
                    return False
                stack.pop()
                
        return len(stack) == 0

# Time complexity: O(n)
# Space complexity: O(n)