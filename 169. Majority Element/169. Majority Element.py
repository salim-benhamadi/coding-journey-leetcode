# ── Hash Map with Early Exit ──────────────────────────────
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        majority_count = len(nums) // 2

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            if frequency[num] > majority_count:
                return num

# Time Complexity:  O(n) — single pass through the array, each operation is O(1) average
# Space Complexity: O(n) — hash map stores up to n distinct elements in worst case
