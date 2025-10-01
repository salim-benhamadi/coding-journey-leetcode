# Digit extraction solution
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        remaining = num 
        while remaining > 0:
            digit = remaining % 10
            if num % digit == 0:
                count += 1
            remaining //= 10
        
        return count

# Time Complexity: O(log n), where n is the value of num (number of digits)
# Space Complexity: O(1), only using constant extra space