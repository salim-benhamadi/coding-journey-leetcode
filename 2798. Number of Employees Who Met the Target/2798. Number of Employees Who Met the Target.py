from typing import List

# Filter and lambda solution
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len(list(filter(lambda x: x >= target, hours)))

# Time Complexity: O(n), where n is the number of employees
# Space Complexity: O(n), for the filtered list


# List comprehension solution
class Solution2:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for hour in hours if hour >= target)

# Time Complexity: O(n), where n is the number of employees
# Space Complexity: O(1), using generator expression


# Simple loop solution
class Solution3:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for hour in hours:
            if hour >= target:
                count += 1
        return count

# Time Complexity: O(n), where n is the number of employees
# Space Complexity: O(1), only using constant extra space