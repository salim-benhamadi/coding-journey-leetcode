from typing import List

# List comprehension with max solution
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(sentence.split(" ")) for sentence in sentences])

# Time Complexity: O(n * m), where n is number of sentences and m is average sentence length
# Space Complexity: O(n), for the list of word counts