class Solution(object):
    def lengthOfLongestSubstring(self, s):

        last = {}

        left = 0
        ans = 0

        for right, ch in enumerate(s):

            left = max(left, last.get(ch, -1) + 1)

            last[ch] = right

            ans = max(ans, right - left + 1)

        return ans