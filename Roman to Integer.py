class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Correct mapping: D is 500, L is 50
        roman_map = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50,
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If the current symbol's value is smaller than the next symbol's value,
            # we subtract the current value (Subtractive Rule).
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, we add it to the total.
                total += roman_map[s[i]]
                
        return total
