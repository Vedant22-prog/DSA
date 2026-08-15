class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)

        current = sum(cardPoints[:k])
        ans = current

        for i in range(k):
            current -= cardPoints[k - 1 - i]
            current += cardPoints[n - 1 - i]

            ans = max(ans, current)

        return ans