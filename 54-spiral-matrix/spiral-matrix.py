class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        
        while matrix:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        
        return result
