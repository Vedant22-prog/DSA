class Solution(object):
    def minimumDistance(self, nums):
        last = {}
        second_last = {}
        
        ans = float('inf')
        
        for i, x in enumerate(nums):
            if x in second_last:
                ans = min(ans, 2 * (i - second_last[x]))
            
            if x in last:
                second_last[x] = last[x]
            
            last[x] = i
        
        return ans if ans != float('inf') else -1
        