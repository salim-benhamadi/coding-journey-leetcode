from typing import List

# Stack with time tracking solution
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        counter = [0] * n
        stack = []
        prev = 0

        for log in logs:
            id, operation, time = log.split(":")
            id, time = int(id), int(time)

            if operation == "start":
                if stack:
                    counter[stack[-1]] += time - prev
                stack.append(id)
                prev = time
                 
            else:  # operation == "end"
                counter[stack[-1]] += time - prev + 1
                stack.pop()
                prev = time + 1
        
        return counter

# Time Complexity: O(m), where m is the number of logs
# Space Complexity: O(n), where n is the number of functions (for call stack and result array)