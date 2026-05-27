# ── Sliding Window ────────────────────────────────────────
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
        return count

# Time Complexity:  O(n) — each element is visited at most twice (once by right, once by left)
# Space Complexity: O(1) — only a few integer variables used
