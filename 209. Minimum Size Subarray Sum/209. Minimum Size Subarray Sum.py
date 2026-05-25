# ── Sliding Window ────────────────────────────────────────
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink from the left as long as the window is valid
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

# Time Complexity:  O(n) — each element is added and removed at most once
# Space Complexity: O(1) — only a few integer variables used
