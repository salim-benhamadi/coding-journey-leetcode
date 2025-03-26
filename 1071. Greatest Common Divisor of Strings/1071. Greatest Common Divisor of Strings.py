
# First Solution 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        largest_divisor = ""
        len_1, len_2 = len(str1), len(str2)
        min_len = min(len_1, len_2)
        
        for i in range(min_len):
            if str1[i] == str2[i]:
                candidate = str1[:i+1]
                if (candidate * (len_1 // (i+1)) == str1 and 
                    candidate * (len_2 // (i+1)) == str2 and
                    len_1 % (i+1) == 0 and 
                    len_2 % (i+1) == 0):
                    largest_divisor = candidate
            else: 
                break
                
        return largest_divisor

# Time Complexity : O(min(m, n) * (m + n)), where m and n are the lengths of str1 and str2
# Space Complexity : O(min(m, n))


# Alternative Solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If str1 + str2 != str2 + str1, they can't have a common divisor
        if str1 + str2 != str2 + str1:
            return ""
            
        # Find the GCD of the lengths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
    
# Time Complexity : O(m + n + log(min(m, n))), where m and n are the lengths of str1 and str2
# Space Complexity : O(m + n)