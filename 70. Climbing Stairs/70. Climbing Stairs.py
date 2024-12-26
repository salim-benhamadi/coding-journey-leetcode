class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursive Solution (Time Limit Exceeded)
        if n == 0: return 1
        if n < 0: return 0
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # Time complexity: O(2n)
        # Space complexity: O(n)

        # Dynamic Programming Solution
        memory = [0]*(n+1)
        for i in range(n+1):
            if i == 0 or i - 1 == 0: 
                memory[i] = 1
            else:
                memory[i] = memory[i-1] + memory[i-2]
        return memory[n]

        # Time complexity: O(n)
        # Space complexity: O(n)