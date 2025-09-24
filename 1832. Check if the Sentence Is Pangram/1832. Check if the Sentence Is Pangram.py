# Set solution
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

# Time Complexity: O(n), where n is the length of the sentence
# Space Complexity: O(1), at most 26 letters can be stored in the set