# Iteration solution
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        return total

# Time Complexity: O(n), where n is the upper limit
# Space Complexity: O(1), only using constant extra space


# Mathematical formula solution (Inclusion-Exclusion Principle)
class Solution2:
    def sumOfMultiples(self, n: int) -> int:
        def sum_divisible_by(divisor):
            count = n // divisor
            return divisor * count * (count + 1) // 2
        
        # Apply Inclusion-Exclusion Principle
        result = (sum_divisible_by(3) + sum_divisible_by(5) + sum_divisible_by(7) 
                  - sum_divisible_by(15) - sum_divisible_by(21) - sum_divisible_by(35) 
                  + sum_divisible_by(105))
        return result

# Time Complexity: O(1), constant time calculation
# Space Complexity: O(1), only using constant extra space