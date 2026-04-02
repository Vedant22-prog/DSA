class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break   # pruning
                
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return res