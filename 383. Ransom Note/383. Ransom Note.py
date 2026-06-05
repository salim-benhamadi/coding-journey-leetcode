# ── Counter Comparison ────────────────────────────────────
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        for char in ransom_counter:
            if ransom_counter[char] > magazine_counter.get(char, 0):
                return False
        
        return True

# Time Complexity:  O(n + m) — building both counters and iterating over ransomNote's unique characters
# Space Complexity: O(k) — where k is the number of unique characters across both strings (at most 26 for lowercase letters)
