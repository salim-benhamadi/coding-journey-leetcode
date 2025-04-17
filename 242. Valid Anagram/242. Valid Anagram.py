class Solution:
    def isAnagram(self, first_str: str, second_str: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(first_str) != len(second_str):
            return False

        freq_first, freq_second = {}, {}
    
        for i in range(len(first_str)):
            freq_first[first_str[i]] = freq_first.get(first_str[i], 0) + 1
            freq_second[second_str[i]] = freq_second.get(second_str[i], 0) + 1
            
        return freq_first == freq_second

# Time Complexity : O(n), where n is the length of the input strings
# Space Complexity : O(k), where k is the size of the character set