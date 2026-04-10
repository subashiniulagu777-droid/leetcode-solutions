class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Double the string to simulate all possible rotations using a sliding window
        s = s + s
        
        # Create two alternating target patterns of the same length as the doubled string
        alt1 = "".join(["0" if i % 2 == 0 else "1" for i in range(len(s))])
        alt2 = "".join(["1" if i % 2 == 0 else "0" for i in range(len(s))])
        
        res = float("inf")
        diff1, diff2 = 0, 0
        l = 0
        
        for r in range(len(s)):
            # Add current character's mismatch to counters
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            
            # Maintain a window of size exactly n
            if (r - l + 1) > n:
                # Remove the leftmost element's mismatch contribution as it leaves the window
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
            
            # When window is size n, update the result with the minimum flips found so far
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
                
        return res
