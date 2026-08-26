class Solution:

    def candy(self, ratings):

        n = len(ratings)

        left = [1] * n
        right = [1] * n

        # Left requirement
        for i in range(1, n):

            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # Right requirement
        for i in range(n - 2, -1, -1):

            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        total = 0

        for i in range(n):
            total += max(left[i], right[i])

        return total
        