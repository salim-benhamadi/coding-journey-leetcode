import math
from typing import List

class Solution:
    def calculate_time(self, eating_speed: int, h: int, piles: List[int]):
        total_hours = 0
        for pile_size in piles:
            total_hours += math.ceil(float(pile_size) / eating_speed)
        return total_hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        result = max_speed
        
        while min_speed <= max_speed:
            mid_speed = (max_speed + min_speed) // 2
            time_needed = self.calculate_time(mid_speed, h, piles)
            
            if time_needed <= h:
                result = mid_speed
                max_speed = mid_speed - 1
            else:
                min_speed = mid_speed + 1
                
        return result

# Time Complexity: O(n * log(m)), where n is the number of piles and m is the maximum pile size.
# Space Complexity: O(1), as we are using a constant amount of space.