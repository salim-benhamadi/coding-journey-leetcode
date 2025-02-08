class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        
        output = 0
        i = 0
        
        while i < len(s) - 1:
            curr_val = roman[s[i]]
            next_val = roman[s[i+1]]
            
            # Check if subtraction case (when current value makes either 
            # 1/5 or 1/10 of next value)
            if curr_val * 5 == next_val or curr_val * 10 == next_val:
                output += next_val - curr_val
                i += 2
            else:
                output += curr_val
                i += 1
                
        # Add last character if not already processed
        if i == len(s) - 1:
            output += roman[s[i]]
            
        return output

# Time complexity: O(n)
# Space complexity: O(1)