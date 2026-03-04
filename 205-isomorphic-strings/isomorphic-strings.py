class Solution(object):
    def isIsomorphic(self, s, t):
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True
        