class Solution(object):
    def subArrayRanges(self, nums):

        def contribution(is_max):
            n = len(nums)
            stack = []
            total = 0

            for i in range(n + 1):

                while stack and (
                    i == n or
                    (nums[stack[-1]] < nums[i] if is_max else nums[stack[-1]] > nums[i])
                ):

                    mid = stack.pop()

                    left = stack[-1] if stack else -1
                    right = i

                    total += nums[mid] * (mid - left) * (right - mid)

                stack.append(i)

            return total

        max_sum = contribution(True)
        min_sum = contribution(False)

        return max_sum - min_sum