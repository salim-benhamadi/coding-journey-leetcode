from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest_altitude = 0
        current_altitude = 0

        for n in gain:
            current_altitude += n
            highest_altitude = max(highest_altitude, current_altitude)
            
        return highest_altitude
    

# Time complexity: O(n)
# Space complexity: O(1)