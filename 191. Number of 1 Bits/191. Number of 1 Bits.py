class Solution:
    def hammingWeight(self, n: int) -> int:
        number_of_bits = 1
        while n // 2 != 0:
            number_of_bits += n % 2
            n //= 2
        return number_of_bits
    
    # Time complexity: O(log n)
    # Space complexity: O(1)

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n-1)
            count += 1
        return count
    
    # Time complexity: O(n)
    # Space complexity: O(1)