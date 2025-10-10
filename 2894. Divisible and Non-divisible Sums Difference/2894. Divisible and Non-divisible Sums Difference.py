# Single pass solution
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        difference = 0
        for i in range(1, n + 1):
            if i % m == 0:
                difference -= i
            else:
                difference += i
        
        return difference

# Time Complexity: O(n), where n is the upper limit
# Space Complexity: O(1), only using constant extra space

