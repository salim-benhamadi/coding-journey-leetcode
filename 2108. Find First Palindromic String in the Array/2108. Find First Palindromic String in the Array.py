from typing import List

# String reversal solution
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

# Time Complexity: O(n * m), where n is number of words and m is average word length
# Space Complexity: O(m), for the reversed string created by slicing
