# ── Two Pointers ──────────────────────────────────────────
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Time Complexity:  O(n) — each element is swapped once, requiring n/2 iterations
# Space Complexity: O(1) — only two integer variables are used
