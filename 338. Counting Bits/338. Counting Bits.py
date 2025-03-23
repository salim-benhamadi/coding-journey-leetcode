from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_counts = []
        for num in range(0, n+1):
            current = num
            ones_count = current % 2
            while current != 0 and current != 1:
                current //= 2
                ones_count += current % 2
            bit_counts.append(ones_count)
        return bit_counts

# Time complexity: O(n log n)
# Space complexity: O(1) 