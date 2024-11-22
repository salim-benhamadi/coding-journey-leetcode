from typing import List
class Solution:
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
            # Method 1 : Brute Force
            # Time complexity: O(n^2)
            # Space complexity: O(1)
            output = []
            for i in range(len(temperatures)):
                j, tmp = 1,0
                while i+j<len(temperatures):
                    if temperatures[i+j]>temperatures[i]:
                        tmp = j
                        break
                    j +=1
                output.append(tmp)
            
            # Method 2 : Monotonic Stack
            # Source  : https://www.youtube.com/watch?v=cTBiBSnjO3c
            output = [0] * len(temperatures)
            stack = []  # pair: [temp, index]

            for i, t in enumerate(temperatures):
                while stack and t > stack[-1][0]:
                    stackT, stackInd = stack.pop()
                    output[stackInd] = i - stackInd
                stack.append((t, i))
            
            # Time complexity: O(n)
            # Space complexity: O(n)
            return output
                
                