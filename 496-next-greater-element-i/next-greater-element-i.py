class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        nxt = {}

        for num in nums2:

            while stack and num > stack[-1]:
                nxt[stack.pop()] = num

            stack.append(num)

        while stack:
            nxt[stack.pop()] = -1

        ans = []

        for num in nums1:
            ans.append(nxt[num])

        return ans