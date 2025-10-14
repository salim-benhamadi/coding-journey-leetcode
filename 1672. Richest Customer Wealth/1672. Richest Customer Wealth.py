from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)

# Time Complexity: O(m * n), where m is number of customers and n is number of banks
# Space Complexity: O(1), generator expression doesn't create intermediate list