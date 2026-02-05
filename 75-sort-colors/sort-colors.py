class Solution(object):
    def sortColors(self, nums):
        low = 0        # for 0s
        mid = 0        # current index
        high = len(nums) - 1  # for 2s
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        