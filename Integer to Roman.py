class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # List of Roman numeral symbols and their corresponding values
        # These are ordered from largest to smallest
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        res = []
        
        # Iterate through the map
        for value, symbol in roman_map:
            # If the number is 0, we are done
            if num == 0:
                break
                
            # Determine how many times this symbol fits into the current number
            count, num = divmod(num, value)
            
            # Append the symbol that many times to our result list
            res.append(symbol * count)
            
        # Join all parts into the final string
        return "".join(res)
