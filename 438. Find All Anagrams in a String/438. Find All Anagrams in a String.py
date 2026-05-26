# ── Sliding Window with Counter ───────────────────────────
from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        indices = []
        ns, np = len(s), len(p)
        counter_p = Counter(p)
        while left <= ns - np:
            if s[left] in p:
                if Counter(s[left:left+np]) == counter_p:
                    indices.append(left)
            left += 1
        return indices

# Time Complexity:  O(n * m) — outer loop runs O(n) times, and each Counter creation takes O(m) where m = len(p)
# Space Complexity: O(m) — two Counters each store up to m characters
