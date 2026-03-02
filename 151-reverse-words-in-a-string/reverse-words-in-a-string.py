class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        s = " ".join(s.split())
        s = list(s[::-1])
        
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                s[start:i] = reversed(s[start:i])
                start = i + 1
        
        return "".join(s)
        