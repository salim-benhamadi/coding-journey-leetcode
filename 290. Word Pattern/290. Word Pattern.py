# ── Bijection with Dictionary and Values Check ────────────
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = dict()
        words = s.split(" ")
        
        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in mapping and words[i] not in mapping.values():
                mapping[pattern[i]] = words[i]
            elif mapping.get(pattern[i], "") != words[i]:
                return False
        
        return True

# Time Complexity:  O(n) — single pass over pattern and words, where n is the length of pattern
# Space Complexity: O(m) — stores up to m unique mappings, where m is the number of distinct letters in pattern
