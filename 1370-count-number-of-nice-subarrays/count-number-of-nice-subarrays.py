class Solution(object):
    def numberOfSubarrays(self, nums, k):

        count = {0: 1}

        prefix = 0
        ans = 0

        for num in nums:

            if num % 2 == 1:
                prefix += 1

            if prefix - k in count:
                ans += count[prefix - k]

            count[prefix] = count.get(prefix, 0) + 1

        return ans