class Solution:

    def jump(self, nums):

        target = len(nums) - 1
        jumps = 0

        while target > 0:

            for i in range(target):

                if i + nums[i] >= target:
                    target = i
                    jumps += 1
                    break

        return jumps