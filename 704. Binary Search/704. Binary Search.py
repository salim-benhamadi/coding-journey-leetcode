from typing import List

def search(self, nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            start = middle + 1
        elif target < nums[middle]:
            end = middle - 1
    return -1

# Time complexity: O(log n)
# Space complexity: O(1)
