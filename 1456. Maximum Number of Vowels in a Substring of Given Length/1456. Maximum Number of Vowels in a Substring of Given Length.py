# ── Sliding Window with Vowel Map ─────────────────────────
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_map = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        outgoing_vowel = 0
        current_count = 0
        max_count = 0

        for i in range(len(s)):
            current_count -= outgoing_vowel
            current_count += vowel_map.get(s[i], 0)
            max_count = max(max_count, current_count)
            if i >= k - 1:
                outgoing_vowel = vowel_map.get(s[i - k + 1], 0)
        return max_count

# Time Complexity:  O(n) — single pass through the string of length n
# Space Complexity: O(1) — vowel_map has constant size, only a few integer variables
