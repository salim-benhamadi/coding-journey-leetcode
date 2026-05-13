# ── Dutch National Flag ───────────────────────────────────
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, start, end = 0, 0, len(nums) - 1
        while i <= end:
            if nums[i] == 0 and start != i:
                if nums[start] != 0:
                    nums[start], nums[i] = nums[i], nums[start]
                    i += 1
                start += 1
            elif nums[i] == 2 and end != i:
                if nums[end] != 2:
                    nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1

# Time Complexity:  O(n) — single pass through the array with pointer adjustments
# Space Complexity: O(1) — only a few integer variables used
