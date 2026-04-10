class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count flips needed to match the pattern "0101..."
        flips_to_01 = 0
        for i in range(len(s)):
            # If index is even, we expect '0'. If odd, we expect '1'.
            expected = '0' if i % 2 == 0 else '1'
            if s[i] != expected:
                flips_to_01 += 1
        
        # The flips for "1010..." is simply (total length - flips_to_01)
        # We return the minimum of the two possible patterns
        return min(flips_to_01, len(s) - flips_to_01)
