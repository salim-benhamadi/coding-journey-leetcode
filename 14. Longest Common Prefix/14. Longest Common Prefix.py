from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        for s in strs:
            if output == "": 
                return ""
            idx = min(len(s), len(output))
            for i in range(idx):
                if output[i] != s[i]:
                    output = output[:i]
                    break
            output = output[:idx]
        return output

# Time complexity: O(S), S is the sum of all characters in all strings
# Space complexity: O(1)