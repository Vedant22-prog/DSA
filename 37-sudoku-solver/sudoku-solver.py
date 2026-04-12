class Solution(object):
    def solveSudoku(self, board):
        
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = int(board[i][j]) - 1
                    mask = 1 << num
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i//3)*3 + j//3] |= mask
        
        def backtrack(idx):
            if idx == len(empty):
                return True
            
            r, c = empty[idx]
            b = (r//3)*3 + c//3
            
            used = rows[r] | cols[c] | boxes[b]
            
            for num in range(9):
                if (used >> num) & 1:
                    continue
                
                mask = 1 << num
                board[r][c] = str(num + 1)
                
                rows[r] |= mask
                cols[c] |= mask
                boxes[b] |= mask
                
                if backtrack(idx + 1):
                    return True
                
                rows[r] ^= mask
                cols[c] ^= mask
                boxes[b] ^= mask
                board[r][c] = "."
            
            return False
        
        backtrack(0)