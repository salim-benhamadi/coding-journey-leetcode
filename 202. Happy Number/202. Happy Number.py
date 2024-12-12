class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        while True:
            n = sum([int(c)**2 for c in str(n)])
            if n == 1: return True
            if n in visited: return False
            visited.add(n)

# Time complexity: O(log n)
# Space complexity: O(log n)