class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Strings are equal if characters at even indices match 
        # and characters at odd indices match.
        even_match = sorted(s1[0] + s1[2]) == sorted(s2[0] + s2[2])
        odd_match = sorted(s1[1] + s1[3]) == sorted(s2[1] + s2[3])
        
        return even_match and odd_match
