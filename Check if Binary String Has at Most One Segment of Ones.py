class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # If "01" is present, it means a new segment of ones started after a zero.
        return "01" not in s
