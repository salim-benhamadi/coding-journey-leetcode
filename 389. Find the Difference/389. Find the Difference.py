# ── Counter Comparison ────────────────────────────────────
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)

        for character in counter_t:
            if counter_t[character] != counter_s.get(character, 0):
                return character

# Time Complexity:  O(n + m) — building two counters and iterating over one of them, where n = len(s), m = len(t)
# Space Complexity: O(n + m) — storing two counters with up to 26 keys each, but in worst case O(n + m) for the counts
