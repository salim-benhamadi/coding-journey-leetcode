# ── Sorted String Key ─────────────────────────────────────
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = dict()
        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key not in anagram_groups:
                anagram_groups[sorted_key] = [word]
            else:
                anagram_groups[sorted_key].append(word)
        return list(anagram_groups.values())

# Time Complexity:  O(n * k log k) — n is number of strings, k is max string length; sorting each string takes O(k log k)
# Space Complexity: O(n * k) — dictionary stores all strings grouped by sorted key
