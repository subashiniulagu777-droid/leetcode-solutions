class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        n = len(mat[0])
        # The effective shift is k modulo the number of columns
        shift = k % n
        
        # If shift is 0, the matrix is always identical to itself
        if shift == 0:
            return True
            
        for row in mat:
            for j in range(n):
                # Check if the element at j matches the element k positions away
                if row[j] != row[(j + shift) % n]:
                    return False
        
        return True
