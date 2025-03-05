# Solution 1 (Dynamic Programming Approach)

class Solution:
    def tribonacci(self, n: int) -> int:
        sequence = []
        
        for i in range(n + 1):
            if i == 0:
                sequence.append(0)
            elif i == 1 or i == 2:
                sequence.append(1)
            else:
                sequence.append(sum(sequence[i-3:i]))
                
        return sequence[-1]
    
# Time complexity: O(n)
# Space complexity: O(n)    

# Solution 2 (Recursive Approach with Memoization)

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}
        
        def recursive_trib(n):
            if n in memo:
                return memo[n]
            
            memo[n] = recursive_trib(n-1) + recursive_trib(n-2) + recursive_trib(n-3)
            return memo[n]
        
        return recursive_trib(n)
    
# Time complexity: O(n)
# Space complexity: O(n)