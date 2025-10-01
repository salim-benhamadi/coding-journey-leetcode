from typing import List

# List comprehension solution
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]

# Time Complexity: O(n * m), where n is the number of words and m is average word length
# Space Complexity: O(k), where k is the number of matching indices