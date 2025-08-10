from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            current_row = matrix[mid_row]
            row_start, row_end = current_row[0], current_row[-1]
            
            if target <= row_end and target >= row_start:
                left, right = 0, len(current_row) - 1
                while left <= right:
                    mid_col = (left + right) // 2
                    if target == current_row[mid_col]:
                        return True
                    elif current_row[mid_col] < target:
                        left = mid_col + 1
                    elif current_row[mid_col] > target:
                        right = mid_col - 1
                return False
            elif row_start > target:
                bottom = mid_row - 1
            elif row_end < target:
                top = mid_row + 1
                
        return False

# Time Complexity: O(log(m * n)), where m is the number of rows and n is the number of columns.
# Space Complexity: O(1), as we are using only a constant amount of space.