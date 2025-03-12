class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = dict()
        palindrome_length = 0
        has_odd_count = 0
        
        # Count frequency of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Calculate palindrome length
        for count in char_count.values():
            remainder = count % 2
            palindrome_length += count - remainder
            has_odd_count = max(has_odd_count, remainder)
        
        return palindrome_length + has_odd_count

# Time Complexity : O(n), where n is the length of the input string
# Space Complexity : O(k), where k is the number of unique characters