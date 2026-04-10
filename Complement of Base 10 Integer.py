class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0: return 1
        # Create a mask of 1s with the same bit length as n
        mask = (1 << n.bit_length()) - 1
        # XOR n with the mask to flip all bits
        return n ^ mask
