class Solution(object):
    def maxSlidingWindow(self, nums, k):

        n = len(nums)

        if k == 1:
            return nums

        left = [0] * n
        right = [0] * n

        # Left-to-right maximum
        for i in range(n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

        # Right-to-left maximum
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])

        result = []

        for i in range(n - k + 1):
            result.append(max(right[i], left[i + k - 1]))

        return result