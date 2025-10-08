from typing import List

# Counter solution
class Solution2:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_count = 0

        for num in arr:
            if num % 2 == 1:
                consecutive_count += 1
                if consecutive_count == 3:
                    return True
            else:
                consecutive_count = 0

        return False

# Time Complexity: O(n), where n is the length of the array
# Space Complexity: O(1), only using constant extra space