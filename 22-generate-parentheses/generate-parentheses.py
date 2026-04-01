class Solution(object):
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(s, open, close):
            if len(s) == 2 * n:
                res.append("".join(s))
                return
            
            if open < n:
                s.append("(")
                backtrack(s, open + 1, close)
                s.pop()
            
            if close < open:
                s.append(")")
                backtrack(s, open, close + 1)
                s.pop()
        
        backtrack([], 0, 0)
        return res