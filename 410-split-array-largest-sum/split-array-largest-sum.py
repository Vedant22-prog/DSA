class Solution(object):
    def splitArray(self, nums, k):
        
        def canSplit(maxSum):
            count = 1
            currentSum = 0
            
            for num in nums:
                if currentSum + num > maxSum:
                    count += 1
                    currentSum = num
                else:
                    currentSum += num
            
            return count <= k
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        
        return left