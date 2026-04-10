class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            # Check if result is already computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base Case: If we reached the end of the pattern
            if j == len(p):
                return i == len(s)

            # Check if the current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle the '*' wildcard
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two choices: 
                # 1. Skip the '*' and its preceding character (0 occurrences)
                # 2. Use the '*' if the first character matches (1+ occurrences)
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # No '*', just move both pointers if they match
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
