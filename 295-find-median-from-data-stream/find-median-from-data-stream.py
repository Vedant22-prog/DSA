class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num):
        self.nums.append(num)

    def findMedian(self):
        self.nums.sort()

        n = len(self.nums)

        if n % 2 == 1:
            return float(self.nums[n // 2])

        left = self.nums[n // 2 - 1]
        right = self.nums[n // 2]

        return (left + right) / 2.0