class Solution(object):
    def removeKdigits(self, num, k):
        st = []

        for ch in num:
            while st and k and st[-1] > ch:
                st.pop()
                k -= 1
            st.append(ch)

        st = st[:-k] if k else st

        res = "".join(st).lstrip("0")

        return res if res else "0"