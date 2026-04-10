class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(grid), len(grid[0])
        sums = set()

        for r in range(rows):
            for c in range(cols):
                # Radius 0: Single cell
                sums.add(grid[r][c])
                
                # Radius q > 0
                q = 1
                while True:
                    # Check if the rhombus with radius q fits in the grid
                    if r - q < 0 or r + q >= rows or c - q < 0 or c + q >= cols:
                        break
                    
                    current_sum = 0
                    # Traverse the 4 edges of the rhombus
                    # Top to Right, Right to Bottom, Bottom to Left, Left to Top
                    for i in range(q):
                        current_sum += grid[r - q + i][c + i] # Top-right edge
                        current_sum += grid[r + i][c + q - i] # Right-bottom edge
                        current_sum += grid[r + q - i][c - i] # Bottom-left edge
                        current_sum += grid[r - i][c - q + i] # Left-top edge
                    
                    sums.add(current_sum)
                    q += 1
        
        # Return the 3 largest distinct sums
        return sorted(list(sums), reverse=True)[:3]
