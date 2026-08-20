from collections import Counter

class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False

        count = Counter(nums)

        for num in sorted(count):

            if count[num] == 0:
                continue

            freq = count[num]

            for x in range(num, num + k):

                if count[x] < freq:
                    return False

                count[x] -= freq

        return True