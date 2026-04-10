class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        
        # Step 1: Calculate heights of consecutive 1s for each column
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1 and r > 0:
                    matrix[r][c] += matrix[r-1][c]
            
            # Step 2: Sort the heights in the current row in descending order
            # Sorting allows us to "rearrange" columns to group the tallest ones together
            curr_row = sorted(matrix[r], reverse=True)
            
            # Step 3: Calculate the area for each possible width
            for i in range(cols):
                height = curr_row[i]
                width = i + 1
                ans = max(ans, height * width)
                
        return ans
