class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequence_index = 0
        len_t, len_s = len(t), len(s)
        
        for main_index in range(len_t):
            if subsequence_index == len_s:
                return True
            if t[main_index] == s[subsequence_index]:
                subsequence_index += 1
        
        return subsequence_index == len_s

# Time complexity: O(n)
# Space complexity: O(1) 