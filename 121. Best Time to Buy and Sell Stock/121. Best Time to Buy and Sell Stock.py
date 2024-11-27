from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Method 1: Brute Force
        max_profit = 0
        for i in range(len(prices)-1):
            tmp = max(prices[i+1:]) - prices[i]
            if tmp > max_profit:
                max_profit = tmp
        return max_profit

        # Time Complexity : O(n²)
        # Space Complexity : O(1)

        # Method 2: Sliding Window
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
        
        return max_profit
        
        # Time Complexity : O(n)
        # Space Complexity : O(1)
            

        