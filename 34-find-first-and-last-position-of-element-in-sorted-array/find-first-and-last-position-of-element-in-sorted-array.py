class Solution(object):
    def searchRange(self, nums, target):

        def lower_bound():
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper_bound():
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        first = lower_bound()
        last = upper_bound() - 1

        if first <= last and first < len(nums) and nums[first] == target:
            return [first, last]
        return [-1, -1]

        