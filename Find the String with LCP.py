class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        n = len(lcp)
        res = [None] * n
        char_idx = 0
        
        # 1. Greedy construction of the string
        for i in range(n):
            if res[i] is None:
                if char_idx >= 26: return ""  # More than 26 distinct letters needed
                char = chr(ord('a') + char_idx)
                char_idx += 1
                # Any index j where lcp[i][j] > 0 must have the same character
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = char
        
        # If any index didn't get assigned (shouldn't happen with valid LCP), return ""
        if None in res: return ""
        s = "".join(res)
        
        # 2. Validation: Verify the constructed string matches the LCP matrix exactly
        # We check the LCP property: 
        # If s[i] == s[j]: lcp[i][j] = 1 + lcp[i+1][j+1]
        # If s[i] != s[j]: lcp[i][j] = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if s[i] == s[j]:
                    expected = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                
                if lcp[i][j] != expected:
                    return ""
        
        return s
