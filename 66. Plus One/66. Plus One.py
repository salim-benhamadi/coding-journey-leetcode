from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i, carry = -1,1
        while carry != 0:
            tmp = digits[i]
            digits[i] = (tmp + carry )%10
            carry = (tmp + carry)//10
            if  len(digits) + i == 0 and carry != 0:
                digits.insert(0, carry)
                carry = 0
            i -= 1
        return digits

# Time complexity: O(n)
# Space complexity: O(1)