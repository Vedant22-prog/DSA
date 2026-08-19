class Solution(object):
    def mergeKLists(self, lists):

        def merge(a, b):
            if not a:
                return b

            if not b:
                return a

            if a.val < b.val:
                a.next = merge(a.next, b)
                return a
            else:
                b.next = merge(a, b.next)
                return b

        def solve(left, right):
            if left == right:
                return lists[left]

            mid = (left + right) // 2

            a = solve(left, mid)
            b = solve(mid + 1, right)

            return merge(a, b)

        if not lists:
            return None

        return solve(0, len(lists) - 1)