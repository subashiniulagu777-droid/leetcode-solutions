class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. Constants for 32-bit signed integer limits
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        # 2. Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # 3. Check for sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1
            
        # 4. Read digits and build the number
        res = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            res = res * 10 + digit
            index += 1
            
        # 5. Apply sign and handle overflow
        res *= sign
        
        if res > MAX_INT:
            return MAX_INT
        if res < MIN_INT:
            return MIN_INT
            
        return res
