class Solution(object):
    def minBitFlips(self, start, goal):
        count = 0
        
        while start > 0 or goal > 0:
            if (start & 1) != (goal & 1):
                count += 1
            
            start >>= 1
            goal >>= 1
        
        return count