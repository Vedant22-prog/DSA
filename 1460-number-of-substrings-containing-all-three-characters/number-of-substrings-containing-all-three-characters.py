class Solution(object):
    def numberOfSubstrings(self, s):
        last = [-1, -1, -1]
        ans = 0

        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i

            if min(last) != -1:
                ans += min(last) + 1

        return ans