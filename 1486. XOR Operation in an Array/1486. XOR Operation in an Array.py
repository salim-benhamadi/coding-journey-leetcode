# Iterative XOR solution
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2*i
        return result

# Time Complexity: O(n), where n is the number of elements
# Space Complexity: O(1), only using constant extra space