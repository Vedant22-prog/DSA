class Solution(object):
    def solveNQueens(self, n):
        res = []
        board = ["." * n for _ in range(n)]
        
        cols = set()
        diag = set()      # row - col
        anti = set()      # row + col
        
        def backtrack(row):
            if row == n:
                res.append(board[:])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti:
                    continue
                
                
                cols.add(col)
                diag.add(row - col)
                anti.add(row + col)
                
                board[row] = "." * col + "Q" + "." * (n - col - 1)
                
                backtrack(row + 1)
                
                
                cols.remove(col)
                diag.remove(row - col)
                anti.remove(row + col)
        
        backtrack(0)
        return res
        