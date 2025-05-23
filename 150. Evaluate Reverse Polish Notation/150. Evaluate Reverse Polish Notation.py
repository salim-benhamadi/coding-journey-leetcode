from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.lstrip("-").isdigit():
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                if t == "+":
                    stack.append(x + y)
                elif t == "-":
                    stack.append(x - y)
                elif t == "*":
                    stack.append(x * y)
                else:  # t == "/"
                    stack.append(int(x / y))
                    
        return stack[-1]
    

# Time Complexity : O(n), where n is the length of the tokens array
# Space Complexity : O(n)