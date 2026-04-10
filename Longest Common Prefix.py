class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Sort the strings alphabetically
        # The common prefix must be shared between the "smallest" and "largest" string
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        res = ""
        # Compare characters of the first and last strings
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
            
        return res
