
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        # Cantor's Diagonal Argument:
        # Build a string that differs from the i-th string at the i-th index.
        return "".join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))
