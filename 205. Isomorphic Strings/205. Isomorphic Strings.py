# ── Hash Map with Value Check ─────────────────────────────
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        for i in range(len(t)):
            if t[i] in mapping and mapping[t[i]] != s[i]:
                return False
            if t[i] not in mapping:
                if s[i] in mapping.values():
                    return False
                mapping[t[i]] = s[i]
        return True

# Time Complexity:  O(n) — single pass through the strings, but checking values each iteration adds O(n) per step in worst case, making it O(n^2) due to the 'in mapping.values()' call
# Space Complexity: O(k) — where k is the number of distinct characters in t (at most n)
