class Solution(object):
    def solveNQueens(self, n):
        res = []
        # Tracking sets for O(1) lookup
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # Base case: All rows filled
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # Check if the position is attacked
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place the queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Move to next row
                backtrack(r + 1)

                # Backtrack: Remove the queen to try next column
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
