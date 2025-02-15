from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        slots = 0
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed)-1):
            if (flowerbed[i - 1] == 0 and 
                flowerbed[i] == 0 and 
                flowerbed[i + 1] == 0):
                slots += 1
                flowerbed[i] = 1
                
        return slots >= n

# Time complexity: O(n)
# Space complexity: O(n)