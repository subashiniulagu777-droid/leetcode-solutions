class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes (e.g., -121 reversed is 121-)
        # Also, if the last digit is 0, the first digit must be 0 (only 0 itself works)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_number = 0
        while x > reverted_number:
            # Pop the last digit and push it onto the reverted number
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
            
        # For even digits, x == reverted_number (e.g., 1221 -> x=12, reverted=12)
        # For odd digits, x == reverted_number // 10 (e.g., 121 -> x=1, reverted=12)
        return x == reverted_number or x == reverted_number // 10
