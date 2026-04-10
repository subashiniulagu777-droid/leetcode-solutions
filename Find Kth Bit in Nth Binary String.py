class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Base case: S1 is always "0"
        if n == 1:
            return "0"
        
        # Calculate the middle position of Sn
        # Length of Sn is (2^n) - 1
        mid = (1 << (n - 1))
        
        if k == mid:
            return "1"
        elif k < mid:
            # If k is in the first half, it's the same as in Sn-1
            return self.findKthBit(n - 1, k)
        else:
            # If k is in the second half, it's the inverted bit 
            # of the mirrored position in Sn-1
            mirrored_k = (mid * 2) - k
            res = self.findKthBit(n - 1, mirrored_k)
            return "1" if res == "0" else "0"
