# Iterative approach
class Solution:
    def addDigits(self, num: int) -> int:
        digit_sum = 0
        while num or digit_sum >= 10:
            if not num and digit_sum >= 10:
                num = digit_sum
                digit_sum = 0
            digit_sum += num % 10
            num //= 10
        return digit_sum

# Time Complexity: O(log n * log n), where n is the input number
# Space Complexity: O(1)


# Recursive approach
class Solution2:
    def addDigits(self, num: int) -> int:
        if num // 10 == 0: 
            return num
        else: 
            digit_sum = 0
            while num // 10:
                digit_sum += num % 10
                num //= 10
            digit_sum += num % 10
        return self.addDigits(digit_sum)

# Time Complexity: O(log n * log n), where n is the input number
# Space Complexity: O(log n) due to recursive call stack