# ── Counter Intersection ──────────────────────────────────
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)
        output = []
        for key in counter_1:
            if counter_2.get(key, 0):
                output.append(key)
        return output

# Time Complexity:  O(n + m) — building two counters and iterating over one counter's keys
# Space Complexity: O(n + m) — storing two counters


# ── Set Intersection ──────────────────────────────────────
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# Time Complexity:  O(n + m) — building two sets and computing intersection
# Space Complexity: O(n + m) — storing two sets
