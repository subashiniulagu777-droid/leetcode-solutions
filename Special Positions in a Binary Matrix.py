class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # Calculate the number of 1s in each row and each column
        row_count = [sum(row) for row in mat]
        col_count = [sum(col) for col in zip(*mat)]
        
        special_positions = 0
        
        # Traverse the matrix to check conditions
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # A position is special if it's 1 and is the only 1 in its row and column
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_positions += 1
                    
        return special_positions
