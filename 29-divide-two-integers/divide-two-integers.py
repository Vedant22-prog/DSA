class Solution(object):
    def divide(self, dividend, divisor):
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        
        for i in range(31, -1, -1):
            if dividend >= (divisor << i):
                dividend -= (divisor << i)
                result += (1 << i)
        
        return sign * result