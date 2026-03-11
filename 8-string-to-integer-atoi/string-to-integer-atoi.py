import re

class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        
        match = re.match(r'[+-]?\d+', s)
        
        if not match:
            return 0
        
        num = int(match.group())
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        return max(INT_MIN, min(INT_MAX, num))