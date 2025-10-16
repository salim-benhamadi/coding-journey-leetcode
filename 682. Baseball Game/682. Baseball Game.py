from typing import List

# Stack solution
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            if operation == "C":
                scores.pop()
            elif operation == "+":
                scores.append(scores[-1] + scores[-2])
            elif operation == "D":
                scores.append(2 * scores[-1])
            else:
                scores.append(int(operation))
        
        return sum(scores)

# Time Complexity: O(n), where n is the number of operations
# Space Complexity: O(n), for storing the scores