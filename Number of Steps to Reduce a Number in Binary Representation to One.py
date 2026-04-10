class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0
        
        # Traverse the string from right to left, excluding the first character
        for i in range(len(s) - 1, 0, -1):
            # If (current bit + carry) is 1, the number is odd
            if int(s[i]) + carry == 1:
                steps += 2  # Step 1: Add 1 (becomes even), Step 2: Divide by 2
                carry = 1   # Adding 1 to an odd binary digit always carries
            else:
                steps += 1  # Even: Just divide by 2
                
        # If there's a carry at the end, the first '1' became '10', requiring one final division
        return steps + carry
